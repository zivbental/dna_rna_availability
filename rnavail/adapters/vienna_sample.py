"""Boltzmann ensemble sampling (the Sfold strategy, via ViennaRNA).

Stochastic backtracking draws structures from the Boltzmann distribution, so
the fraction of samples in which a target interval is completely unpaired is
a Monte Carlo estimate of P_unpaired(i,j). It samples the same declared
ViennaRNA whole-sequence ensemble as the constrained partition-function path,
so it is useful for inspecting state populations and numerical sampling
behavior, not as an independent biological measurement.

It also does something the DP engines cannot, which is report *how* a region
is buried. Sampled structures are classified into exposed / partly exposed /
buried states, giving an interpretable population breakdown rather than a
single mean accessibility number.

The known weakness, which this adapter reports rather than hides, is rare
events: when a region is open in one sample per million, no feasible number of
draws will estimate its probability. Whenever zero samples land in the exposed
state the result carries an upper bound instead of a point estimate; a
constrained partition-function calculation can resolve that event under its
own declared global scope. Comparisons across scope or model assumptions still
need to be reported as sensitivity, rather than treated as a validation vote.
"""

from __future__ import annotations

import math

from ..core.result import Availability, M, Tier, ToolResult
from ..core.sequence import Region
from ..core import thermo
from . import _vienna as V
from .base import AccessibilityAdapter, AccessibilityRequest
from .registry import register

DEFAULT_SAMPLES = 2000

#: Fixed RNG seed so repeated runs give identical numbers. Pass
#: ``sampling_seed=None`` to draw fresh samples instead.
DEFAULT_SEED = 20260903
#: A region is called "partly exposed" when at least this fraction of its
#: nucleotides are unpaired in a sampled structure.
PARTIAL_THRESHOLD = 0.5


