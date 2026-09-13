"""Sequence and region types.

Coordinate convention
---------------------
Every region in rnavail is **1-based and inclusive on both ends**, matching
ViennaRNA, RNAplfold and the way people write about nucleotide positions in
papers. Region 5..12 is eight nucleotides long and includes both 5 and 12.
Conversion to Python slices happens in exactly one place, :meth:`Region.slice`,
so off-by-one errors cannot leak into individual adapters.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Iterator, Literal

Molecule = Literal["rna", "dna"]

_IUPAC_UNAMBIGUOUS = set("ACGU")
_IUPAC_AMBIGUOUS = set("RYSWKMBDHVN")
_WHITESPACE = re.compile(r"\s+")


class SequenceError(ValueError):
    """Raised when a sequence or region cannot be interpreted."""


@dataclass(frozen=True)
class Sequence:
    """A single nucleic-acid sequence.

    The stored sequence is always uppercase and always written in the RNA
    alphabet (T is transcribed to U) regardless of ``molecule``. The
    ``molecule`` field selects the energy parameter set, not the alphabet,
    because ViennaRNA's DNA parameters also expect U-form input.
    """

    name: str
    seq: str
    molecule: Molecule = "rna"
    description: str = ""

    def __post_init__(self) -> None:
        cleaned = _WHITESPACE.sub("", self.seq).upper().replace("T", "U")
        if not cleaned:
            raise SequenceError(f"sequence {self.name!r} is empty")
        bad = set(cleaned) - _IUPAC_UNAMBIGUOUS - _IUPAC_AMBIGUOUS
        if bad:
            raise SequenceError(
                f"sequence {self.name!r} contains non-IUPAC characters: "
                f"{''.join(sorted(bad))}"
            )
        object.__setattr__(self, "seq", cleaned)
        if self.molecule not in ("rna", "dna"):
            raise SequenceError(f"unknown molecule type {self.molecule!r}")

    def __len__(self) -> int:
        return len(self.seq)

    @property
    def has_ambiguous(self) -> bool:
        """True if the sequence contains degenerate IUPAC codes.

        Thermodynamic folding treats these as unpairable, which silently
        inflates apparent accessibility, so callers should warn about them.
        """
        return bool(set(self.seq) & _IUPAC_AMBIGUOUS)

    @property
    def gc_fraction(self) -> float:
        gc = sum(1 for c in self.seq if c in "GC")
        return gc / len(self.seq)

    def as_dna(self) -> str:
        """Return the sequence in the DNA alphabet (U back-transcribed to T)."""
        return self.seq.replace("U", "T")

    @property
    def sha256(self) -> str:
        """Checksum of the normalized sequence and molecule type."""
        payload = f"{self.molecule}:{self.seq}".encode()
        return hashlib.sha256(payload).hexdigest()

    def region(self, start: int, end: int, name: str = "") -> "Region":
        return Region(start=start, end=end, name=name, parent=self.name)


@dataclass(frozen=True)
class Region:
    """A 1-based inclusive interval on a :class:`Sequence`."""

    start: int
    end: int
    name: str = ""
    parent: str = ""

    def __post_init__(self) -> None:
        if self.start < 1:
            raise SequenceError(f"region start must be >= 1, got {self.start}")
        if self.end < self.start:
            raise SequenceError(
                f"region end ({self.end}) precedes start ({self.start})"
            )

    def __len__(self) -> int:
        return self.end - self.start + 1

    @property
    def label(self) -> str:
        return self.name or f"{self.start}-{self.end}"

    def slice(self, seq: str | Sequence) -> str:
        """Extract this region's subsequence, converting 1-based to 0-based."""
        text = seq.seq if isinstance(seq, Sequence) else seq
        if self.end > len(text):
            raise SequenceError(
                f"region {self.label} ends at {self.end} but the sequence is "
                f"only {len(text)} nt long"
            )
        return text[self.start - 1 : self.end]

    def positions(self) -> Iterator[int]:
        """Yield every 1-based position covered by the region."""
        return iter(range(self.start, self.end + 1))

    def overlaps(self, other: "Region") -> bool:
        return self.start <= other.end and other.start <= self.end

    def with_flanks(self, upstream: int, downstream: int, limit: int) -> "Region":
        """Expand the region by flanking context, clipped to ``limit`` nt.

        Used to build the folding context around a target: a recognition site
        must not be folded in isolation, because the neighbouring sequence is
        often exactly what buries it.
        """
        return Region(
            start=max(1, self.start - upstream),
            end=min(limit, self.end + downstream),
            name=f"{self.label}+ctx",
            parent=self.parent,
        )

    def shifted(self, offset: int) -> "Region":
        """Translate the region by ``offset`` nucleotides."""
        return Region(
            start=self.start + offset,
            end=self.end + offset,
            name=self.name,
            parent=self.parent,
        )

    def to_local(self, context: "Region") -> "Region":
        """Re-express this region in coordinates local to ``context``.

        When a target is folded inside a windowed context, adapters need the
        target's position *within that window*, which is what this returns.
        """
        if not (context.start <= self.start and self.end <= context.end):
            raise SequenceError(
                f"region {self.label} is not contained in context {context.label}"
            )
        return self.shifted(1 - context.start)


def parse_region(spec: str, sequence: Sequence | None = None) -> Region:
    """Parse a region given as ``start-end``, ``start..end`` or ``name:start-end``.

    A bare nucleotide string is also accepted and located in ``sequence``,
    which is convenient when the user knows the trigger sequence but not its
    coordinates.
    """
    spec = spec.strip()
    name = ""
    if ":" in spec:
        name, spec = spec.split(":", 1)
        name, spec = name.strip(), spec.strip()

    match = re.fullmatch(r"(\d+)\s*(?:-|\.\.)\s*(\d+)", spec)
    if match:
        return Region(int(match.group(1)), int(match.group(2)), name=name)

    candidate = _WHITESPACE.sub("", spec).upper().replace("T", "U")
    if candidate and set(candidate) <= _IUPAC_UNAMBIGUOUS | _IUPAC_AMBIGUOUS:
        if sequence is None:
            raise SequenceError(
                f"region {spec!r} looks like a subsequence but no parent "
                "sequence was supplied to locate it in"
            )
        index = sequence.seq.find(candidate)
        if index < 0:
            raise SequenceError(
                f"subsequence {candidate!r} does not occur in {sequence.name!r}"
            )
        if sequence.seq.find(candidate, index + 1) >= 0:
            raise SequenceError(
                f"subsequence {candidate!r} occurs more than once in "
                f"{sequence.name!r}; specify explicit coordinates instead"
            )
        return Region(index + 1, index + len(candidate), name=name or "match")

    raise SequenceError(f"cannot interpret region specification {spec!r}")


def tile_regions(
    length: int,
    window: int,
    step: int = 1,
    name_prefix: str = "w",
) -> list[Region]:
    """Generate every candidate window of ``window`` nt across ``length``."""
    if window <= 0:
        raise SequenceError("window length must be positive")
    if step <= 0:
        raise SequenceError("step must be positive")
    if window > length:
        raise SequenceError(
            f"window ({window} nt) is longer than the sequence ({length} nt)"
        )
    return [
        Region(start, start + window - 1, name=f"{name_prefix}{start}")
        for start in range(1, length - window + 2, step)
    ]
