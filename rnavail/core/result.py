"""Result containers and the canonical metric vocabulary.

Every adapter, whatever it wraps, reports into the same small namespace of
metric names defined in :class:`M`. That is what lets the aggregation layer
compare RNAplfold against RNAstructure against CONTRAfold without
special-casing each tool.

Every metric here describes one molecule folded on itself. None of them
predict binding to another RNA — that is a different, harder question this
tool does not try to answer.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable, Literal

from .sequence import Region


class Tier(str, Enum):
    """Pipeline stages, ordered by increasing computational cost.

    The ordering is what the driver uses to decide what to run first and
    what to reserve for candidates that survive earlier filters.
    """

    ACCESSIBILITY = "accessibility"      # RNAplfold, exact dG_open, sampling
    STRUCTURE = "structure"              # global folds, orthogonal models

    @property
    def order(self) -> int:
        return _TIER_ORDER[self]


_TIER_ORDER = {
    Tier.ACCESSIBILITY: 0,
    Tier.STRUCTURE: 1,
}


class M:
    """Canonical metric keys.

    Sign convention: for every key listed in :data:`HIGHER_IS_BETTER` a larger
    value means a *more* available / better target. Energies are the obvious
    exception and are listed in :data:`LOWER_IS_BETTER`.
    """

    # --- joint accessibility of the full target interval -------------------
    P_UNPAIRED = "p_unpaired"
    DG_OPEN = "dg_open"
    DG_OPEN_PER_NT = "dg_open_per_nt"

    # --- nucleation seed ---------------------------------------------------
    SEED_P_UNPAIRED = "seed_p_unpaired"
    SEED_DG_OPEN = "seed_dg_open"
    SEED_START = "seed_start"
    SEED_LENGTH = "seed_length"

    # --- per-base descriptors (diagnostic, never a substitute for the joint)
    MEAN_BASE_UNPAIRED = "mean_base_unpaired"
    MIN_BASE_UNPAIRED = "min_base_unpaired"
    PAIRED_FRACTION = "paired_fraction"
    SHANNON_ENTROPY = "shannon_entropy"

    # --- global structure --------------------------------------------------
    MFE = "mfe"
    ENSEMBLE_FREE_ENERGY = "ensemble_free_energy"
    MFE_ENSEMBLE_GAP = "mfe_ensemble_gap"
    MEAN_BP_DISTANCE = "mean_bp_distance"

    # --- robustness across model settings ---------------------------------
    DG_OPEN_SPREAD = "dg_open_spread"
    RANK_STABILITY = "rank_stability"

    # --- robustness across the sequence itself ------------------------------
    # These vary the input, not the model: does a natural point mutation or a
    # different choice of flanking context change the answer.
    RIBOSNITCH_SPREAD = "ribosnitch_spread"
    CONTEXT_DG_SPREAD = "context_dg_spread"

    # --- structure beyond nested secondary structure ------------------------
    GQUAD_SCORE = "gquad_score"
    PSEUDOKNOT_PAIRED_FRACTION = "pseudoknot_paired_fraction"

    # --- kinetics: does equilibrium ever get reached ------------------------
    CO_TX_TRAP_LENGTH = "co_tx_trap_length"

    # --- robustness across window length, and windowed-vs-exact agreement --
    # Sibling of DG_OPEN_SPREAD: that one perturbs the folding model, this one
    # perturbs the candidate's own length. WINDOW_EXACT_GAP is diagnostic only
    # (its sign carries information a desirability curve would throw away);
    # WINDOW_LENGTH_SPREAD is scored the same way DG_OPEN_SPREAD is.
    WINDOW_LENGTH_SPREAD = "window_length_spread"
    WINDOW_EXACT_GAP = "window_exact_gap"


#: Metrics where a larger number means a better / more available target.
HIGHER_IS_BETTER = frozenset({
    M.P_UNPAIRED, M.SEED_P_UNPAIRED, M.MEAN_BASE_UNPAIRED, M.MIN_BASE_UNPAIRED,
    M.SHANNON_ENTROPY, M.RANK_STABILITY,
})

#: Metrics where a smaller (or more negative) number is better.
LOWER_IS_BETTER = frozenset({
    M.DG_OPEN, M.DG_OPEN_PER_NT, M.SEED_DG_OPEN, M.PAIRED_FRACTION,
    M.DG_OPEN_SPREAD, M.RIBOSNITCH_SPREAD, M.CONTEXT_DG_SPREAD,
    M.PSEUDOKNOT_PAIRED_FRACTION, M.WINDOW_LENGTH_SPREAD,
})

#: Human-readable units, used by the report writers.
UNITS = {
    M.DG_OPEN: "kcal/mol", M.DG_OPEN_PER_NT: "kcal/mol/nt",
    M.SEED_DG_OPEN: "kcal/mol", M.MFE: "kcal/mol",
    M.ENSEMBLE_FREE_ENERGY: "kcal/mol", M.MFE_ENSEMBLE_GAP: "kcal/mol",
    M.DG_OPEN_SPREAD: "kcal/mol", M.SHANNON_ENTROPY: "bits/nt",
    M.RIBOSNITCH_SPREAD: "kcal/mol", M.CONTEXT_DG_SPREAD: "kcal/mol",
    M.CO_TX_TRAP_LENGTH: "nt", M.WINDOW_LENGTH_SPREAD: "kcal/mol/nt",
    M.WINDOW_EXACT_GAP: "kcal/mol",
}

Status = Literal["ok", "skipped", "failed"]


@dataclass(frozen=True)
class OpeningObservation:
    """One coherent interval-opening estimate from one protocol.

    Probability, energy, temperature, interval, seed and conditioning remain
    attached so aggregation cannot create a physically impossible hybrid from
    medians of unrelated fields.
    """

    observation_id: str
    tool: str
    interval: Region
    p_unpaired: float | None
    dg_open_kcal_mol: float | None
    temperature_c: float
    event: str
    model_family: str
    algorithm: str
    sequence_scope: str
    conditioning_id: str
    estimate_kind: Literal[
        "point", "upper_bound", "lower_bound", "interval", "censored"
    ]
    p_lower_bound: float | None = None
    p_upper_bound: float | None = None
    seed_start: int | None = None
    seed_length: int | None = None
    seed_p_unpaired: float | None = None
    seed_dg_open_kcal_mol: float | None = None
    censor_reason: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "observation_id": self.observation_id,
            "tool": self.tool,
            "interval": {
                "start": self.interval.start,
                "end": self.interval.end,
            },
            "p_unpaired": self.p_unpaired,
            "dg_open_kcal_mol": self.dg_open_kcal_mol,
            "temperature_c": self.temperature_c,
            "event": self.event,
            "model_family": self.model_family,
            "algorithm": self.algorithm,
            "sequence_scope": self.sequence_scope,
            "conditioning_id": self.conditioning_id,
            "estimate_kind": self.estimate_kind,
            "p_lower_bound": self.p_lower_bound,
            "p_upper_bound": self.p_upper_bound,
            "seed": (
                {
                    "start": self.seed_start,
                    "length": self.seed_length,
                    "p_unpaired": self.seed_p_unpaired,
                    "dg_open_kcal_mol": self.seed_dg_open_kcal_mol,
                }
                if self.seed_start is not None else None
            ),
            "censor_reason": self.censor_reason,
        }


@dataclass
class RegionMetrics:
    """Metrics one tool produced for one region."""

    region: Region
    values: dict[str, float] = field(default_factory=dict)
    detail: dict[str, Any] = field(default_factory=dict)

    def set(self, key: str, value: float | None) -> None:
        """Record a finite metric and preserve why a nonfinite value was omitted."""
        if value is None:
            return
        value = float(value)
        if math.isfinite(value):
            self.values[key] = value
        else:
            status = "nan" if math.isnan(value) else (
                "positive_infinity" if value > 0 else "negative_infinity"
            )
            self.detail.setdefault("numerical_status", {})[key] = status

    def get(self, key: str, default: float | None = None) -> float | None:
        return self.values.get(key, default)

    @property
    def key(self) -> str:
        return f"{self.region.start}-{self.region.end}"


@dataclass
class ToolResult:
    """Everything one adapter produced in one invocation.

    ``independence_group`` and ``estimand`` exist so the consensus layer can
    distinguish separately declared calculation groups from two views of the same
    calculation. Two tools sharing a group (e.g. the ViennaRNA bindings and
    the stock RNAplfold binary, which the test suite asserts agree to
    0.01 kcal/mol) are not two votes; they're one measurement checked twice.
    ``estimand`` says what *kind* of number a per-base metric is — a
    Boltzmann probability, a learned model's posterior, or a single
    deterministic structure — since a median across those three is not
    combining like with like.
    """

    tool: str
    tier: Tier
    status: Status = "ok"
    version: str = ""
    regions: dict[str, RegionMetrics] = field(default_factory=dict)
    globals: dict[str, float] = field(default_factory=dict)
    detail: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    error: str = ""
    runtime_s: float = 0.0
    settings: dict[str, Any] = field(default_factory=dict)
    independence_group: str = ""
    estimand: str = "probability"
    model_family: str = ""
    algorithm: str = ""
    conditioning: dict[str, Any] = field(default_factory=dict)
    applied_protocol: dict[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return self.status == "ok"

    def region_metrics(self, region: Region) -> RegionMetrics:
        """Fetch or create the metrics record for ``region``."""
        key = f"{region.start}-{region.end}"
        if key not in self.regions:
            self.regions[key] = RegionMetrics(region=region)
        return self.regions[key]

    def warn(self, message: str) -> None:
        if message not in self.warnings:
            self.warnings.append(message)

    def to_dict(self) -> dict[str, Any]:
        return {
            "tool": self.tool,
            "tier": self.tier.value,
            "status": self.status,
            "version": self.version,
            "runtime_s": round(self.runtime_s, 4),
            "independence_group": self.independence_group,
            "estimand": self.estimand,
            "model_family": self.model_family,
            "algorithm": self.algorithm,
            "conditioning": self.conditioning,
            "applied_protocol": self.applied_protocol,
            "globals": self.globals,
            "regions": {
                key: {
                    "start": rm.region.start,
                    "end": rm.region.end,
                    "name": rm.region.name,
                    "values": rm.values,
                    "detail": rm.detail,
                }
                for key, rm in self.regions.items()
            },
            "detail": self.detail,
            "warnings": self.warnings,
            "error": self.error,
            "settings": self.settings,
        }


@dataclass
class Availability:
    """Whether an adapter can run here, and why not if it cannot."""

    available: bool
    version: str = ""
    reason: str = ""
    hint: str = ""

    @classmethod
    def yes(cls, version: str = "") -> "Availability":
        return cls(available=True, version=version)

    @classmethod
    def no(cls, reason: str, hint: str = "") -> "Availability":
        return cls(available=False, reason=reason, hint=hint)


class Timer:
    """Context manager recording wall-clock runtime into a ToolResult."""

    def __init__(self, result: ToolResult) -> None:
        self.result = result

    def __enter__(self) -> "Timer":
        self._t0 = time.perf_counter()
        return self

    def __exit__(self, *exc: Any) -> Literal[False]:
        self.result.runtime_s = time.perf_counter() - self._t0
        return False
