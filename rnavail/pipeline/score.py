"""Consensus across tools, and the composite availability score.

Two separate jobs live here, and keeping them separate matters.

**Consensus** merges the same metric reported by different tools into a
median, a spread and a count. The spread is the useful part: when RNAplfold,
the exact partition function and RNAstructure agree on a site, its ranking is
solid; when they disagree by kcal/mol, the site is model-dependent and the
report says so instead of averaging the disagreement away.

**Scoring** turns the raw physics into one number for ranking. It does this in
two stages. Each metric is first mapped through a *desirability* function onto
[0, 1] using absolute anchors, not z-scores, so a candidate's score does not
change when you add or remove other candidates from the run. Those
desirabilities are then combined as a **weighted geometric mean**, which is
conjunctive rather than additive: a region needs a low per-nucleotide opening
cost, an accessible nucleation seed, and a stable answer across perturbed
folding parameters all at once to score well. A region that looks cheap to
open on average but whose number swings by kcal/mol under a different
dangling-end model is not a trustworthy candidate, and a geometric mean says
so, while an arithmetic mean would let one strong number paper over a shaky
one.

Weights are defaults, not truths. The source document is explicit that they
should be fit against measured gate performance, and :func:`load_weights`
exists so that fitting them does not require touching this file.
"""

from __future__ import annotations

import json
import math
import statistics
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence as TSequence

from ..core.result import HIGHER_IS_BETTER, LOWER_IS_BETTER, M, ToolResult
from ..core.sequence import Region


@dataclass
class Consensus:
    """One metric as reported by every tool that produced it.

    The median and spread are not a plain average over ``values``. Two
    corrections happen first, because "every tool that reported it" is not
    the same thing as "every independent measurement of it":

    1. **De-duplication.** Tools sharing an ``independence_group`` (the
       ViennaRNA bindings and the RNAplfold binary; ProbKnot and
       RNAstructure's own partition-function adapter) are the same
       calculation checked twice, not two votes. They are averaged together
       into one value per group before the cross-group median is taken, so a
       validation pair can never outvote a third separately declared
       calculation group.
    2. **Estimand gating.** For metrics multiple *kinds* of tool report — a
       Boltzmann probability, a learned model's posterior, one deterministic
       structure's binary call — only the probability-estimand tools feed
       the primary median. The rest are not dropped; they stay in
       ``values``/``by_tool`` for full transparency, and ``excluded`` names
       which ones and why.

    ``values``, keyed by raw tool name, always holds everything every
    successful tool reported — including values withheld from the primary
    statistic for an incompatible probing condition or protocol.  The
    explicit ``eligible_tools`` and ``primary_tools`` views make the two
    questions separable:

    * *What did every tool report?* — ``values``.
    * *What can answer the requested experimental/model protocol?* —
      ``eligible_tools``.
    * *What compatible values can be pooled as the same estimand?* —
      ``primary_tools``.

    This distinction is important when no compatible value exists.  In that
    case the raw diagnostic is still serialized, but ``median`` and
    ``spread`` are ``None``; the fallback for non-probability estimands must
    never turn an incompatible value into a primary estimate.
    """

    metric: str
    values: dict[str, float] = field(default_factory=dict)
    #: tool name -> independence group (defaults to the tool's own name).
    groups: dict[str, str] = field(default_factory=dict)
    #: tool name -> estimand ("probability", "posterior", "single_structure").
    estimands: dict[str, str] = field(default_factory=dict)
    excluded_conditioning: dict[str, str] = field(default_factory=dict)
    #: Tool -> material settings the adapter could not apply. The raw tool
    #: result remains available, but no value under a different protocol may
    #: be pooled with compatible estimates or used as an estimand fallback.
    excluded_protocol: dict[str, dict[str, str]] = field(default_factory=dict)

    @property
    def eligible_tools(self) -> list[str]:
        """Raw tools compatible with the requested conditioning and protocol.

        Estimand is deliberately *not* considered here.  A compatible
        posterior or single-structure call remains eligible evidence to show,
        even though it will normally be excluded from a probability median.
        """
        return [
            tool for tool in self.values
            if tool not in self.excluded_conditioning
            and tool not in self.excluded_protocol
        ]

    @property
    def primary_tools(self) -> list[str]:
        """Compatible tools whose values can enter the primary statistic.

        Compatible probability-estimand values take precedence.  If there
        are no such values, the fallback is restricted to *compatible* raw
        values; if none are compatible, there is deliberately no fallback.
        """
        eligible = self.eligible_tools
        probability = [
            tool for tool in eligible
            if self.estimands.get(tool, "probability") == "probability"
        ]
        return probability or eligible

    @property
    def eligible_values(self) -> dict[str, float]:
        """Compatible raw values, before probability-estimand gating."""
        return {tool: self.values[tool] for tool in self.eligible_tools}

    @property
    def primary_values(self) -> dict[str, float]:
        """Values that can contribute to the median or its fallback."""
        return {tool: self.values[tool] for tool in self.primary_tools}

    # Kept private for callers written before the public primary view was
    # added.  Internal aggregation should use the same eligibility rules.
    def _primary_tools(self) -> list[str]:
        return self.primary_tools

    @property
    def excluded(self) -> dict[str, str]:
        """tool -> estimand, for tools reported but not in the primary set."""
        primary = set(self.primary_tools)
        return {
            tool: self.estimands.get(tool, "probability")
            for tool in self.eligible_tools if tool not in primary
        }

    def _grouped_values(self) -> dict[str, float]:
        """One value per independence group, averaged within the group."""
        buckets: dict[str, list[float]] = {}
        for tool in self._primary_tools():
            group = self.groups.get(tool) or tool
            buckets.setdefault(group, []).append(self.values[tool])
        return {group: statistics.mean(vals) for group, vals in buckets.items()}

    @property
    def n(self) -> int:
        """Raw count of tools that reported this metric, duplicates included."""
        return len(self.values)

    @property
    def n_eligible(self) -> int:
        """Compatible raw-tool count before estimand gating."""
        return len(self.eligible_tools)

    @property
    def n_primary(self) -> int:
        """Raw-tool count behind the median or compatible fallback."""
        return len(self.primary_tools)

    @property
    def n_independent(self) -> int:
        """Count of distinct independence groups behind the primary median."""
        return len(self._grouped_values())

    @property
    def median(self) -> float | None:
        grouped = self._grouped_values()
        return statistics.median(grouped.values()) if grouped else None

    @property
    def spread(self) -> float | None:
        """Max minus min across independent groups, not raw tools.

        Zero with a single independent group (``n_independent`` disambiguates
        that from "nobody reported this").
        """
        grouped = self._grouped_values()
        if len(grouped) < 2:
            return 0.0 if grouped else None
        return max(grouped.values()) - min(grouped.values())

    @property
    def disagreement(self) -> float | None:
        """Spread relative to the magnitude of the value, for cross-metric use."""
        median = self.median
        if median is None or self.n_independent < 2:
            return None
        scale = max(abs(median), 1e-6)
        return self.spread / scale

    def to_dict(self) -> dict[str, Any]:
        return {
            "metric": self.metric,
            "n_tools": self.n,
            "n_eligible": self.n_eligible,
            "n_primary": self.n_primary,
            "n_independent": self.n_independent,
            "median": self.median,
            "spread": self.spread,
            "by_tool": dict(self.values),
            "groups": dict(self.groups),
            "eligible_for_primary": self.eligible_tools,
            "primary_for_median": self.primary_tools,
            "excluded_from_median": self.excluded,
            "excluded_for_conditioning": self.excluded_conditioning,
            "excluded_for_protocol": self.excluded_protocol,
        }


