"""EternaFold: CONTRAfold's model class retrained on chemical-mapping data.

EternaFold (Wayment-Steele et al. 2022, *Nature Methods*) runs the identical
CONTRAfold inference engine under a parameter set fit by multitask learning
across roughly a million Eterna crowdsourced SHAPE/DMS measurements plus
several other probing datasets, rather than CONTRAfold's original CRW-derived
training set. Same model *class* as ``contrafold``, different training data —
which is what makes it a genuinely second opinion rather than a duplicate:
the two are registered under different ``independence_group`` values (each
defaulting to its own name) so the consensus layer treats them as two votes,
not one calculation checked twice. The published benchmark found the biggest
gains over stock CONTRAfold specifically on ensemble/accessibility tasks
rather than MFE structure, which is the quantity this pipeline ranks on.

Like ``contrafold``, its posteriors are a trained model's confidence, not a
Boltzmann probability, so this adapter never converts them into a dG_open.
"""

from __future__ import annotations

from pathlib import Path

from ..core.result import Availability, M, Tier, ToolResult
from ._contrafold_family import run_predict
from .base import AccessibilityAdapter, AccessibilityRequest
from .external import find_binary
from .registry import register

#: Bundled with this repo rather than fetched at install time: ~20 KB of
#: plain text, stable across releases, BSD-3-Clause licensed by Stanford
#: (see https://github.com/eternagame/EternaFold), so redistributing it here
#: needs no network access at install time the way the multi-GB tool
#: binaries in tools/install_tools.sh do.
PARAMS_PATH = Path(__file__).parent / "data" / "EternaFoldParams.v1"


@register
class EternaFoldAdapter(AccessibilityAdapter):
    name = "eternafold"
    tier = Tier.STRUCTURE
    cost = 2
    orthogonal = True
    #: A trained model's posterior, not a Boltzmann probability (see the
    #: module docstring). Kept out of the primary per-base statistic so a
    #: model confidence never gets averaged in as if it were one.
    estimand = "posterior"
    description = (
        "EternaFold posterior pairing probabilities: CONTRAfold's model "
        "retrained on ~1M Eterna crowdsourced chemical-mapping measurements; "
        "a second, independently-trained learned model rather than a "
        "duplicate of contrafold"
    )
    provides = (M.MEAN_BASE_UNPAIRED, M.MIN_BASE_UNPAIRED, M.PAIRED_FRACTION)

    def availability(self) -> Availability:
        if not find_binary("contrafold"):
            return Availability.no(
                "contrafold binary not found (eternafold reuses the "
                "CONTRAfold binary with a different --params file)",
                hint="run tools/install_tools.sh",
            )
        if not PARAMS_PATH.is_file():
            return Availability.no(
                f"EternaFold parameter file missing at {PARAMS_PATH}",
                hint="reinstall rnavail; the file ships with the package",
            )
        return Availability.yes("EternaFoldParams.v1 on CONTRAfold 2.02")

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        sequence = request.sequence

        if request.settings.is_dna:
            result.warn(
                "EternaFold was trained on RNA; its scores for a DNA target "
                "are not meaningful"
            )
        if request.probing is not None:
            result.warn("EternaFold ignores probing data supplied to it here")

        paired = run_predict(
            find_binary("contrafold"), sequence.name, sequence.seq,
            params_path=str(PARAMS_PATH),
        )

        unpaired = [0.0] + [
            max(0.0, min(1.0, 1.0 - paired[i])) for i in range(1, len(sequence) + 1)
        ]
        result.detail["note"] = (
            "posteriors are model confidences, not Boltzmann probabilities; "
            "no opening free energy is derived from them"
        )
        result.detail["params"] = "EternaFoldParams.v1"
        for region in request.regions:
            metrics = result.region_metrics(region)
            values = [unpaired[i] for i in region.positions()]
            mean = sum(values) / len(values)
            metrics.set(M.MEAN_BASE_UNPAIRED, mean)
            metrics.set(M.MIN_BASE_UNPAIRED, min(values))
            metrics.set(M.PAIRED_FRACTION, 1.0 - mean)
        return result
