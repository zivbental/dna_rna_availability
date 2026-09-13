"""LinearFold: linear-time folding for long transcripts.

The cubic-time engines become impractical somewhere around a few thousand
nucleotides, which is well inside the length of a real mRNA. LinearFold folds
in linear time with beam search, so it is the only structure tool here that
scales to a full-length transcript folded as a whole rather than in windows.

The tradeoff is honest and worth stating: beam search returns one structure,
not an ensemble, so this adapter can only report whether a region is paired in
that structure. That is a coarse, binary signal. It belongs in the pipeline as
a fast triage filter and a long-range sanity check on the windowed engines,
never as the basis for a final ranking.
"""

from __future__ import annotations

from ..core.result import Availability, M, Tier, ToolResult
from .base import AccessibilityAdapter, AccessibilityRequest
from .external import find_binary, run_command
from .registry import register


@register
class LinearFoldAdapter(AccessibilityAdapter):
    name = "linearfold"
    tier = Tier.STRUCTURE
    cost = 1
    #: One MFE structure, not an ensemble: values are binary per base
    #: (quantised to multiples of 1/length), so this is excluded from the
    #: primary per-base probability statistic rather than blended into it.
    estimand = "single_structure"
    description = (
        "LinearFold: linear-time whole-transcript MFE structure, for a "
        "long-range check that the windowed engines are not missing burial"
    )
    provides = (M.MFE, M.PAIRED_FRACTION, M.MEAN_BASE_UNPAIRED)

    def availability(self) -> Availability:
        if not find_binary("linearfold"):
            return Availability.no(
                "linearfold binary not found", hint="run tools/install_tools.sh"
            )
        return Availability.yes("LinearFold")

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        sequence = request.sequence

        args = [find_binary("linearfold")]
        # -V selects the Vienna/Turner energy model over the learned CONTRAfold
        # one, keeping this comparable with the rest of the thermodynamic tier.
        if not request.options.get("linearfold_learned_model"):
            args.append("-V")
        beam = request.options.get("linearfold_beam")
        if beam:
            args += ["-b", str(int(beam))]

        proc = run_command(args, stdin=f"{sequence.seq}\n", timeout=1800)
        structure, energy = _parse_linearfold(proc.stdout, len(sequence))
        if structure is None:
            raise RuntimeError("LinearFold produced no structure")

        if energy is not None:
            result.globals[M.MFE] = energy
        result.detail["structure"] = structure
        result.detail["note"] = (
            "a single beam-search structure, not an ensemble: pairing here is "
            "binary and cannot express partial accessibility"
        )

        for region in request.regions:
            metrics = result.region_metrics(region)
            window = region.slice(structure)
            open_fraction = window.count(".") / len(window)
            metrics.set(M.MEAN_BASE_UNPAIRED, open_fraction)
            metrics.set(M.PAIRED_FRACTION, 1.0 - open_fraction)
            metrics.detail["substructure"] = window
        return result


def _parse_linearfold(text: str, length: int) -> tuple[str | None, float | None]:
    """Pull the dot-bracket structure and its energy out of LinearFold output."""
    structure: str | None = None
    energy: float | None = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        candidate = line.split(" ")[0]
        if len(candidate) == length and set(candidate) <= set(".()"):
            structure = candidate
            if "(" in line[len(candidate):]:
                tail = line[len(candidate):].strip().strip("()")
                try:
                    energy = float(tail)
                except ValueError:
                    energy = None
    return structure, energy
