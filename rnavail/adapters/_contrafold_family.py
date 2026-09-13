"""Shared plumbing for the two adapters that drive the CONTRAfold binary.

``contrafold`` and ``eternafold`` are the same C++ inference engine run under
two different trained parameter sets — stock CONTRAfold's, and EternaFold's
retraining of the same model class on Eterna's crowdsourced chemical-mapping
data (Wayment-Steele et al. 2022). Everything except *which* ``--params`` flag
gets passed is identical, so that plumbing lives here once.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from .external import run_command


def run_predict(binary: str, sequence_name: str, sequence: str,
                params_path: str | None = None) -> list[float]:
    """Run ``contrafold predict`` and return summed pairing posteriors.

    Returns a 1-based list (index 0 unused) of the total posterior pairing
    probability at each position, from CONTRAfold's own posterior decoding.
    """
    with tempfile.TemporaryDirectory(prefix="rnavail-contrafold-") as workdir:
        work = Path(workdir)
        fasta = work / "target.fa"
        fasta.write_text(f">{sequence_name}\n{sequence}\n")
        posteriors = work / "posteriors.txt"
        args = [binary, "predict", str(fasta)]
        if params_path:
            args += ["--params", str(params_path)]
        args += ["--posteriors", "0.001", str(posteriors)]
        run_command(args, timeout=1800)
        return parse_posteriors(posteriors.read_text(), len(sequence))


def parse_posteriors(text: str, length: int) -> list[float]:
    """Sum CONTRAfold posteriors per nucleotide.

    Each line is ``position base partner:probability ...`` and lists only
    pairs above the reporting threshold, once per pair from the lower index.
    """
    paired = [0.0] * (length + 1)
    for line in text.splitlines():
        fields = line.split()
        if len(fields) < 2:
            continue
        try:
            i = int(fields[0])
        except ValueError:
            continue
        if not 1 <= i <= length:
            continue
        for entry in fields[2:]:
            if ":" not in entry:
                continue
            partner, _, value = entry.partition(":")
            try:
                j, probability = int(partner), float(value)
            except ValueError:
                continue
            if 1 <= j <= length:
                paired[i] += probability
                paired[j] += probability
    return paired
