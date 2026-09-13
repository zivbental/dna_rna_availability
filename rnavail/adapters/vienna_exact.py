"""Joint opening free energy by constrained partition function.

This is the reference implementation of the quantity the whole pipeline is
built on. Where RNAplfold approximates P_unpaired(i,j) inside a sliding
window, this adapter computes the constrained partition-function value exactly
*under the declared ViennaRNA model and scope* by running the partition
function twice:

    dG_open(i,j) = G_ensemble[i..j forced unpaired] - G_ensemble[unconstrained]

and P_unpaired(i,j) = exp(-dG_open/RT). It is the Raccess definition evaluated
with ViennaRNA's energy model, and unlike a lookup table it works for target
intervals of any length.

Cost is one extra partition function per region, so it is the right tool for
tens or hundreds of shortlisted regions, not for a transcriptome scan.
"""

from __future__ import annotations

import math

from ..core.model import ModelSettings
from ..core.result import Availability, M, Tier, ToolResult
from ..core.sequence import Region, Sequence
from ..core import thermo
from . import _vienna as V
from .base import AccessibilityAdapter, AccessibilityRequest
from .registry import register

#: Above this many partition-function calls a full exact seed scan is
#: replaced by a strided one, to keep a single region from taking minutes.
SEED_SCAN_BUDGET = 40


@register
class ViennaExactAdapter(AccessibilityAdapter):
    name = "vienna-exact"
    tier = Tier.ACCESSIBILITY
    cost = 3
    probing_methods = frozenset({"deigan", "zarringhalam", "eddy2"})
    independence_group = "vienna-global-pf"
    model_family = "vienna-turner"
    algorithm = "constrained-partition-function"
    applied_setting_names = frozenset({
        "temperature_c", "param_set", "dangles", "no_lonely_pairs",
        "no_gu", "no_gu_closure", "gquad", "circular", "salt_molar",
        "global_max_bp_span",
    })
    ignored_setting_names = frozenset({
        "max_bp_span", "window_size", "max_unpaired",
    })
    description = (
        "Joint unpaired probability and opening free energy from constrained "
        "partition functions (exact under the declared ViennaRNA model)"
    )
    provides = (
        M.P_UNPAIRED, M.DG_OPEN, M.DG_OPEN_PER_NT,
        M.SEED_P_UNPAIRED, M.SEED_DG_OPEN, M.SEED_START, M.SEED_LENGTH,
        M.ENSEMBLE_FREE_ENERGY,
    )

    def availability(self) -> Availability:
        return V.availability()

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        seq = request.sequence.seq
        temperature = settings.temperature_c

        if request.sequence.has_ambiguous:
            result.warn(
                "sequence contains ambiguous IUPAC codes, which fold as "
                "unpairable and will overstate accessibility"
            )

        reference = V.make_fold_compound(seq, settings, probing=request.probing)
        g_free = V.ensemble_free_energy(reference)
        result.globals[M.ENSEMBLE_FREE_ENERGY] = g_free
        result.detail["reference_free_energy"] = g_free

        def dg_open_of(region: Region) -> float:
            g_constrained = V.constrained_free_energy(
                seq, settings, region.positions(), probing=request.probing
            )
            return g_constrained - g_free

        for region in request.regions:
            metrics = result.region_metrics(region)
            dg_open = dg_open_of(region)
            metrics.set(M.DG_OPEN, dg_open)
            metrics.set(M.DG_OPEN_PER_NT, thermo.dg_open_per_nucleotide(dg_open, len(region)))
            metrics.set(M.P_UNPAIRED, thermo.probability_from_dg_open(dg_open, temperature))

            seed = self._scan_seed(
                region, request.seed_length, request.seed_starts(region),
                dg_open_of, temperature, result
            )
            seed_scan = result.detail.get("seed_scans", {}).get(region.label)
            if seed_scan is not None:
                metrics.detail["seed_trials"] = seed_scan["trials"]
            if seed is not None:
                seed_start, seed_dg = seed
                metrics.set(M.SEED_START, seed_start)
                metrics.set(M.SEED_LENGTH, request.seed_length)
                metrics.set(M.SEED_DG_OPEN, seed_dg)
                metrics.set(
                    M.SEED_P_UNPAIRED,
                    thermo.probability_from_dg_open(seed_dg, temperature),
                )
                metrics.detail["seed_selection_note"] = (
                    "lowest-opening-energy permitted placement selected from "
                    "the evaluated trials"
                )
        return result

    def _scan_seed(
        self,
        region: Region,
        seed_length: int,
        allowed_starts: list[int],
        dg_open_of: "callable",
        temperature: float,
        result: ToolResult,
    ) -> tuple[int, float] | None:
        """Locate the cheapest-to-open seed window inside ``region``.

        A trigger does not need its whole footprint open at once to start
        binding; it needs a nucleation site. This finds the best one, which
        is frequently far more accessible than the full interval.
        """
        if seed_length > len(region) or not allowed_starts:
            result.detail.setdefault("seed_scans", {})[region.label] = {
                "placements": 0,
                "tested_starts": [],
                "omitted_starts": [],
                "trials": [],
            }
            return None
        placements = len(allowed_starts)
        stride = 1
        if placements > SEED_SCAN_BUDGET:
            stride = -(-placements // SEED_SCAN_BUDGET)   # ceiling division
            result.warn(
                f"region {region.label}: {placements} seed placements exceeds "
                f"the exact budget, scanning every {stride}th offset instead"
            )

        indices = list(range(0, placements, stride))
        if indices[-1] != placements - 1:
            indices.append(placements - 1)
        tested_starts = [allowed_starts[index] for index in indices]
        tested_set = set(tested_starts)
        trials_by_start: dict[int, dict[str, object]] = {
            start: {
                "start": start,
                "end": start + seed_length - 1,
                "p_unpaired": None,
                "dg_open_kcal_mol": None,
                "estimate_kind": "not_evaluated",
                "reason": (
                    "not evaluated because the exact seed-scan budget "
                    "selected other permitted placements"
                ),
            }
            for start in allowed_starts
        }
        for start in tested_starts:
            # The result remains an energy point estimate even if converting
            # it to a binary64 probability underflows.  Preserve that status
            # instead of presenting a numerical zero as a measured event.
            seed = Region(start, start + seed_length - 1)
            dg_open = float(dg_open_of(seed))
            trial = trials_by_start[start]
            if not math.isfinite(dg_open):
                trial["estimate_kind"] = "unavailable"
                trial["reason"] = "exact constrained calculation was nonfinite"
                continue
            probability = thermo.probability_from_dg_open(dg_open, temperature)
            trial["dg_open_kcal_mol"] = dg_open
            trial["p_unpaired"] = probability
            if probability == 0.0:
                trial["estimate_kind"] = "censored"
                trial["censor_reason"] = (
                    "probability conversion underflowed; finite opening energy "
                    "is retained"
                )
            else:
                trial["estimate_kind"] = "point"
            trial.pop("reason", None)

        result.detail.setdefault("seed_scans", {})[region.label] = {
            "placements": placements,
            "tested_starts": tested_starts,
            "omitted_starts": [
                start for start in allowed_starts if start not in tested_set
            ],
            "trials": [trials_by_start[start] for start in allowed_starts],
        }

        best: tuple[int, float] | None = None
        for start in tested_starts:
            trial = trials_by_start[start]
            dg_open = trial["dg_open_kcal_mol"]
            if not isinstance(dg_open, (int, float)):
                continue
            if best is None or float(dg_open) < best[1]:
                best = (start, float(dg_open))
        return best
