"""The adapter contract.

An *adapter* wraps one external tool or one internal calculation and reports
into the shared metric vocabulary. Adapters must be honest about two things:

1. :meth:`Adapter.availability` tells the driver whether the tool can run at
   all, so a missing binary degrades the report rather than crashing it.
2. A failing tool returns a ``failed`` :class:`ToolResult` carrying the error
   instead of raising, so one broken tool never costs you the rest of them.
"""

from __future__ import annotations

import traceback
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Sequence as TSequence

from ..core.model import ConditionSpec, ModelSettings, ProbingData, RecognitionSpec
from ..core.result import Availability, Tier, ToolResult, Timer
from ..core.sequence import Region, Sequence


@dataclass
class AccessibilityRequest:
    """Ask: how available is each of these regions on this one molecule?

    This is deliberately single-molecule: rnavail answers whether a region is
    unpaired within its own folded structure, not whether it binds some other
    RNA. That second question needs a partner-specific interaction model and
    is out of scope here.
    """

    sequence: Sequence
    regions: list[Region]
    settings: ModelSettings
    probing: ProbingData | None = None
    #: Length of the nucleation seed scanned inside each target region.
    seed_length: int = 10
    #: Flanking context folded around each region when an adapter needs to
    #: fold a window rather than the whole molecule.
    context_flank: int = 150
    options: dict[str, Any] = field(default_factory=dict)
    recognition: RecognitionSpec | None = None
    condition: ConditionSpec | None = None

    def __post_init__(self) -> None:
        if self.recognition is None:
            self.recognition = RecognitionSpec(seed_lengths=(self.seed_length,))
        if self.condition is None:
            self.condition = ConditionSpec(
                temperature_c=self.settings.temperature_c,
                sodium_molar=self.settings.salt_molar,
            )
        if self.recognition.seed_lengths != (self.seed_length,):
            raise ValueError(
                "this calculation supports one seed length; RecognitionSpec."
                "seed_lengths must equal (seed_length,)"
            )
        if abs(self.condition.temperature_c - self.settings.temperature_c) > 1e-9:
            raise ValueError(
                "ConditionSpec.temperature_c must match ModelSettings.temperature_c"
            )
        if self.condition.sodium_molar != self.settings.salt_molar:
            raise ValueError(
                "ConditionSpec.sodium_molar must match ModelSettings.salt_molar"
            )
        length = len(self.sequence)
        if self.probing is not None:
            if self.probing.sequence_hash and self.probing.sequence_hash != self.sequence.sha256:
                raise ValueError(
                    "probing track sequence_hash does not match the target sequence"
                )
            if (
                self.probing.condition_id != "unspecified"
                and self.condition.condition_id != "unspecified"
                and self.probing.condition_id != self.condition.condition_id
            ):
                raise ValueError(
                    "probing track condition_id must match the declared "
                    "ConditionSpec for a conditioned folding run"
                )
        for region in self.regions:
            if region.end > length:
                raise ValueError(
                    f"region {region.label} exceeds sequence "
                    f"{self.sequence.name!r} ({length} nt)"
                )
            # A fixed/listed placement is part of the requested event. Do not
            # run adapters and quietly omit the seed if a direct evaluation
            # names a footprint that contains none of its allowed placements.
            if self.recognition.requires_declared_seed and not self.seed_starts(region):
                raise ValueError(
                    f"{self.recognition.seed_mode} seed placement does not fit "
                    f"region {region.label} for seed length {self.seed_length}"
                )

    def seed_starts(self, region: Region) -> list[int]:
        """Allowed starts for the requested recognition mechanism."""
        return self.recognition.permitted_seed_starts(region, self.seed_length)