def build_consensus(
    results: TSequence[ToolResult], region: Region,
    conditioning_id: str | None = None,
) -> dict[str, Consensus]:
    """Collect every metric reported for ``region`` across all tools."""
    key = f"{region.start}-{region.end}"
    merged: dict[str, Consensus] = {}
    for result in results:
        if not result.ok:
            continue
        status = result.conditioning.get("status")
        metrics = result.regions.get(key)
        if metrics is None:
            continue
        group = result.independence_group or result.tool
        result_conditioning = result.conditioning.get(
            "conditioning_id", "unconditioned"
        )
        conditioning_exclusion: str | None = None
        if status == "unsupported":
            requested_method = result.conditioning.get("requested_method")
            method_text = (
                f" ({requested_method})" if requested_method else ""
            )
            conditioning_exclusion = (
                f"adapter did not apply requested conditioning{method_text}; "
                f"reported {result_conditioning}"
            )
        elif (
            conditioning_id is not None
            and status == "applied"
            and result_conditioning != conditioning_id
        ):
            conditioning_exclusion = (
                f"reported {result_conditioning}; requested {conditioning_id}"
            )
        elif (
            conditioning_id is not None
            and conditioning_id != "unconditioned"
            and status not in {"applied", "not_applicable"}
        ):
            # A caller supplying an explicit conditioning ID is asking for a
            # particular experimental state.  An unannotated or
            # unconditioned result cannot become a primary fallback merely
            # because it happened to report the same metric.
            conditioning_exclusion = (
                f"conditioning status {status or 'missing'}; "
                f"requested {conditioning_id}"
            )
        unsupported = result.applied_protocol.get("unsupported", {}) or {}
        for name, value in metrics.values.items():
            consensus = merged.setdefault(name, Consensus(metric=name))
            consensus.values[result.tool] = value
            consensus.groups[result.tool] = group
            consensus.estimands[result.tool] = result.estimand
            if conditioning_exclusion is not None:
                consensus.excluded_conditioning[result.tool] = conditioning_exclusion
            if unsupported:
                consensus.excluded_protocol[result.tool] = dict(unsupported)
    return merged


