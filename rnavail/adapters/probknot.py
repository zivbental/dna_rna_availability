"""ProbKnot: pseudoknot-aware pairing, as a check on a blind spot every other
adapter here shares.

RNAplfold, the exact partition function, RNAfold, RNAstructure's partition
function, CONTRAfold and LinearFold are all, by construction, restricted to
*nested* secondary structure: no base pair may cross another. That is a
deliberate and almost always correct simplification, and it is also exactly
wrong for the minority of sites where a real crossing interaction — a
pseudoknot — locks the region up. A site every one of those tools calls open
can be pseudoknotted shut, and nothing above would ever show it.

ProbKnot builds its structure from RNAstructure's own partition function
(iteratively pairing each base with its most probable partner, so it shares
an energy model with ``rnastructure-partition``) but does not forbid crossing
pairs. That makes its *disagreement* with the nested-only tools the useful
signal, in the same spirit as ``contrafold``: when it agrees, nothing here is
missed; when it reports much heavier pairing, a pseudoknot is a real
candidate explanation and none of the other tools could have told you.

This is one prediction of one algorithm, not an ensemble probability, so it
gets the same weight as ``linearfold`` or ``contrafold`` output: a diagnostic
cross-check on the joint accessibility, never a substitute for it.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from ..core.result import Availability, M, Tier, ToolResult
from .base import AccessibilityAdapter, AccessibilityRequest
from .external import find_binary, probe_version, rnastructure_datapath, run_command
from .registry import register


@register
class ProbKnotAdapter(AccessibilityAdapter):
    name = "probknot"
    tier = Tier.STRUCTURE
    cost = 3
    orthogonal = True
    #: Built on RNAstructure's own partition function, same codebase and
    #: parameter tables as rnastructure-partition — grouped so the two don't
    #: count as independent votes on the same underlying calculation.
    independence_group = "rnastructure"
    #: One iteratively-built pairing, not an ensemble probability: values
    #: are quantised to multiples of 1/length. Excluded from the primary
    #: per-base statistic so it isn't averaged in as though it were one.
    estimand = "single_structure"
    description = (
        "RNAstructure ProbKnot: pseudoknot-capable pairing, the one adapter "
        "here not restricted to nested secondary structure"
    )
    provides = (
        M.MEAN_BASE_UNPAIRED, M.MIN_BASE_UNPAIRED, M.PAIRED_FRACTION,
        M.PSEUDOKNOT_PAIRED_FRACTION,
    )

    def availability(self) -> Availability:
        if not find_binary("ProbKnot"):
            return Availability.no(
                "ProbKnot binary not found", hint="run tools/install_tools.sh"
            )
        if not rnastructure_datapath():
            return Availability.no(
                "RNAstructure data tables not found",
                hint="set DATAPATH to the RNAstructure data_tables directory",
            )
        return Availability.yes(probe_version("ProbKnot", ["--version"]))

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        sequence = request.sequence

        with tempfile.TemporaryDirectory(prefix="rnavail-probknot-") as workdir:
            work = Path(workdir)
            fasta = work / "target.fa"
            fasta.write_text(f">{sequence.name}\n{sequence.seq}\n")
            ct = work / "target.ct"

            args = [find_binary("ProbKnot"), str(fasta), str(ct), "--sequence"]
            if settings.is_dna:
                args.append("--DNA")
            run_command(args, timeout=1800)
            partner = _parse_ct(ct.read_text(), len(sequence))

        crossing = _crossing_positions(partner)
        n_pseudoknotted = sum(crossing)
        result.detail["has_pseudoknot"] = n_pseudoknotted > 0
        result.detail["pseudoknotted_bases"] = n_pseudoknotted
        result.detail["note"] = (
            "one MFE-style pairing prediction, not an ensemble probability; "
            "read as a structural hypothesis to cross-check, not a P_unpaired"
        )

        for region in request.regions:
            metrics = result.region_metrics(region)
            positions = list(region.positions())
            paired_here = [partner[i] != 0 for i in positions]
            unpaired_here = [0.0 if p else 1.0 for p in paired_here]
            mean_unpaired = sum(unpaired_here) / len(unpaired_here)
            metrics.set(M.MEAN_BASE_UNPAIRED, mean_unpaired)
            metrics.set(M.MIN_BASE_UNPAIRED, min(unpaired_here))
            metrics.set(M.PAIRED_FRACTION, 1.0 - mean_unpaired)

            pk_here = [crossing[i] for i in positions]
            metrics.set(M.PSEUDOKNOT_PAIRED_FRACTION, sum(pk_here) / len(pk_here))
            if any(pk_here):
                example = next(
                    (i, partner[i]) for i in positions if crossing[i]
                )
                metrics.detail["pseudoknot_example_pair"] = example
        return result


def _parse_ct(text: str, length: int) -> list[int]:
    """Pairing partner per position from an RNAstructure .ct file, 1-based.

    Column layout is ``index base prev next partner original``; ``partner``
    is 0 for an unpaired base. The header line (sequence length and name) has
    a different shape and is skipped by the field-count check.
    """
    partner = [0] * (length + 1)
    for line in text.splitlines():
        fields = line.split()
        if len(fields) != 6:
            continue
        try:
            i, j = int(fields[0]), int(fields[4])
        except ValueError:
            continue
        if 1 <= i <= length:
            partner[i] = j if 1 <= j <= length else 0
    return partner


def _crossing_positions(partner: list[int]) -> list[bool]:
    """Flag every base in a pair that crosses another pair — a pseudoknot.

    Pairs (i, j) and (k, l) with i < j and k < l cross when exactly one of
    k, l falls strictly inside (i, j): that is the geometric definition of a
    pseudoknot, as opposed to nested or disjoint pairs.
    """
    length = len(partner) - 1
    pairs = [
        (i, partner[i]) for i in range(1, length + 1)
        if 0 < partner[i] and i < partner[i]
    ]
    crossing = [False] * (length + 1)
    for a, (i, j) in enumerate(pairs):
        for k, l in pairs[a + 1:]:
            if (i < k < j) != (i < l < j):
                crossing[i] = crossing[j] = crossing[k] = crossing[l] = True
    return crossing
