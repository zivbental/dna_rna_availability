"""The two drivers: scan a transcript, or evaluate named regions in depth.

Both funnel into the same report structure, and both obey the cost hierarchy
the source document argues for: cheap tools look at everything, expensive
tools look only at what survived. The difference is only where they start.

Both answer a single-molecule question — is this region unpaired within its
own folded structure — using every applicable tool. Neither predicts binding
to another RNA; that is a different, harder question this tool does not try
to answer.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Sequence as TSequence

from ..adapters.base import AccessibilityRequest, Adapter
from ..adapters.registry import DEFAULT_MAX_COST, select
from ..core.model import (
    ConditionSpec, ModelSettings, ProbingData, RecognitionSpec,
)
from ..core.evidence import EvidenceTrack
from ..core.result import M, OpeningObservation, Tier, ToolResult
from ..core import thermo
from ..core.sequence import Region, Sequence, tile_regions
from .score import (
    Consensus, Criterion, DEFAULT_CRITERIA, Score, build_consensus,
    flatten_metrics, rank_stability, score_candidate,
)

ProgressFn = Callable[[str], None]


# A seed coordinate and its opening probability are meaningful only for a
# declared complementary-strand recognition mechanism.  Keep the complete set
# together so a custom score cannot accidentally reintroduce a seed-derived
# term for a protein or small-molecule binder.
_SEED_NUCLEATION_METRICS = frozenset({
    M.SEED_P_UNPAIRED,
    M.SEED_DG_OPEN,
    M.SEED_START,
    M.SEED_LENGTH,
})


def _noop(message: str) -> None:
    pass


def _validate_condition(settings: ModelSettings, condition: ConditionSpec) -> None:
    """Prevent reports from claiming conditions different from the fold."""
    if abs(condition.temperature_c - settings.temperature_c) > 1e-9:
        raise ValueError(
            "ConditionSpec.temperature_c must match ModelSettings.temperature_c; "
            "one run cannot report a different temperature from the folding model"
        )
    if condition.sodium_molar != settings.salt_molar:
        raise ValueError(
            "ConditionSpec.sodium_molar must match ModelSettings.salt_molar; "
            "one run cannot report a different monovalent salt setting from "
            "the folding model"
        )


@dataclass
class CandidateReport:
    """Everything known about one region, and what it scored."""

    region: Region
    subsequence: str
    consensus: dict[str, Consensus] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)
    score: Score | None = None
    notes: list[str] = field(default_factory=list)
    detail: dict[str, Any] = field(default_factory=dict)
    opening_observations: list[OpeningObservation] = field(default_factory=list)
    primary_opening_observation_id: str | None = None
    #: Overlapping condition-linked observations. These are deliberately
    #: preserved as annotations, not converted into an unvalidated score.
    biological_evidence: list[dict[str, Any]] = field(default_factory=list)

    @property
    def key(self) -> str:
        return f"{self.region.start}-{self.region.end}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "region": {
                "start": self.region.start,
                "end": self.region.end,
                "length": len(self.region),
                "name": self.region.name,
            },
            "subsequence": self.subsequence,
            "metrics": self.metrics,
            "consensus": {k: v.to_dict() for k, v in self.consensus.items()},
            "score": self.score.to_dict() if self.score else None,
            "heuristic_rank_score": self.score.value if self.score else None,
            "notes": self.notes,
            "detail": self.detail,
            "primary_opening_observation_id": self.primary_opening_observation_id,
            "opening_observations": [
                observation.to_dict() for observation in self.opening_observations
            ],
            "biological_evidence": self.biological_evidence,
        }


@dataclass
class Report:
    """The output of a scan or an evaluation."""

    sequence: Sequence
    settings: ModelSettings
    mode: str
    recognition: RecognitionSpec | None = None
    condition: ConditionSpec | None = None
    probing: ProbingData | None = None
    candidates: list[CandidateReport] = field(default_factory=list)
    tool_results: list[ToolResult] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    detail: dict[str, Any] = field(default_factory=dict)
    #: RNAplfold's raw (position -> [p_unpaired for length 1, 2, ...]) table,
    #: set by ``scan``. Deliberately not part of ``to_dict()``/JSON — it is
    #: the source for the accessibility-profile and (position, length)
    #: landscape plots, kept in memory only so the HTML renderer can draw
    #: them from what was already computed instead of re-folding a third
    #: time. ``detail["profile"]`` carries the one-length slice of it that is
    #: worth persisting as numbers.
    profile_table: dict[int, list[float | None]] | None = None
    #: Validated condition-linked annotations. Kept after the legacy fields so
    #: positional construction of Report remains backward compatible.
    evidence_tracks: tuple[EvidenceTrack, ...] = ()

    @property
    def tools_ran(self) -> list[str]:
        return [r.tool for r in self.tool_results if r.ok]

    @property
    def tools_failed(self) -> list[tuple[str, str]]:
        return [(r.tool, r.error) for r in self.tool_results if r.status == "failed"]

    @property
    def tools_skipped(self) -> list[tuple[str, str]]:
        return [(r.tool, r.error) for r in self.tool_results if r.status == "skipped"]

    def ranked(self) -> list[CandidateReport]:
        return sorted(
            self.candidates,
            key=lambda c: (c.score.value if c.score else -1.0),
            reverse=True,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_schema_version": "2.0",
            "mode": self.mode,
            "sequence": {
                "name": self.sequence.name,
                "length": len(self.sequence),
                "molecule": self.sequence.molecule,
                "gc_fraction": round(self.sequence.gc_fraction, 4),
                "sha256": self.sequence.sha256,
            },
            "settings": self.settings.to_dict(),
            "protocol": self.settings.signature(),
            "recognition_spec_id": (
                self.recognition.identifier() if self.recognition else None
            ),
            "recognition": self.recognition.to_dict() if self.recognition else None,
            "condition": self.condition.to_dict() if self.condition else None,
            "probing": self.probing.to_dict() if self.probing else None,
            "evidence_tracks": [
                track.to_dict() for track in self.evidence_tracks
            ],
            "tools": {
                "ran": self.tools_ran,
                "failed": [{"tool": t, "error": e} for t, e in self.tools_failed],
                "skipped": [{"tool": t, "reason": e} for t, e in self.tools_skipped],
            },
            "candidates": [c.to_dict() for c in self.ranked()],
            "tool_results": [r.to_dict() for r in self.tool_results],
            "warnings": self.warnings,
            "detail": self.detail,
        }


def _initialize_report_context(report: Report) -> None:
    """Record context that must survive both successful and failed runs."""
    recognition = report.recognition
    condition = report.condition
    unsupported = (
        condition.unsupported_by_secondary_structure_model() if condition else {}
    )
    if recognition and (
        recognition.partner_sequence is not None
        or recognition.endpoint != "structural_opening"
    ):
        unsupported["partner_binding_or_function"] = {
            "partner_chemistry": recognition.partner_chemistry,
            "endpoint": recognition.endpoint,
        }
    if recognition is not None:
        seed_status = recognition.seed_nucleation_status
        report.detail["recognition_scoring"] = {
            "seed_nucleation_status": seed_status,
            "seed_metrics": (
                "ranked" if recognition.supports_seed_nucleation
                else "diagnostic_only"
            ),
            "shortlist_order": (
                "seed_then_opening_cost" if recognition.supports_seed_nucleation
                else "opening_cost_only"
            ),
        }
        if seed_status == "exploratory":
            report.detail["recognition_scoring"]["assumption"] = (
                "no complementary binder class was declared; seed accessibility "
                "uses the generic exploratory complementary-strand proxy"
            )
        elif seed_status == "not_applicable":
            unsupported["seed_nucleation_ranking"] = {
                "binder_class": recognition.binder_class,
                "reason": (
                    "no complementary base-pair nucleation mechanism was "
                    "declared"
                ),
            }
            report.warnings.append(
                f"binder class {recognition.binder_class!r} does not declare "
                "a complementary nucleation mechanism; seed metrics are "
                "excluded from screening and ranking, and the remaining "
                "structural-opening rank is not a binding-affinity prediction"
            )
    report.detail["unsupported_assumptions"] = unsupported
    report.detail["ranking_semantics"] = (
        "heuristic_rank_score is an uncalibrated structural ranking aid, not "
        "a probability of binding, cleavage, or cellular function"
    )
    report.detail["sequence_sha256"] = report.sequence.sha256
    if report.probing is not None:
        report.detail["probing"] = report.probing.to_dict()
    if report.evidence_tracks:
        matches = {
            _evidence_condition_status(track, condition)
            for track in report.evidence_tracks
        }
        report.detail["evidence_tracks"] = {
            "count": len(report.evidence_tracks),
            "condition_statuses": sorted(matches),
            "scoring": "annotation_only",
        }
        report.warnings.append(
            "condition-linked evidence tracks are displayed as annotations; "
            "they do not alter the uncalibrated structural heuristic rank"
        )
        if "different_condition" in matches:
            report.warnings.append(
                "one or more evidence tracks were measured under a different "
                "condition and are labeled as unmatched rather than treated as "
                "evidence for this calculation"
            )
    if unsupported and set(unsupported) != {"seed_nucleation_ranking"}:
        report.warnings.append(
            "some declared recognition or environmental fields are recorded "
            "but are not modeled by the target-RNA secondary-structure layer"
        )


def _validated_evidence_tracks(
    sequence: Sequence, evidence_tracks: Iterable[EvidenceTrack] | None,
) -> tuple[EvidenceTrack, ...]:
    """Validate direct-API evidence just as strictly as file imports."""
    tracks = tuple(evidence_tracks or ())
    for index, track in enumerate(tracks, start=1):
        if not isinstance(track, EvidenceTrack):
            raise TypeError(
                f"evidence track {index} must be an EvidenceTrack, not "
                f"{type(track).__name__}"
            )
        track.validate_against(sequence)
    return tracks


def _evidence_condition_status(
    track: EvidenceTrack, condition: ConditionSpec | None,
) -> str:
    """Describe condition identity without guessing an effect direction."""
    if (
        condition is None
        or condition.condition_id == "unspecified"
        or track.condition_id == "unspecified"
    ):
        return "unverified"
    return "matched" if track.condition_id == condition.condition_id else "different_condition"


def _overlapping_evidence(
    tracks: TSequence[EvidenceTrack], region: Region,
    condition: ConditionSpec | None,
) -> list[dict[str, Any]]:
    """Return raw overlapping evidence records with their condition status.

    An overlap says only that an observation maps to this target interval. Its
    interpretation and measurement limitations remain attached to the source
    record; callers must not convert it into occupancy or accessibility.
    """
    overlap: list[dict[str, Any]] = []
    for track in tracks:
        condition_status = _evidence_condition_status(track, condition)
        for record in track.records:
            if not record.interval.overlaps(region):
                continue
            overlap.append({
                "track_id": track.track_id,
                "evidence_type": track.evidence_type,
                "source": track.source,
                "condition_id": track.condition_id,
                "condition_status": condition_status,
                "transcript_id": track.transcript_id,
                "sequence_hash": track.sequence_hash,
                "track_interpretation": track.interpretation,
                "record": record.to_dict(),
            })
    return overlap


def _criteria_for_recognition(
    report: Report, criteria: TSequence[Criterion],
) -> tuple[Criterion, ...]:
    """Remove seed-derived ranking terms without discarding raw observations."""
    recognition = report.recognition
    active = tuple(criteria)
    if recognition is None or recognition.supports_seed_nucleation:
        excluded: list[str] = []
    else:
        excluded = [
            criterion.key for criterion in active
            if criterion.key in _SEED_NUCLEATION_METRICS
        ]
        active = tuple(
            criterion for criterion in active
            if criterion.key not in _SEED_NUCLEATION_METRICS
        )
    scoring = report.detail.setdefault("recognition_scoring", {})
    scoring["active_criteria"] = [criterion.key for criterion in active]
    if excluded:
        scoring["excluded_criteria"] = excluded
    return active


def evaluate(
    sequence: Sequence,
    regions: TSequence[Region],
    settings: ModelSettings | None = None,
    probing: ProbingData | None = None,
    recognition: RecognitionSpec | None = None,
    condition: ConditionSpec | None = None,
    seed_length: int = 10,
    tools: Iterable[str] | None = None,
    criteria: TSequence[Criterion] = DEFAULT_CRITERIA,
    robustness: bool = False,
    ribosnitch: bool = False,
    context_robustness: bool = False,
    length_robustness: bool = False,
    max_cost: int | None = DEFAULT_MAX_COST,
    options: dict[str, Any] | None = None,
    progress: ProgressFn = _noop,
    evidence_tracks: Iterable[EvidenceTrack] | None = None,
) -> Report:
    """Characterise named regions with every applicable tool.

    This is the deep-dive path: no filtering, everything that can run does.
    """
    settings = (settings or ModelSettings()).for_molecule(sequence.molecule)
    recognition = recognition or RecognitionSpec(seed_lengths=(seed_length,))
    condition = condition or ConditionSpec(
        temperature_c=settings.temperature_c,
        sodium_molar=settings.salt_molar,
    )
    _validate_condition(settings, condition)
    evidence_tracks = _validated_evidence_tracks(sequence, evidence_tracks)
    options = dict(options or {})
    report = Report(
        sequence=sequence, settings=settings, mode="evaluate",
        recognition=recognition, condition=condition, probing=probing,
        evidence_tracks=evidence_tracks,
    )
    _initialize_report_context(report)
    active_criteria = _criteria_for_recognition(report, criteria)
    regions = list(regions)

    if sequence.has_ambiguous:
        report.warnings.append(
            "target contains ambiguous IUPAC codes; folding treats them as "
            "unpairable, which inflates apparent accessibility"
        )

    access_request = AccessibilityRequest(
        sequence=sequence, regions=regions, settings=settings,
        probing=probing, seed_length=seed_length, options=options,
        recognition=recognition, condition=condition,
    )
    for adapter in select(names=tools, max_cost=max_cost):
        progress(f"{adapter.name} ({adapter.tier.value})")
        report.tool_results.append(adapter.run_accessibility(access_request))

    spreads: dict[str, float] = {}
    if robustness:
        progress("robustness sweep across model settings")
        spreads = _robustness_sweep(
            sequence, regions, settings, probing, seed_length, options, report
        )

    ribosnitch_spreads: dict[str, float] = {}
    if ribosnitch:
        progress("ribosnitch sweep: every single-point mutant of each region")
        ribosnitch_spreads = _ribosnitch_scan(sequence, regions, settings, report)

    context_spreads: dict[str, float] = {}
    if context_robustness:
        progress("context sweep: refolding each region with more or less flank")
        context_spreads = _context_sweep(sequence, regions, settings, probing, report)

    length_spreads: dict[str, float] = {}
    if length_robustness:
        progress("length sweep: refolding each region at nearby window lengths")
        length_spreads = _length_sweep(
            sequence, regions, settings, probing, report
        )

    if ribosnitch or context_robustness or length_robustness:
        report.warnings.append(
            "the ribosnitch, context and length sweeps fold a "
            f"±{RIBOSNITCH_CONTEXT_FLANK} nt local context around each "
            "region, not the whole sequence the headline dG_open uses; their "
            "reported spreads are internally consistent but not directly "
            "comparable in magnitude to dG_open itself"
        )

    _assemble(
        report, regions, spreads, ribosnitch_spreads, context_spreads,
        length_spreads, active_criteria,
    )
    return report


def scan(
    sequence: Sequence,
    window: int = 25,
    step: int = 1,
    settings: ModelSettings | None = None,
    probing: ProbingData | None = None,
    recognition: RecognitionSpec | None = None,
    condition: ConditionSpec | None = None,
    seed_length: int = 10,
    keep: int = 25,
    screen_tool: str = "rnaplfold",
    tools: Iterable[str] | None = None,
    criteria: TSequence[Criterion] = DEFAULT_CRITERIA,
    robustness: bool = False,
    ribosnitch: bool = False,
    context_robustness: bool = False,
    length_robustness: bool = False,
    max_cost: int | None = DEFAULT_MAX_COST,
    options: dict[str, Any] | None = None,
    progress: ProgressFn = _noop,
    evidence_tracks: Iterable[EvidenceTrack] | None = None,
) -> Report:
    """Tile the transcript, screen every window cheaply, then dig into the best.

    The screen uses a single local-folding pass over all windows, which is the
    only stage that scales to a whole transcript. Everything after it sees at
    most ``keep`` candidates.
    """
    settings = (settings or ModelSettings()).for_molecule(sequence.molecule)
    recognition = recognition or RecognitionSpec(seed_lengths=(seed_length,))
    condition = condition or ConditionSpec(
        temperature_c=settings.temperature_c,
        sodium_molar=settings.salt_molar,
    )
    _validate_condition(settings, condition)
    evidence_tracks = _validated_evidence_tracks(sequence, evidence_tracks)
    options = dict(options or {})
    report = Report(
        sequence=sequence, settings=settings, mode="scan",
        recognition=recognition, condition=condition, probing=probing,
        evidence_tracks=evidence_tracks,
    )
    _initialize_report_context(report)
    _criteria_for_recognition(report, criteria)

    tiled_windows = tile_regions(len(sequence), window, step)
    windows = tiled_windows
    if recognition.requires_declared_seed:
        windows = [
            candidate for candidate in tiled_windows
            if recognition.permitted_seed_starts(candidate, seed_length)
        ]
        report.detail["windows_excluded_by_recognition"] = (
            len(tiled_windows) - len(windows)
        )
    report.detail["windows_tiled"] = len(tiled_windows)
    report.detail["windows_screened"] = len(windows)
    report.detail["screen_tool"] = screen_tool
    if not windows:
        report.warnings.append(
            "no tiled candidate contains an allowed fixed/listed seed; adjust "
            "the seed coordinate, seed length, or scan window"
        )
        return report
    progress(f"screening {len(windows)} windows of {window} nt with {screen_tool}")

    screen = select(names=[screen_tool], max_cost=None)
    if not screen:
        raise RuntimeError(
            f"screening tool {screen_tool!r} is not available; "
            "run tools/install_tools.sh or choose another with --screen-tool"
        )
    screen_result = screen[0].run_accessibility(AccessibilityRequest(
        sequence=sequence, regions=windows, settings=settings,
        probing=probing, seed_length=seed_length, options=options,
        recognition=recognition, condition=condition,
    ))
    report.tool_results.append(screen_result)
    if not screen_result.ok:
        report.warnings.append(
            f"screening with {screen_tool} did not run: {screen_result.error}"
        )
        report.detail["screening_failure"] = screen_result.error
        return report

    profile = _build_profile(sequence, settings, window, probing, report)
    if profile:
        report.detail["profile"] = profile
        report.detail["profile_window"] = window

    shortlist = _shortlist(
        screen_result, windows, keep,
        use_seed=recognition.supports_seed_nucleation,
    )
    report.detail["windows_kept"] = len(shortlist)
    if not shortlist:
        report.warnings.append(
            "no window produced a usable accessibility value; try a shorter "
            "--window or a wider --window-size"
        )
        return report

    progress(
        f"kept {len(shortlist)} of {len(windows)} windows for detailed analysis"
    )

    deep = evaluate(
        sequence=sequence, regions=shortlist, settings=settings,
        probing=probing, evidence_tracks=evidence_tracks,
        seed_length=seed_length, tools=tools, criteria=criteria,
        recognition=recognition, condition=condition,
        robustness=robustness, ribosnitch=ribosnitch,
        context_robustness=context_robustness, length_robustness=length_robustness,
        max_cost=max_cost, options=options,
        progress=progress,
    )

    # Keep the screening pass in the record, then adopt the deep results.
    deep.tool_results.insert(0, screen_result)
    deep.mode = "scan"
    deep.detail.update(report.detail)
    deep.warnings = list(dict.fromkeys(report.warnings + deep.warnings))
    deep.profile_table = report.profile_table
    return deep


#: Longest window length tabulated for the accessibility landscape, capped
#: independent of ``--window`` so a very wide window request doesn't blow up
#: the heatmap's row count. The per-base profile itself is unaffected by
#: this cap as long as ``--window`` is within it.
PROFILE_MAX_LENGTH = 50


def _build_profile(
    sequence: Sequence,
    settings: ModelSettings,
    window: int,
    probing: ProbingData | None,
    report: Report,
) -> dict[str, float]:
    """Compute RNAplfold's (position, length) table once for the whole
    transcript, keep the raw table on ``report`` for the HTML landscape and
    profile plots, and return the one-length slice worth persisting as
    numbers (for ``report.json``/a profile TSV).

    Deliberately independent of ``--step``: every position gets a value
    here, because the underlying table is already at single-nucleotide
    resolution and reading more of it costs nothing further (see the
    per-tool timing note in the project's methods review) — a coarse
    ``--step`` only decided how many *candidates* get the expensive deep
    stage, never how finely this profile is drawn.
    """
    from ..adapters import _vienna as V
    from ..core import thermo

    if not V.availability().available:
        report.warnings.append(
            "accessibility profile needs the ViennaRNA python bindings, "
            "which are unavailable"
        )
        return {}

    max_length = min(max(window, settings.max_unpaired), PROFILE_MAX_LENGTH)
    try:
        table = V.local_unpaired_matrix(
            sequence.seq, settings, max_length, probing=probing
        )
    except Exception as exc:                            # noqa: BLE001
        report.warnings.append(f"accessibility profile failed: {exc}")
        return {}

    report.profile_table = table
    profile: dict[str, float] = {}
    for start in range(1, len(sequence) - window + 2):
        region = Region(start, start + window - 1)
        p = V.region_probability_from_table(table, region)
        if p is None:
            continue
        profile[str(start)] = thermo.dg_open_from_probability(
            p, settings.temperature_c
        ) / window
    return profile


def _shortlist(
    screen_result: ToolResult,
    windows: TSequence[Region],
    keep: int,
    *,
    use_seed: bool = True,
) -> list[Region]:
    """Rank screened windows by the declared recognition mechanism.

    Complementary-strand binders prioritize seed accessibility, then opening
    cost.  When no complementary nucleation mechanism is declared, a seed is
    not a valid selection proxy and the screen orders structural opening cost
    alone.
    """
    scored: list[tuple[float, float, Region]] = []
    for region in windows:
        metrics = screen_result.regions.get(f"{region.start}-{region.end}")
        if metrics is None:
            continue
        seed = metrics.get(M.SEED_P_UNPAIRED)
        dg_per_nt = metrics.get(M.DG_OPEN_PER_NT)
        if use_seed:
            if seed is None and dg_per_nt is None:
                continue
            scored.append((
                seed if seed is not None else 0.0,
                -(dg_per_nt if dg_per_nt is not None else 1e6),
                region,
            ))
        elif dg_per_nt is not None:
            scored.append((-dg_per_nt, 0.0, region))
    scored.sort(key=lambda t: (-t[0], -t[1], t[2].start))

    # Prefer non-overlapping sites so the shortlist is not fifteen shifts of
    # the same hairpin loop.
    chosen: list[Region] = []
    for _, _, region in scored:
        if any(region.overlaps(other) for other in chosen):
            continue
        chosen.append(region)
        if len(chosen) >= keep:
            break
    if not chosen:
        chosen = [region for _, _, region in scored[:keep]]
    return chosen


def _robustness_sweep(
    sequence: Sequence,
    regions: TSequence[Region],
    settings: ModelSettings,
    probing: ProbingData | None,
    seed_length: int,
    options: dict[str, Any],
    report: Report,
) -> dict[str, float]:
    """Re-screen under perturbed folding parameters and measure the spread.

    Returns the per-region range of dG_open across the variants. A candidate
    whose opening cost is stable under these perturbations is one whose
    ranking does not depend on a parameter choice nobody can defend exactly.
    """
    adapters = select(names=["rnaplfold"], max_cost=None)
    if not adapters:
        report.warnings.append("robustness sweep needs rnaplfold, which is unavailable")
        return {}
    adapter = adapters[0]

    per_region: dict[str, list[float]] = {}
    orderings: list[list[str]] = []
    variants = list(settings.variants())

    for variant in variants:
        result = adapter.run_accessibility(AccessibilityRequest(
            sequence=sequence, regions=list(regions), settings=variant,
            probing=probing, seed_length=seed_length, options=options,
        ))
        if not result.ok:
            continue
        ranking: list[tuple[float, str]] = []
        for region in regions:
            key = f"{region.start}-{region.end}"
            metrics = result.regions.get(key)
            if metrics is None:
                continue
            dg_open = metrics.get(M.DG_OPEN)
            if dg_open is None:
                continue
            per_region.setdefault(key, []).append(dg_open)
            ranking.append((dg_open, key))
        ranking.sort()
        orderings.append([key for _, key in ranking])

    report.detail["robustness_variants"] = [v.signature() for v in variants]
    report.detail["rank_stability"] = rank_stability(orderings)

    spreads: dict[str, float] = {}
    for key, values in per_region.items():
        if len(values) >= 2:
            spreads[key] = max(values) - min(values)
    return spreads


#: Local context folded around each region for the ribosnitch mutation scan.
#: Bounded independent of transcript length so the O(3 x region length)
#: mutants stay a matter of seconds, not minutes, on a long input.
RIBOSNITCH_CONTEXT_FLANK = 100

#: Flank widths tried by the context-sensitivity sweep, narrowest first. The
#: whole remaining sequence is always tried too, as the natural upper end.
CONTEXT_SWEEP_FLANKS = (0, 30, 75, 150, 300)

_RNA_ALPHABET = "ACGU"


def _ribosnitch_scan(
    sequence: Sequence,
    regions: TSequence[Region],
    settings: ModelSettings,
    report: Report,
) -> dict[str, float]:
    """Fold every single-point mutant of each region, on its local context.

    Answers a question the folding model itself cannot: is this ranking a
    property of the site, or an accident of the one sequence you happened to
    give it. A natural SNP, a sequencing error, or a codon-optimisation choice
    is a point mutation, and if one of the three possible substitutions at any
    position swings dG_open by kcal/mol, the site is a riboSNitch candidate —
    fragile in a way no amount of re-running the same tool would reveal.

    Deliberately ignores any supplied SHAPE/DMS data: reactivity was measured
    on the real, unmutated molecule and saying nothing about a hypothetical
    point mutant is more honest than carrying it over unchanged.
    """
    from ..adapters import _vienna as V

    if not V.availability().available:
        report.warnings.append(
            "ribosnitch sweep needs the ViennaRNA python bindings, which are "
            "unavailable"
        )
        return {}

    spreads: dict[str, float] = {}
    detail: dict[str, dict[str, Any]] = {}

    for region in regions:
        key = f"{region.start}-{region.end}"
        context = region.with_flanks(
            RIBOSNITCH_CONTEXT_FLANK, RIBOSNITCH_CONTEXT_FLANK, len(sequence)
        )
        local = region.to_local(context)
        bases = list(context.slice(sequence))

        def dg_open_of(candidate_seq: str) -> float | None:
            try:
                free = V.ensemble_free_energy(V.make_fold_compound(candidate_seq, settings))
                return V.constrained_free_energy(
                    candidate_seq, settings, list(local.positions())
                ) - free
            except Exception:                            # noqa: BLE001
                return None

        wild_type = dg_open_of("".join(bases))
        if wild_type is None:
            continue

        worst = (wild_type, None)
        best = (wild_type, None)
        for offset in range(local.start, local.end + 1):
            original = bases[offset - 1]
            for alt in _RNA_ALPHABET:
                if alt == original:
                    continue
                mutant = bases.copy()
                mutant[offset - 1] = alt
                dg = dg_open_of("".join(mutant))
                if dg is None:
                    continue
                global_pos = region.start + (offset - local.start)
                mutation = (global_pos, original, alt, dg)
                if dg > worst[0]:
                    worst = (dg, mutation)
                if dg < best[0]:
                    best = (dg, mutation)

        spreads[key] = worst[0] - best[0]
        detail[key] = {
            "wild_type_dg_open": wild_type,
            "worst_mutation": worst[1],
            "best_mutation": best[1],
        }

    report.detail["ribosnitch_scan"] = detail
    return spreads


def _context_sweep(
    sequence: Sequence,
    regions: TSequence[Region],
    settings: ModelSettings,
    probing: ProbingData | None,
    report: Report,
) -> dict[str, float]:
    """Refold each region with different amounts of flanking context.

    Every adapter here folds whatever sequence it is handed, in full — where
    you cut the FASTA is a modelling choice nothing checks. A neighbouring
    UTR, vector scar or assembly overhang can bury or expose a site as surely
    as the site's own sequence can, so this refolds each region at several
    flank widths, from none to the whole remaining sequence, and reports how
    much dG_open moves. A candidate whose ranking depends on how much
    surrounding sequence you happened to include is not one you can defend
    without also defending that choice.
    """
    from ..adapters import _vienna as V

    if not V.availability().available:
        report.warnings.append(
            "context sweep needs the ViennaRNA python bindings, which are "
            "unavailable"
        )
        return {}

    spreads: dict[str, float] = {}
    detail: dict[str, dict[str, Any]] = {}

    for region in regions:
        key = f"{region.start}-{region.end}"
        seen: set[tuple[int, int]] = set()
        values: dict[str, float] = {}

        widths = list(CONTEXT_SWEEP_FLANKS) + [len(sequence)]
        for flank in widths:
            context = region.with_flanks(flank, flank, len(sequence))
            bounds = (context.start, context.end)
            if bounds in seen:
                continue
            seen.add(bounds)
            local = region.to_local(context)
            context_seq = context.slice(sequence)
            context_probing = (
                probing.sliced(context.start, context.end) if probing else None
            )
            try:
                free = V.ensemble_free_energy(
                    V.make_fold_compound(context_seq, settings, probing=context_probing)
                )
                dg = V.constrained_free_energy(
                    context_seq, settings, list(local.positions()),
                    probing=context_probing,
                ) - free
            except Exception:                            # noqa: BLE001
                continue
            values[f"{bounds[0]}-{bounds[1]}"] = dg

        if len(values) >= 2:
            spreads[key] = max(values.values()) - min(values.values())
            detail[key] = values

    report.detail["context_sweep"] = detail
    return spreads


#: Offsets (nt) from a candidate's own length tried by the length-robustness
#: sweep, symmetric and modest: the point is to ask "does this rank survive
#: nearby, equally defensible choices of window length", not to re-litigate
#: the window length from scratch the way `scan --window` already does.
LENGTH_SWEEP_OFFSETS = (-6, -3, 0, 3, 6)

#: Shortest window length the sweep will try, regardless of offset.
LENGTH_SWEEP_MIN = 6


def _length_sweep(
    sequence: Sequence,
    regions: TSequence[Region],
    settings: ModelSettings,
    probing: ProbingData | None,
    report: Report,
) -> dict[str, float]:
    """Refold each candidate at several nearby window lengths.

    The window length is a design choice (what will bind there), not a
    physical constant, and dG_open_per_nt is not even monotonic in it —
    opening cost tracks which helices the boundary falls across, a step
    function of length, not a smooth trend. A site that only looks cheap to
    open at exactly the length it happened to be screened at is a narrower
    bet than one that stays cheap across nearby lengths. Every variant keeps
    the region's start fixed and extends or trims from the end, folded on
    the same local context as the ribosnitch and context sweeps (see their
    docstrings for why that context, not the whole sequence, is used here).
    """
    from ..adapters import _vienna as V

    if not V.availability().available:
        report.warnings.append(
            "length-robustness sweep needs the ViennaRNA python bindings, "
            "which are unavailable"
        )
        return {}

    spreads: dict[str, float] = {}
    detail: dict[str, dict[str, float]] = {}
    contexts: dict[str, dict[str, int]] = {}

    for region in regions:
        key = f"{region.start}-{region.end}"
        per_nt: dict[int, float] = {}
        lengths = [
            len(region) + offset for offset in LENGTH_SWEEP_OFFSETS
            if len(region) + offset >= LENGTH_SWEEP_MIN
            and region.start + len(region) + offset - 1 <= len(sequence)
        ]
        if not lengths:
            continue

        enclosing = Region(region.start, region.start + max(lengths) - 1)
        context = enclosing.with_flanks(
            RIBOSNITCH_CONTEXT_FLANK, RIBOSNITCH_CONTEXT_FLANK, len(sequence)
        )
        context_seq = context.slice(sequence)
        context_probing = (
            probing.sliced(context.start, context.end) if probing else None
        )
        contexts[key] = {"start": context.start, "end": context.end}

        for length in lengths:
            variant = Region(region.start, region.start + length - 1)
            local = variant.to_local(context)
            try:
                free = V.ensemble_free_energy(
                    V.make_fold_compound(
                        context_seq, settings, probing=context_probing
                    )
                )
                dg = V.constrained_free_energy(
                    context_seq, settings, list(local.positions()),
                    probing=context_probing,
                ) - free
            except Exception:                            # noqa: BLE001
                continue
            per_nt[length] = dg / length

        if len(per_nt) >= 2:
            spreads[key] = max(per_nt.values()) - min(per_nt.values())
            detail[key] = {str(length): v for length, v in per_nt.items()}

    report.detail["length_sweep"] = detail
    report.detail["length_sweep_contexts"] = contexts
    return spreads


def _window_exact_gap(consensus: dict[str, "Consensus"]) -> float | None:
    """Difference between windowed and whole-sequence opening estimates.

    Positive means the windowed group (RNAplfold, bindings and CLI averaged
    as one measurement) reports a lower dG_open than the constrained
    whole-sequence calculation. Negative means the reverse. Either direction
    can reflect window boundaries, permitted pairing partners, span settings,
    or the distinct ensemble definitions; it does not identify a unique
    mechanism or a universally trusted estimate.
    """
    dg = consensus.get(M.DG_OPEN)
    if dg is None or "vienna-exact" not in dg.primary_values:
        return None
    exact = dg.primary_values["vienna-exact"]
    windowed = [
        value for tool, value in dg.primary_values.items()
        if dg.groups.get(tool) == "vienna-rnaplfold"
    ]
    if not windowed:
        return None
    return exact - statistics.mean(windowed)


_PRIMARY_OPENING_ORDER = {
    "vienna-exact": 0,
    "rnaplfold": 1,
    "rnaplfold-cli": 2,
    "ensemble-sample": 3,
}


def _opening_observations(
    results: TSequence[ToolResult], region: Region,
    conditioning_id: str | None = None,
) -> list[OpeningObservation]:
    """Build transform-consistent observations without discarding raw tools."""
    key = f"{region.start}-{region.end}"
    observations: list[OpeningObservation] = []
    for result in results:
        status = result.conditioning.get("status")
        if not result.ok or status == "unsupported":
            continue
        if result.applied_protocol.get("unsupported"):
            continue
        result_conditioning = result.conditioning.get(
            "conditioning_id", "unconditioned"
        )
        if (
            conditioning_id is not None and status == "applied"
            and result_conditioning != conditioning_id
        ):
            continue
        metrics = result.regions.get(key)
        if metrics is None:
            continue
        raw_p = metrics.get(M.P_UNPAIRED)
        raw_dg = metrics.get(M.DG_OPEN)
        upper = metrics.detail.get("p_unpaired_upper_bound")
        if raw_p is None and raw_dg is None and upper is None:
            continue

        temperature = float(result.settings.get("temperature_c", 37.0))
        kind = "point" if raw_p is not None or raw_dg is not None else "upper_bound"
        censor_reason = None
        if raw_dg is not None:
            dg_open = raw_dg
            p_unpaired = thermo.probability_from_dg_open(raw_dg, temperature)
            if p_unpaired == 0.0:
                p_unpaired = None
                upper = math.nextafter(0.0, 1.0)
                censor_reason = (
                    "inverse probability conversion underflowed; opening "
                    "energy remains a finite point estimate"
                )
        elif raw_p is not None and raw_p > 0.0:
            p_unpaired = raw_p
            dg_open = thermo.dg_open_from_probability(raw_p, temperature)
        elif raw_p == 0.0:
            p_unpaired = None
            dg_open = None
            kind = "censored"
            upper = None
            censor_reason = (
                "backend reported zero probability; this may be a mathematical "
                "zero or numerical underflow, so no numerical upper bound is claimed"
            )
        else:
            p_unpaired = None
            dg_open = None

        seed_p = metrics.get(M.SEED_P_UNPAIRED)
        seed_dg = metrics.get(M.SEED_DG_OPEN)
        seed_censor_reason = None
        if seed_dg is not None and math.isfinite(seed_dg):
            seed_p = thermo.probability_from_dg_open(seed_dg, temperature)
            if seed_p == 0.0:
                seed_p = None
                seed_censor_reason = (
                    "seed inverse probability conversion underflowed; seed "
                    "opening energy remains a finite point estimate"
                )
        elif seed_dg is not None:
            seed_dg = None
            seed_p = None
            seed_censor_reason = "seed opening energy was non-finite"
        elif seed_p is not None and seed_p > 0.0:
            seed_dg = thermo.dg_open_from_probability(seed_p, temperature)
        elif seed_p == 0.0:
            seed_p = None
            seed_dg = None
            seed_censor_reason = (
                "backend reported zero seed probability; this may be a "
                "mathematical zero or numerical underflow"
            )
        elif seed_p is not None:
            seed_p = None
            seed_dg = None
            seed_censor_reason = "backend reported an invalid seed probability"
        if seed_censor_reason:
            censor_reason = (
                f"{censor_reason}; {seed_censor_reason}"
                if censor_reason else seed_censor_reason
            )

        scope = (
            "local_window" if "window" in result.algorithm.lower()
            else "global_ensemble"
        )
        observations.append(OpeningObservation(
            observation_id=f"{result.tool}:{key}:{result_conditioning}",
            tool=result.tool,
            interval=region,
            p_unpaired=p_unpaired,
            dg_open_kcal_mol=dg_open,
            temperature_c=temperature,
            event="all_target_nucleotides_unpaired",
            model_family=result.model_family or result.tool,
            algorithm=result.algorithm or result.tool,
            sequence_scope=scope,
            conditioning_id=result_conditioning,
            estimate_kind=kind,
            p_upper_bound=float(upper) if upper is not None else None,
            seed_start=(
                int(metrics.get(M.SEED_START))
                if metrics.get(M.SEED_START) is not None else None
            ),
            seed_length=(
                int(metrics.get(M.SEED_LENGTH))
                if metrics.get(M.SEED_LENGTH) is not None else None
            ),
            seed_p_unpaired=seed_p,
            seed_dg_open_kcal_mol=seed_dg,
            censor_reason=censor_reason,
        ))
    return observations


def _primary_opening(
    observations: TSequence[OpeningObservation],
) -> OpeningObservation | None:
    points = [o for o in observations if o.estimate_kind == "point"]
    if not points:
        return None
    return min(
        points,
        key=lambda o: (_PRIMARY_OPENING_ORDER.get(o.tool, 100), o.tool),
    )


def _assemble(
    report: Report,
    regions: TSequence[Region],
    spreads: dict[str, float],
    ribosnitch_spreads: dict[str, float],
    context_spreads: dict[str, float],
    length_spreads: dict[str, float],
    criteria: TSequence[Criterion],
) -> None:
    """Merge tool results per region, score them and attach interpretation."""
    stability = report.detail.get("rank_stability", {})
    ribosnitch_detail = report.detail.get("ribosnitch_scan", {})
    recognition = report.recognition
    uses_seed_nucleation = (
        recognition is None or recognition.supports_seed_nucleation
    )

    for region in regions:
        key = f"{region.start}-{region.end}"
        requested_conditioning = (
            report.probing.conditioning_id() if report.probing else "unconditioned"
        )
        consensus = build_consensus(
            report.tool_results, region, conditioning_id=requested_conditioning
        )

        extra: dict[str, float] = {}
        if key in spreads:
            extra[M.DG_OPEN_SPREAD] = spreads[key]
        if key in stability:
            extra[M.RANK_STABILITY] = stability[key]
        if key in ribosnitch_spreads:
            extra[M.RIBOSNITCH_SPREAD] = ribosnitch_spreads[key]
        if key in context_spreads:
            extra[M.CONTEXT_DG_SPREAD] = context_spreads[key]
        if key in length_spreads:
            extra[M.WINDOW_LENGTH_SPREAD] = length_spreads[key]
        gap = _window_exact_gap(consensus)
        if gap is not None:
            extra[M.WINDOW_EXACT_GAP] = gap

        metrics = flatten_metrics(consensus, extra)
        observations = _opening_observations(
            report.tool_results, region, conditioning_id=requested_conditioning
        )
        primary = _primary_opening(observations)
        linked = {
            M.P_UNPAIRED, M.DG_OPEN, M.DG_OPEN_PER_NT,
            M.SEED_P_UNPAIRED, M.SEED_DG_OPEN, M.SEED_START, M.SEED_LENGTH,
        }
        for name in linked:
            metrics.pop(name, None)
        if primary is not None:
            if primary.p_unpaired is not None:
                metrics[M.P_UNPAIRED] = primary.p_unpaired
            if primary.dg_open_kcal_mol is not None:
                metrics[M.DG_OPEN] = primary.dg_open_kcal_mol
                metrics[M.DG_OPEN_PER_NT] = (
                    primary.dg_open_kcal_mol / len(region)
                )
            if uses_seed_nucleation:
                if primary.seed_start is not None:
                    metrics[M.SEED_START] = float(primary.seed_start)
                if primary.seed_length is not None:
                    metrics[M.SEED_LENGTH] = float(primary.seed_length)
                if primary.seed_p_unpaired is not None:
                    metrics[M.SEED_P_UNPAIRED] = primary.seed_p_unpaired
                if primary.seed_dg_open_kcal_mol is not None:
                    metrics[M.SEED_DG_OPEN] = primary.seed_dg_open_kcal_mol
        detail: dict[str, Any] = {}
        if key in ribosnitch_detail:
            detail["ribosnitch_worst_mutation"] = ribosnitch_detail[key]["worst_mutation"]
            detail["ribosnitch_best_mutation"] = ribosnitch_detail[key]["best_mutation"]
        if not uses_seed_nucleation:
            detail["seed_nucleation"] = {
                "status": "not_applicable",
                "raw_observations": (
                    "retained with each tool result but excluded from candidate "
                    "metrics, screening, and the heuristic rank"
                ),
            }

        candidate = CandidateReport(
            region=region,
            subsequence=region.slice(report.sequence),
            consensus=consensus,
            metrics=metrics,
            score=score_candidate(metrics, criteria),
            detail=detail,
            opening_observations=observations,
            primary_opening_observation_id=(
                primary.observation_id if primary is not None else None
            ),
            biological_evidence=_overlapping_evidence(
                report.evidence_tracks, region, report.condition,
            ),
        )
        candidate.notes = _interpret(candidate)
        if candidate.biological_evidence:
            matched = sum(
                entry["condition_status"] == "matched"
                for entry in candidate.biological_evidence
            )
            candidate.notes.append(
                f"{len(candidate.biological_evidence)} condition-linked evidence "
                f"record(s) overlap this interval ({matched} condition-matched); "
                "they are annotations, not score penalties or occupancy calls"
            )
        if not uses_seed_nucleation:
            candidate.notes.insert(
                0,
                "seed accessibility is not used because the declared binder "
                "has no complementary nucleation mechanism; any raw seed "
                "readings are structural diagnostics, not affinity evidence",
            )
        report.candidates.append(candidate)

    _diagnose_run(report, criteria)


#: A criterion's desirability within this of an anchor (0 or 1) counts as
#: pinned there for the purpose of the saturation check below.
SATURATION_TOLERANCE = 0.02

#: A criterion is flagged as not discriminating in this run when at least
#: this fraction of the candidates it was scored for are pinned at an anchor.
SATURATION_THRESHOLD = 0.5

#: The two metrics whose estimator set is checked for dropout: the joint
#: probability and its energy are the quantity the whole score is built on,
#: so an inconsistent estimator there matters more than for a diagnostic
#: per-base metric.
DROPOUT_WATCHED_METRICS = (M.P_UNPAIRED, M.DG_OPEN)


def _diagnose_run(report: Report, criteria: TSequence[Criterion]) -> None:
    """Report-wide checks that no single candidate's numbers reveal alone.

    Two unrelated things live here, because both need every candidate scored
    before they mean anything:

    **Score saturation.** A desirability curve pinned at 0 or 1 for most of
    the run's candidates is not discriminating between them, however large
    its weight — a criterion's nominal weight and its *effective* weight in
    this particular run can differ sharply, and nothing about reading one
    candidate's score components reveals that; it only shows up by comparing
    across all of them.

    **Estimator dropout.** A compatible primary estimator that refuses a
    point value for the hardest-to-measure sites changes *what was measured*,
    not just the number: a candidate scored by three declared calculation
    groups and one scored by two are not directly comparable, even though
    both look like ordinary rows in the same table. A Monte Carlo upper bound
    is raw-only when an exact value from that same ensemble exists.
    """
    candidates = [c for c in report.candidates if c.score is not None]
    if not candidates:
        return

    # --- score saturation ---------------------------------------------
    saturation: dict[str, dict[str, Any]] = {}
    for criterion in criteria:
        present = [
            component
            for candidate in candidates
            for component in candidate.score.components
            if component.criterion.key == criterion.key and component.present
        ]
        if len(present) < 3:
            continue
        saturated_high = sum(
            1 for c in present if c.desirability >= 1.0 - SATURATION_TOLERANCE
        )
        saturated_low = sum(
            1 for c in present if c.desirability <= SATURATION_TOLERANCE
        )
        saturated = saturated_high + saturated_low
        fraction = saturated / len(present)
        saturation[criterion.key] = {
            "label": criterion.label,
            "weight": criterion.weight,
            "n_scored": len(present),
            "n_saturated": saturated,
            "fraction_saturated": round(fraction, 3),
        }
        if fraction >= SATURATION_THRESHOLD:
            anchor = "its accessible anchor" if saturated_high >= saturated_low \
                else "its inaccessible anchor"
            report.warnings.append(
                f"scoring criterion '{criterion.label}' is pinned at {anchor} "
                f"for {saturated}/{len(present)} candidates in this run; it "
                f"is not discriminating between them here, whatever its "
                f"weight ({criterion.weight}) implies"
            )
    if saturation:
        report.detail["score_saturation"] = saturation

    # --- estimator dropout ----------------------------------------------
    best_independent: dict[str, int] = {}
    all_groups: dict[str, set[str]] = {}
    for candidate in candidates:
        for name in DROPOUT_WATCHED_METRICS:
            agreement = candidate.consensus.get(name)
            if agreement is None:
                continue
            best_independent[name] = max(
                best_independent.get(name, 0), agreement.n_independent
            )
            groups = {agreement.groups.get(t, t) for t in agreement.values}
            all_groups.setdefault(name, set()).update(groups)

    for candidate in candidates:
        for name in DROPOUT_WATCHED_METRICS:
            agreement = candidate.consensus.get(name)
            best = best_independent.get(name, 0)
            if agreement is None or best < 2 or agreement.n_independent >= best:
                continue
            present_groups = {agreement.groups.get(t, t) for t in agreement.values}
            missing = sorted(all_groups.get(name, set()) - present_groups)
            if not missing:
                continue
            candidate.notes.append(
                f"{name} here rests on {agreement.n_independent} of the "
                f"{best} independent measurements used elsewhere in this "
                f"run ({', '.join(missing)} reported nothing for this site, "
                "often because a rare-event bound rather than a point "
                "estimate was all it could give); not a like-for-like "
                "comparison with a candidate scored by all of them"
            )
            break                                     # one dropout note is enough


def _interpret(candidate: CandidateReport) -> list[str]:
    """Turn the numbers into the handful of sentences worth reading.

    These are diagnoses, not decoration: each one names a specific failure
    mode that changes what you would do about the candidate next.
    """
    notes: list[str] = []
    metrics = candidate.metrics

    seed = metrics.get(M.SEED_P_UNPAIRED)
    joint = metrics.get(M.P_UNPAIRED)
    mean_base = metrics.get(M.MEAN_BASE_UNPAIRED)

    if seed is not None and joint is not None and seed > 100 * max(joint, 1e-30):
        notes.append(
            f"the full {len(candidate.region)} nt site is far less available "
            f"(P={joint:.2g}) than its best seed (P={seed:.2g}); a "
            "toehold-style design that only needs to nucleate here is much "
            "more plausible than one requiring the whole site open at once"
        )
    if mean_base is not None and joint is not None and mean_base > 0.5 > joint * 100:
        notes.append(
            f"per-base accessibility averages {mean_base:.2f} but the joint "
            f"probability is {joint:.2g}: these nucleotides are open at "
            "different times, not together"
        )

    spread = metrics.get(M.DG_OPEN_SPREAD)
    if spread is not None and spread > 3.0:
        notes.append(
            f"opening cost varies by {spread:.1f} kcal/mol across folding "
            "parameters; treat this ranking as provisional"
        )

    gap = metrics.get(M.WINDOW_EXACT_GAP)
    if gap is not None and abs(gap) > 1.5:
        if gap > 0:
            notes.append(
                f"the windowed engines (RNAplfold) report an opening cost "
                f"{gap:.1f} kcal/mol lower than the exact whole-sequence "
                "calculation; inspect scope, boundaries, and long-range "
                "pairing before selecting a protocol"
            )
        else:
            notes.append(
                f"the windowed engines (RNAplfold) report an opening cost "
                f"{-gap:.1f} kcal/mol higher than the exact whole-sequence "
                "calculation; the two scopes disagree and neither direction "
                "identifies the physically relevant assay model by itself"
            )

    length_spread = metrics.get(M.WINDOW_LENGTH_SPREAD)
    if length_spread is not None and length_spread > 0.08:
        notes.append(
            f"opening cost per nucleotide varies by {length_spread:.2f} "
            "kcal/mol/nt across nearby window lengths; this site's ranking "
            "depends on the specific window length it was screened at, not "
            "just on its own sequence"
        )

    pk_fraction = metrics.get(M.PSEUDOKNOT_PAIRED_FRACTION)
    if pk_fraction is not None and pk_fraction > 0.2:
        notes.append(
            f"ProbKnot pairs {pk_fraction:.0%} of this site into a crossing "
            "(pseudoknotted) helix that no nested-pair engine here can "
            "represent; every other accessibility number may be optimistic"
        )

    gquad = metrics.get(M.GQUAD_SCORE)
    if gquad is not None and gquad >= 1.2:
        notes.append(
            f"G4Hunter score {gquad:.2f} is above the published quadruplex "
            "threshold (1.2): the G-rich sequence has G-quadruplex "
            "propensity that nested-pair folding engines do not represent"
        )

    trap = metrics.get(M.CO_TX_TRAP_LENGTH)
    if trap is not None:
        notes.append(
            f"kinwalker's co-transcriptional trajectory locks this site "
            f"closed by transcript length {int(trap)} nt and never reopens "
            "it, regardless of what the finished molecule's equilibrium "
            "ensemble says about it"
        )

    ribosnitch = metrics.get(M.RIBOSNITCH_SPREAD)
    if ribosnitch is not None and ribosnitch > 3.0:
        mutation_detail = candidate.detail.get("ribosnitch_worst_mutation")
        where = ""
        if mutation_detail:
            pos, ref, alt, _ = mutation_detail
            where = f" (position {pos}, {ref}→{alt} is the worst case)"
        notes.append(
            f"a single point mutation can move the opening cost by "
            f"{ribosnitch:.1f} kcal/mol{where}; this is a riboSNitch "
            "candidate — a SNP or sequencing error could flip this ranking"
        )

    context_spread = metrics.get(M.CONTEXT_DG_SPREAD)
    if context_spread is not None and context_spread > 2.0:
        notes.append(
            f"opening cost varies by {context_spread:.1f} kcal/mol depending "
            "on how much flanking sequence is folded with it; confirm the "
            "modelled context matches the real construct before trusting "
            "this rank"
        )

    if candidate.score and candidate.score.coverage < 0.5:
        notes.append(
            f"only {candidate.score.coverage:.0%} of the scoring weight had "
            "data behind it; the score is provisional"
        )
    return notes