class Adapter(ABC):
    """Base class for every tool wrapper."""

    #: Short stable identifier used in reports and on the command line.
    name: str = ""
    #: Which pipeline stage this adapter belongs to.
    tier: Tier = Tier.ACCESSIBILITY
    #: One-line description shown by ``rnavail tools``.
    description: str = ""
    #: Metric keys this adapter can emit.
    provides: tuple[str, ...] = ()
    #: Rough cost class, used to order execution and to warn about big jobs.
    cost: int = 1
    #: Whether the adapter answers accessibility requests.
    handles_accessibility: bool = False
    #: Set for adapters whose numbers are model predictions of a physical
    #: quantity rather than partition-function thermodynamics.
    orthogonal: bool = False
    #: Tools that are the same calculation run two ways (the ViennaRNA
    #: Python bindings vs. the RNAplfold binary; RNAstructure's partition
    #: function under ProbKnot vs. under its own partition-function adapter)
    #: share a group name here. The consensus layer averages within a group
    #: before taking the cross-group median, so a validation pair counts as
    #: one independent measurement, not two. Empty means "its own group" —
    #: the common case, for a tool with no sibling.
    independence_group: str = ""
    #: What kind of number this adapter's per-base metrics are: a genuine
    #: Boltzmann/partition-function probability ("probability", the
    #: default), a Monte Carlo estimate of one ("monte_carlo_probability"),
    #: a trained model's posterior ("posterior", not a thermodynamic
    #: quantity), or one deterministic structure's binary paired/unpaired
    #: call ("single_structure"). The consensus layer only blends exact
    #: "probability" values into the primary statistic — other estimands are
    #: kept and shown, never silently dropped, but not averaged in as though
    #: they measured the same thing.
    estimand: str = "probability"
    #: Probing conversions this adapter applies to its calculations. An empty
    #: set means probing-conditioned and unconditioned results must not be
    #: blended when a track was supplied.
    probing_methods: frozenset[str] = frozenset()
    model_family: str = ""
    algorithm: str = ""
    applied_setting_names: frozenset[str] = frozenset()
    #: Requested settings that are intentionally irrelevant to this adapter's
    #: estimand. This is distinct from an unsupported setting: a local span
    #: has no bearing on a whole-sequence fold, whereas an omitted salt
    #: correction is a material protocol mismatch.
    ignored_setting_names: frozenset[str] = frozenset()
    #: True for sequence-only diagnostics that remain meaningful regardless
    #: of a supplied structure-probing track.
    probing_irrelevant: bool = False

    def availability(self) -> Availability:
        """Report whether this adapter can run in the current environment."""
        return Availability.yes()

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        raise NotImplementedError

    # -- the driver calls this -----------------------------------------------

    def new_result(self, settings: ModelSettings | None = None) -> ToolResult:
        result = ToolResult(
            tool=self.name,
            tier=self.tier,
            version=self.availability().version,
            settings=settings.to_dict() if settings else {},
            independence_group=self.independence_group or self.name,
            estimand=self.estimand,
            model_family=self.model_family or self.name,
            algorithm=self.algorithm or self.name,
        )
        if settings is not None:
            requested = settings.to_dict()
            defaults = ModelSettings().to_dict()
            applied = {
                key: value for key, value in requested.items()
                if key in self.applied_setting_names
            }
            unsupported = {
                key: "adapter does not declare support for this setting"
                for key, value in requested.items()
                if key not in self.applied_setting_names
                and key not in self.ignored_setting_names
                and value != defaults[key]
            }
            ignored = {
                key: "not material for this adapter's declared calculation"
                for key, value in requested.items()
                if key not in self.applied_setting_names
                and (key in self.ignored_setting_names or value == defaults[key])
            }
            result.applied_protocol = {
                "requested": requested,
                "applied": applied,
                "unsupported": unsupported,
                "ignored_by_design": ignored,
                "compatible_with_requested": not unsupported,
            }
        return result

    def _annotate_request(
        self, result: ToolResult, request: AccessibilityRequest
    ) -> None:
        probing = request.probing
        if probing is None:
            result.conditioning = {
                "status": "not_requested",
                "conditioning_id": "unconditioned",
            }
            return
        if self.probing_irrelevant:
            result.conditioning = {
                "status": "not_applicable",
                "conditioning_id": "not_applicable",
                "requested_method": probing.method,
            }
            return
        supported = probing.method in self.probing_methods
        identity_status = "verified" if probing.sequence_hash else "unverified"
        result.conditioning = {
            "status": "applied" if supported else "unsupported",
            "conditioning_id": (
                probing.conditioning_id() if supported else "unconditioned"
            ),
            "requested_method": probing.method,
            "sequence_identity": identity_status,
        }
        if not probing.sequence_hash:
            result.warn(
                "probing track has no sequence hash; target identity is "
                "unverified for this API-supplied track"
            )
        if not supported:
            result.warn(
                f"{self.name} does not apply {probing.method} probing; its "
                "outputs are diagnostic only and excluded from conditioned "
                "consensus"
            )

    def run_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        """Run the accessibility calculation, converting failure into a result."""
        result = self.new_result(request.settings)
        self._annotate_request(result, request)
        if not self.handles_accessibility:
            result.status = "skipped"
            result.error = f"{self.name} does not answer accessibility requests"
            return result

        status = self.availability()
        if not status.available:
            result.status = "skipped"
            result.error = status.reason
            if status.hint:
                result.warn(status.hint)
            return result

        try:
            with Timer(result):
                produced = self.compute_accessibility(request)
        except Exception as exc:                    # noqa: BLE001 - deliberate
            result.status = "failed"
            result.error = f"{type(exc).__name__}: {exc}"
            result.detail["traceback"] = traceback.format_exc(limit=6)
            return result

        if produced is not None:
            produced.runtime_s = result.runtime_s
            if not produced.version:
                produced.version = status.version
            if not produced.settings:
                produced.settings = request.settings.to_dict()
            self._annotate_request(produced, request)
            return produced
        return result


class AccessibilityAdapter(Adapter):
    handles_accessibility = True
