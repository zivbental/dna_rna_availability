"""Global partition-function structure descriptors (RNAfold-equivalent).

This adapter does not produce the joint accessibility the ranking is built on;
it produces the context you need to interpret that number. A region can look
accessible simply because the whole transcript is poorly determined, and the
ensemble diagnostics here are what expose that.

The MFE-to-ensemble gap in particular quantifies the Boltzmann weight of the
MFE state. A small gap means high MFE-state probability; a large gap means the
partition function contains substantial weight outside that single state.
"""

from __future__ import annotations

import math

from ..core import thermo
from ..core.result import Availability, M, Tier, ToolResult
from ..core.sequence import Region
from . import _vienna as V
from .base import AccessibilityAdapter, AccessibilityRequest
from .registry import register


@register
class ViennaFoldAdapter(AccessibilityAdapter):
    name = "rnafold"
    tier = Tier.STRUCTURE
    cost = 2
    probing_methods = frozenset({"deigan", "zarringhalam", "eddy2"})
    independence_group = "vienna-global-pf"
    model_family = "vienna-turner"
    algorithm = "global-partition-function"
    applied_setting_names = frozenset({
        "temperature_c", "param_set", "dangles", "no_lonely_pairs",
        "no_gu", "no_gu_closure", "gquad", "circular", "salt_molar",
        "global_max_bp_span",
    })
    ignored_setting_names = frozenset({
        "max_bp_span", "window_size", "max_unpaired",
    })
    description = (
        "Global partition function: MFE, ensemble free energy, per-base "
        "pairing probabilities and positional entropy"
    )
    provides = (
        M.MFE, M.ENSEMBLE_FREE_ENERGY, M.MFE_ENSEMBLE_GAP, M.MEAN_BP_DISTANCE,
        M.MEAN_BASE_UNPAIRED, M.MIN_BASE_UNPAIRED, M.PAIRED_FRACTION,
        M.SHANNON_ENTROPY,
    )

    def availability(self) -> Availability:
        return V.availability()

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        seq = request.sequence.seq

        fc = V.make_fold_compound(seq, settings, probing=request.probing)
        mfe_structure, mfe_energy = fc.mfe()
        # Rescaling by the MFE keeps the partition function numerically stable
        # on long sequences, where the unscaled Boltzmann sum overflows.
        fc.exp_params_rescale(mfe_energy)
        pf_structure, ensemble_energy = fc.pf()

        result.globals[M.MFE] = float(mfe_energy)
        result.globals[M.ENSEMBLE_FREE_ENERGY] = float(ensemble_energy)
        result.globals[M.MFE_ENSEMBLE_GAP] = float(mfe_energy - ensemble_energy)
        result.globals[M.MEAN_BP_DISTANCE] = float(fc.mean_bp_distance())
        result.detail["mfe_structure"] = mfe_structure
        result.detail["pairing_propensity_structure"] = pf_structure
        centroid_structure, centroid_distance = fc.centroid()
        result.detail["centroid_structure"] = centroid_structure
        result.detail["centroid_distance"] = float(centroid_distance)
        mea_structure, mea_score = fc.MEA()
        result.detail["mea_structure"] = mea_structure

        gap = float(mfe_energy - ensemble_energy)
        if gap > 0.5:
            mfe_probability = math.exp(-gap / thermo.rt(settings.temperature_c))
            result.warn(
                "MFE and ensemble free energy differ by more than 0.5 kcal/mol "
                f"(MFE-state probability {mfe_probability:.3f}): "
                "substantial ensemble weight lies outside the MFE state"
            )

        unpaired = None if settings.gquad else V.unpaired_probabilities(fc)
        entropy = None if settings.gquad else V.positional_entropy(fc)

        if settings.gquad:
            result.warn(
                "per-base unpaired probabilities are omitted with gquad=True "
                "because the base-pair matrix does not encode G4 occupancy"
            )

        for region in request.regions:
            metrics = result.region_metrics(region)
            if unpaired is not None:
                values = [unpaired[i] for i in region.positions()]
                metrics.set(M.MEAN_BASE_UNPAIRED, sum(values) / len(values))
                metrics.set(M.MIN_BASE_UNPAIRED, min(values))
                metrics.set(M.PAIRED_FRACTION, 1.0 - sum(values) / len(values))
            if entropy is not None:
                window = [entropy[i] for i in region.positions() if i < len(entropy)]
                if window:
                    metrics.set(M.SHANNON_ENTROPY, sum(window) / len(window))
            metrics.detail["mfe_substructure"] = region.slice(mfe_structure)
        return result