# --------------------------------------------------------------------------
# Desirability transforms
# --------------------------------------------------------------------------

def _ramp(value: float, bad: float, good: float) -> float:
    """Linear ramp from 0 at ``bad`` to 1 at ``good``, clamped outside.

    Works in either direction: ``good`` may be less than ``bad`` for metrics
    where smaller is better.
    """
    if bad == good:
        return 1.0 if value == good else 0.0
    fraction = (value - bad) / (good - bad)
    return max(0.0, min(1.0, fraction))


def _log_ramp(value: float, bad: float, good: float) -> float:
    """Ramp on a log scale, for probabilities spanning many decades."""
    floor = 1e-12
    return _ramp(
        math.log10(max(value, floor)),
        math.log10(max(bad, floor)),
        math.log10(max(good, floor)),
    )


@dataclass(frozen=True)
class Criterion:
    """One scored feature: where to find it, how to judge it, how much it counts."""

    key: str
    weight: float
    desirability: Callable[[float], float]
    label: str
    #: A criterion marked essential contributes a hard zero when it is absent
    #: rather than being silently dropped from the geometric mean.
    essential: bool = False
    rationale: str = ""


#: Default criteria. Anchors follow the development heuristics in the source
#: document; every one of them is a starting point to be recalibrated.
DEFAULT_CRITERIA: tuple[Criterion, ...] = (
    Criterion(
        key=M.SEED_P_UNPAIRED, weight=2.0,
        desirability=lambda v: _log_ramp(v, bad=1e-4, good=0.5),
        label="seed accessibility",
        rationale=(
            "recognition has to start somewhere; a nucleation site that is "
            "open one time in ten thousand will not initiate"
        ),
    ),
    Criterion(
        key=M.DG_OPEN_PER_NT, weight=1.5,
        desirability=lambda v: _ramp(v, bad=1.0, good=0.05),
        label="opening cost per nucleotide",
        rationale=(
            "length-normalised so that a long target is not penalised merely "
            "for being long"
        ),
    ),
    Criterion(
        key=M.DG_OPEN_SPREAD, weight=0.75,
        desirability=lambda v: _ramp(v, bad=4.0, good=0.5),
        label="robustness across model settings",
        rationale=(
            "a site whose opening cost swings by kcal/mol when the folding "
            "parameters are perturbed is not a site you can rank confidently"
        ),
    ),
    Criterion(
        key=M.WINDOW_LENGTH_SPREAD, weight=0.75,
        desirability=lambda v: _ramp(v, bad=0.15, good=0.01),
        label="robustness across window length",
        rationale=(
            "the window length is a design choice, not a physical constant; "
            "opening cost per nucleotide is not even monotonic in length "
            "(it tracks which helices the boundary falls across, a step "
            "function, not a smooth trend), so a site whose per-nt cost only "
            "looks good at one specific length is a narrower bet than one "
            "that holds up across nearby lengths. Present only when "
            "--length-robustness ran, exactly like the model-settings sweep "
            "above; absent otherwise, dropped from the mean rather than "
            "scored as zero"
        ),
    ),
)


@dataclass
class ScoreComponent:
    criterion: Criterion
    value: float | None
    desirability: float | None
    present: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "metric": self.criterion.key,
            "label": self.criterion.label,
            "weight": self.criterion.weight,
            "value": self.value,
            "desirability": self.desirability,
            "present": self.present,
        }


@dataclass
class Score:
    """A composite availability score with its full derivation attached."""

    value: float
    components: list[ScoreComponent]
    coverage: float
    missing: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "heuristic_rank_score": self.value,
            "score": self.value,
            "coverage": self.coverage,
            "missing_metrics": self.missing,
            "components": [c.to_dict() for c in self.components],
        }