@register
class ViennaSampleAdapter(AccessibilityAdapter):
    name = "ensemble-sample"
    tier = Tier.STRUCTURE
    cost = 3
    probing_methods = frozenset({"deigan", "zarringhalam", "eddy2"})
    # Sampling is a numerical check on the same whole-sequence partition
    # function as vienna-exact, not another independent biological vote.
    independence_group = "vienna-global-pf"
    # A Monte Carlo estimate remains useful when it is the only requested
    # observation, but it must not be averaged into the exact dynamic-
    # programming probability from the same ensemble.
    estimand = "monte_carlo_probability"
    model_family = "vienna-turner"
    algorithm = "boltzmann-stochastic-backtracking"
    applied_setting_names = frozenset({
        "temperature_c", "param_set", "dangles", "no_lonely_pairs",
        "no_gu", "no_gu_closure", "gquad", "circular", "salt_molar",
        "global_max_bp_span",
    })
    ignored_setting_names = frozenset({
        "max_bp_span", "window_size", "max_unpaired",
    })
    description = (
        "Boltzmann ensemble sampling (Sfold-style): Monte Carlo accessibility "
        "with sampling error, plus exposed/partial/buried state populations"
    )
    provides = (
        M.P_UNPAIRED, M.DG_OPEN, M.DG_OPEN_PER_NT, M.MEAN_BASE_UNPAIRED,
        M.SEED_P_UNPAIRED, M.SEED_START, M.SEED_LENGTH,
    )

    def availability(self) -> Availability:
        return V.availability()

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        samples = int(request.options.get("samples", DEFAULT_SAMPLES))
        temperature = settings.temperature_c

        # Seed the sampler so a run is reproducible. Without this the only
        # stochastic adapter in the pipeline makes every consensus median
        # drift between runs, which is indistinguishable from a real change
        # when you are comparing two candidate rankings.
        seed = request.options.get("sampling_seed", DEFAULT_SEED)
        if seed is not None:
            V.RNA.init_rand(int(seed))
        result.detail["sampling_seed"] = seed

        fc = V.make_fold_compound(
            request.sequence.seq, settings, probing=request.probing, uniq_ml=True
        )
        _, mfe_energy = fc.mfe()
        fc.exp_params_rescale(mfe_energy)
        fc.pf()

        structures = list(fc.pbacktrack(samples))
        if not structures:
            raise RuntimeError(
                "stochastic backtracking returned no structures; the "
                "partition function may have failed to converge"
            )
        drawn = len(structures)
        result.globals["samples"] = float(drawn)
        result.detail["requested_samples"] = samples

        # Precompute an unpaired mask per structure once, rather than
        # re-parsing dot-bracket for every region.
        masks = [[c == "." for c in s] for s in structures]

        for region in request.regions:
            metrics = result.region_metrics(region)
            lo, hi = region.start - 1, region.end
            size = len(region)

            fully_open = 0
            partly_open = 0
            open_counts = [0] * size
            for mask in masks:
                window = mask[lo:hi]
                count = sum(window)
                open_counts = [c + int(v) for c, v in zip(open_counts, window)]
                if count == size:
                    fully_open += 1
                elif count >= PARTIAL_THRESHOLD * size:
                    partly_open += 1

            metrics.detail["state_populations"] = {
                "exposed": fully_open / drawn,
                "partly_exposed": partly_open / drawn,
                "buried": (drawn - fully_open - partly_open) / drawn,
            }
            metrics.set(
                M.MEAN_BASE_UNPAIRED, sum(open_counts) / (drawn * size)
            )

            if fully_open == 0:
                # Exact one-sided 95% binomial upper bound after zero hits.
                bound = 1.0 - 0.05 ** (1.0 / drawn)
                metrics.detail["p_unpaired_upper_bound"] = bound
                metrics.detail["sampling_limited"] = True
                result.warn(
                    f"region {region.label} was never fully unpaired in "
                    f"{drawn} samples; sampling can only bound its "
                    f"accessibility at < {bound:.2g}. A constrained "
                    f"partition-function calculation can resolve this event "
                    f"under its declared scope."
                )
            else:
                probability = fully_open / drawn
                metrics.set(M.P_UNPAIRED, probability)
                dg_open = thermo.dg_open_from_probability(probability, temperature)
                metrics.set(M.DG_OPEN, dg_open)
                metrics.set(
                    M.DG_OPEN_PER_NT,
                    thermo.dg_open_per_nucleotide(dg_open, size),
                )
                # Binomial standard error, the honest precision of the estimate.
                stderr = math.sqrt(probability * (1 - probability) / drawn)
                metrics.detail["p_unpaired_stderr"] = stderr
                metrics.detail["p_unpaired_interval_95"] = _wilson_interval(
                    fully_open, drawn
                )
                metrics.detail["sampling_limited"] = False

            seed = self._sample_seed(
                masks, region, request.seed_length, drawn,
                request.seed_starts(region),
            )
            if seed is not None:
                seed_start, seed_p, seed_trials = seed
                metrics.set(M.SEED_START, seed_start)
                metrics.set(M.SEED_LENGTH, request.seed_length)
                if seed_p is not None:
                    metrics.set(M.SEED_P_UNPAIRED, seed_p)
                else:
                    selected = next(
                        trial for trial in seed_trials
                        if trial["start"] == seed_start
                    )
                    metrics.detail["seed_p_unpaired_upper_bound"] = selected[
                        "p_unpaired_upper_bound"
                    ]
                    metrics.detail["seed_sampling_limited"] = True
                metrics.detail["seed_trials"] = seed_trials
                metrics.detail["seed_selection_note"] = (
                    "best empirical placement selected from the listed trials; "
                    "intervals are per placement and do not correct selection bias"
                )
        return result

    @staticmethod
    def _sample_seed(
        masks: list[list[bool]], region: Region, seed_length: int, drawn: int,
        allowed_starts: list[int],
    ) -> tuple[int, float | None, list[dict[str, object]]] | None:
        """Most frequently open seed placement across the sampled ensemble."""
        if seed_length > len(region) or not allowed_starts:
            return None
        best: tuple[int, int] | None = None
        trials: list[dict[str, object]] = []
        for start in allowed_starts:
            lo, hi = start - 1, start + seed_length - 1
            hits = sum(1 for mask in masks if all(mask[lo:hi]))
            probability = hits / drawn
            trial: dict[str, object] = {
                "start": start,
                "end": start + seed_length - 1,
                "hits": hits,
                "draws": drawn,
                "interval_95": _wilson_interval(hits, drawn),
            }
            if hits == 0:
                trial.update({
                    "p_unpaired": None,
                    "p_unpaired_upper_bound": 1.0 - 0.05 ** (1.0 / drawn),
                    "estimate_kind": "upper_bound",
                    "censor_reason": (
                        "no sampled structure contained this fully open seed"
                    ),
                })
            else:
                trial.update({
                    "p_unpaired": probability,
                    "estimate_kind": "point",
                })
            trials.append(trial)
            if best is None or hits > best[1]:
                best = (start, hits)
        if best is None:
            return None
        best_probability = best[1] / drawn if best[1] else None
        return best[0], best_probability, trials


def _wilson_interval(hits: int, draws: int, z: float = 1.959963984540054) -> tuple[float, float]:
    """Two-sided Wilson score interval for a binomial proportion."""
    if draws <= 0:
        raise ValueError("draws must be positive")
    p = hits / draws
    z2 = z * z
    denominator = 1.0 + z2 / draws
    center = (p + z2 / (2.0 * draws)) / denominator
    half = z * math.sqrt(
        p * (1.0 - p) / draws + z2 / (4.0 * draws * draws)
    ) / denominator
    return max(0.0, center - half), min(1.0, center + half)
