"""Minimal FASTA and probing-file readers.

Deliberately dependency-free: the pipeline already asks a lot of the user's
environment, and reading a FASTA is not worth another install.
"""

from __future__ import annotations

import math
import hashlib
from pathlib import Path
from typing import Iterator

from ..core.model import ProbingData
from ..core.sequence import Molecule, Sequence, SequenceError


def read_fasta(path: str | Path, molecule: Molecule = "rna") -> list[Sequence]:
    """Read every record from a FASTA file."""
    records = list(iter_fasta(path, molecule))
    if not records:
        raise SequenceError(f"no sequences found in {path}")
    return records


def iter_fasta(path: str | Path, molecule: Molecule = "rna") -> Iterator[Sequence]:
    """Stream FASTA records without holding the whole file in memory."""
    path = Path(path)
    name, description, chunks = "", "", []

    def emit() -> Sequence | None:
        if not chunks:
            return None
        return Sequence(
            name=name or path.stem,
            seq="".join(chunks),
            molecule=molecule,
            description=description,
        )

    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                record = emit()
                if record is not None:
                    yield record
                header = line[1:].strip()
                name, _, description = header.partition(" ")
                chunks = []
            else:
                chunks.append(line)
    record = emit()
    if record is not None:
        yield record


def read_sequence(spec: str, molecule: Molecule = "rna",
                  name: str = "sequence", record: str | None = None) -> Sequence:
    """Accept either a path to a FASTA file or a literal nucleotide string."""
    path = Path(spec)
    if path.is_file():
        records = read_fasta(path, molecule)
        if record is not None:
            matches = [item for item in records if item.name == record]
            if not matches:
                raise SequenceError(
                    f"FASTA {path} has no record {record!r}; available: "
                    + ", ".join(item.name for item in records)
                )
            return matches[0]
        if len(records) != 1:
            raise SequenceError(
                f"FASTA {path} contains {len(records)} records; choose one "
                "with --record"
            )
        return records[0]
    return Sequence(name=name, seq=spec, molecule=molecule)


def read_probing(path: str | Path, length: int | Sequence, method: str = "deigan",
                 slope: float = 1.8, intercept: float = -0.6,
                 beta: float = 0.89,
                 chemistry: str = "SHAPE",
                 condition_id: str = "unspecified",
                 conversion_explicit: bool = False) -> ProbingData:
    """Read reactivities from a two- or three-column SHAPE/DMS file.

    Accepts ``position<TAB>reactivity`` or ``position<TAB>base<TAB>reactivity``.
    Values of -999, NA or nan mark positions without data, which are left
    unconstrained rather than being treated as zero reactivity: a missing
    measurement is not evidence of pairing.
    """
    path = Path(path)
    sequence = length
    length = sequence if isinstance(sequence, int) else len(sequence)
    values: dict[int, float | None] = {}
    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        try:
            position = int(fields[0])
        except (ValueError, IndexError):
            raise SequenceError(
                f"{path}:{lineno}: expected a position in the first column"
            ) from None
        if position < 1:
            raise SequenceError(
                f"{path}:{lineno}: position must be one-based and positive"
            )
        if position in values:
            raise SequenceError(
                f"{path}:{lineno}: duplicate probing position {position}"
            )
        if not isinstance(sequence, int) and len(fields) >= 3:
            observed = fields[1].upper().replace("T", "U")
            expected = sequence.seq[position - 1] if position <= length else None
            if expected is not None and observed != expected:
                raise SequenceError(
                    f"{path}:{lineno}: base {observed!r} at position {position} "
                    f"does not match target base {expected!r}"
                )
        raw = fields[-1]
        if raw.upper() in ("NA", "NAN", "-999", "-999.0", "."):
            values[position] = None
            continue
        try:
            reactivity = float(raw)
        except ValueError:
            raise SequenceError(
                f"{path}:{lineno}: cannot read {raw!r} as a reactivity"
            ) from None
        if not math.isfinite(reactivity):
            raise SequenceError(
                f"{path}:{lineno}: reactivity must be finite or an explicit "
                "missing-value marker"
            )
        values[position] = None if reactivity <= -500 else reactivity

    if not values:
        raise SequenceError(f"no reactivities found in {path}")
    highest = max(values)
    if highest > length:
        raise SequenceError(
            f"{path} has data at position {highest} but the sequence is only "
            f"{length} nt long"
        )
    return ProbingData(
        reactivities=tuple(values.get(i) for i in range(1, length + 1)),
        method=method, source=str(path), slope=slope, intercept=intercept,
        beta=beta,
        chemistry=chemistry, condition_id=condition_id,
        sequence_hash=("" if isinstance(sequence, int) else sequence.sha256),
        source_hash=hashlib.sha256(path.read_bytes()).hexdigest(),
        conversion_explicit=conversion_explicit,
    )