def score_candidate(
    metrics: dict[str, float],
    criteria: TSequence[Criterion] = DEFAULT_CRITERIA,
) -> Score:
    """Combine available metrics into a weighted geometric mean on [0, 1].

    Criteria whose metric is missing are dropped from the mean rather than
    scored as zero, so a candidate is never punished for a tool that was not
    run. The ``coverage`` field reports what fraction of the intended weight
    was actually available, and a score computed from thin coverage should be
    read as provisional. The exception is criteria marked ``essential``, which
    do count as zero when absent.
    """
    for criterion in criteria:
        if not math.isfinite(criterion.weight) or criterion.weight < 0.0:
            raise ValueError(
                f"criterion {criterion.key!r} has an invalid weight; weights "
                "must be finite and non-negative"
            )
    if criteria and not any(criterion.weight > 0.0 for criterion in criteria):
        raise ValueError("at least one scoring weight must be positive")

    components: list[ScoreComponent] = []
    log_sum = 0.0
    weight_sum = 0.0
    available_weight = 0.0
    total_weight = 0.0
    missing: list[str] = []

    for criterion in criteria:
        total_weight += criterion.weight
        value = metrics.get(criterion.key)
        if value is None or not math.isfinite(value):
            components.append(ScoreComponent(criterion, None, None, False))
            missing.append(criterion.key)
            if criterion.essential:
                weight_sum += criterion.weight
                log_sum += criterion.weight * math.log(1e-6)
            continue

        desirability = max(1e-6, min(1.0, criterion.desirability(value)))
        components.append(ScoreComponent(criterion, value, desirability, True))
        log_sum += criterion.weight * math.log(desirability)
        weight_sum += criterion.weight
        available_weight += criterion.weight

    if weight_sum == 0.0:
        return Score(0.0, components, 0.0, missing)

    value = math.exp(log_sum / weight_sum)
    coverage = available_weight / total_weight if total_weight else 0.0
    return Score(value, components, coverage, missing)


def flatten_metrics(
    consensus: dict[str, Consensus], extra: dict[str, float] | None = None
) -> dict[str, float]:
    """Reduce a consensus map to one representative value per metric.

    The median is used rather than the mean because a single tool reporting a
    wildly different number, which does happen when one of them is
    misconfigured, should not drag the consensus with it.
    """
    flat = {
        name: agreement.median
        for name, agreement in consensus.items()
        if agreement.median is not None
    }
    if extra:
        flat.update(extra)
    return flat


def load_weights(path: str | Path) -> tuple[Criterion, ...]:
    """Override the default criterion weights from a JSON file.

    The file maps metric names to weights, e.g. ``{"dg_total": 3.0}``. Only
    weights are configurable this way; the desirability anchors are code
    because changing them changes what the score means.
    """
    overrides = json.loads(Path(path).read_text())
    if not isinstance(overrides, dict):
        raise ValueError("weight file must contain a JSON object")

    unknown = set(overrides) - {c.key for c in DEFAULT_CRITERIA}
    if unknown:
        raise ValueError(
            f"weight file names unknown metrics: {', '.join(sorted(unknown))}"
        )

    resolved: dict[str, float] = {}
    for key, value in overrides.items():
        try:
            weight = float(value)
        except (TypeError, ValueError):
            raise ValueError(
                f"weight for {key!r} must be a finite non-negative number"
            ) from None
        if not math.isfinite(weight) or weight < 0.0:
            raise ValueError(
                f"weight for {key!r} must be a finite non-negative number"
            )
        resolved[key] = weight

    from dataclasses import replace
    criteria = tuple(
        replace(c, weight=resolved[c.key]) if c.key in resolved else c
        for c in DEFAULT_CRITERIA
    )
    if not any(criterion.weight > 0.0 for criterion in criteria):
        raise ValueError("at least one scoring weight must be positive")
    return criteria


def rank_stability(rankings: TSequence[TSequence[str]]) -> dict[str, float]:
    """How consistently each candidate ranks across repeated evaluations.

    Given one ordering of candidate keys per model variant or replicate,
    returns a 0-1 stability per candidate: 1 means it held the same rank every
    time, lower means its position moved. This is what flags a candidate whose
    apparent quality is an artefact of one particular parameter choice.
    """
    if not rankings:
        return {}
    positions: dict[str, list[int]] = {}
    for ordering in rankings:
        for index, key in enumerate(ordering):
            positions.setdefault(key, []).append(index)

    n = max(len(o) for o in rankings)
    stability: dict[str, float] = {}
    for key, ranks in positions.items():
        if len(ranks) < 2 or n < 2:
            stability[key] = 1.0
            continue
        # Normalise the standard deviation of rank by the worst case, which is
        # roughly half the list length for a candidate bouncing end to end.
        spread = statistics.pstdev(ranks) / (n / 2.0)
        stability[key] = max(0.0, min(1.0, 1.0 - spread))
    return stability
