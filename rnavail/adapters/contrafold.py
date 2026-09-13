"""CONTRAfold: a learned, non-thermodynamic second opinion.

CONTRAfold scores structures with a discriminatively trained conditional
log-linear model instead of measured nearest-neighbour free energies. That
makes it the only genuinely different *model class* in the pipeline, and its
value is precisely in disagreement: a site that both the thermodynamic tools
and CONTRAfold call accessible is more credible than one where they split.

Its posteriors are not free energies, so this adapter deliberately does not
convert them into a dG_open. Doing so would dress a machine-learning
confidence up as thermodynamic work.
"""

from __future__ import annotations

from ..core.result import Availability, M, Tier, ToolResult
from ._contrafold_family import run_predict
from .base import AccessibilityAdapter, AccessibilityRequest
from .external import find_binary
from .registry import register


@register
class ContrafoldAdapter(AccessibilityAdapter):
    name = "contrafold"
    tier = Tier.STRUCTURE
    cost = 2
    orthogonal = True
    #: A trained model's posterior, not a Boltzmann probability (see the
    #: module docstring). Kept out of the primary per-base statistic so a
    #: model confidence never gets averaged in as if it were one.
    estimand = "posterior"
    description = (
        "CONTRAfold posterior pairing probabilities: a learned model whose "
        "agreement or disagreement with the thermodynamic tools is the signal"
    )
    provides = (M.MEAN_BASE_UNPAIRED, M.MIN_BASE_UNPAIRED, M.PAIRED_FRACTION)

    def availability(self) -> Availability:
        if not find_binary("contrafold"):
            return Availability.no(
                "contrafold binary not found", hint="run tools/install_tools.sh"
            )
        return Availability.yes("CONTRAfold")

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        sequence = request.sequence

        if request.settings.is_dna:
            result.warn(
                "CONTRAfold was trained on RNA; its scores for a DNA target "
                "are not meaningful"
            )
        if request.probing is not None:
            result.warn("CONTRAfold ignores probing data supplied to it here")

        paired = run_predict(find_binary("contrafold"), sequence.name, sequence.seq)

        unpaired = [0.0] + [
            max(0.0, min(1.0, 1.0 - paired[i])) for i in range(1, len(sequence) + 1)
        ]
        result.detail["note"] = (
            "posteriors are model confidences, not Boltzmann probabilities; "
            "no opening free energy is derived from them"
        )
        for region in request.regions:
            metrics = result.region_metrics(region)
            values = [unpaired[i] for i in region.positions()]
            mean = sum(values) / len(values)
            metrics.set(M.MEAN_BASE_UNPAIRED, mean)
            metrics.set(M.MIN_BASE_UNPAIRED, min(values))
            metrics.set(M.PAIRED_FRACTION, 1.0 - mean)
        return result
