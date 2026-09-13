"""Scoring, consensus, drivers, I/O and the command line."""

import json
import math

import pytest

from rnavail.adapters.base import AccessibilityRequest
from rnavail.core.model import ConditionSpec, ModelSettings, ProbingData, RecognitionSpec
from rnavail.core.result import M, RegionMetrics, Tier, ToolResult
from rnavail.core.sequence import Region, Sequence
from rnavail.io.fasta import read_fasta, read_probing, read_sequence
from rnavail.io.report import to_json, to_profile_tsv, to_text, to_tsv
from rnavail.pipeline.run import evaluate, scan
from rnavail.pipeline.score import (
    DEFAULT_CRITERIA, build_consensus, flatten_metrics, load_weights,
    rank_stability, score_candidate,
)

TARGET = Sequence(
    "target",
    "GGGAAACCCAUAUAUAUAUGCGCGCUUUUUUGCGCGCAAAGGGAAACCCUUAAGGUUCCAAGGUUCC",
)
SETTINGS = ModelSettings(max_bp_span=60, window_size=67)


def metrics_for(**values):
    return dict(values)


class TestScoring:
    def test_better_physics_scores_higher(self):
        strong = metrics_for(
            seed_p_unpaired=0.6, dg_open_per_nt=0.08, p_unpaired=0.02,
            dg_total=-16.0, ontarget_margin=6.0,
        )
        weak = metrics_for(
            seed_p_unpaired=1e-4, dg_open_per_nt=1.1, p_unpaired=1e-10,
            dg_total=-1.0, ontarget_margin=-3.0,
        )
        assert score_candidate(strong).value > score_candidate(weak).value

    def test_score_is_conjunctive_not_additive(self):
        """A great seed does not save a site with a costly full footprint.

        A weighted geometric mean must retain the full-footprint cost instead
        of allowing a favourable seed to dominate the heuristic.
        """
        great_seed_but_never_fully_open = metrics_for(
            seed_p_unpaired=0.95, dg_open_per_nt=1.0, p_unpaired=1e-9,
        )
        assert score_candidate(great_seed_but_never_fully_open).value < 0.15

    def test_score_is_bounded(self):
        perfect = metrics_for(
            seed_p_unpaired=1.0, dg_open_per_nt=0.0, p_unpaired=1.0,
            dg_open_spread=0.0,
        )
        assert 0.0 <= score_candidate(perfect).value <= 1.0

    def test_missing_metrics_lower_coverage_not_the_score(self):
        full = metrics_for(
            seed_p_unpaired=0.6, dg_open_per_nt=0.08, p_unpaired=0.02,
            dg_open_spread=0.2,
        )
        partial = {k: v for k, v in full.items() if k in ("seed_p_unpaired",)}
        assert score_candidate(partial).coverage < score_candidate(full).coverage
        assert score_candidate(partial).value > 0

    def test_no_data_gives_zero_and_no_crash(self):
        score = score_candidate({})
        assert score.value == 0.0 and score.coverage == 0.0

    def test_components_explain_the_score(self):
        score = score_candidate(metrics_for(seed_p_unpaired=0.5))
        present = [c for c in score.components if c.present]
        assert len(present) == 1
        assert present[0].criterion.key == M.SEED_P_UNPAIRED
        assert 0 <= present[0].desirability <= 1

    def test_weights_can_be_overridden(self, tmp_path):
        path = tmp_path / "w.json"
        path.write_text(json.dumps({"dg_open_per_nt": 9.0}))
        criteria = load_weights(path)
        assert {c.key: c.weight for c in criteria}["dg_open_per_nt"] == 9.0

    def test_unknown_weight_key_is_rejected(self, tmp_path):
        path = tmp_path / "w.json"
        path.write_text(json.dumps({"not_a_metric": 1.0}))
        with pytest.raises(ValueError, match="unknown metrics"):
            load_weights(path)

    @pytest.mark.parametrize("value", (-1, float("nan"), float("inf"), "bad"))
    def test_invalid_weight_value_is_rejected(self, tmp_path, value):
        path = tmp_path / "w.json"
        path.write_text(json.dumps({"seed_p_unpaired": value}))
        with pytest.raises(ValueError, match="finite non-negative"):
            load_weights(path)

    def test_score_rejects_invalid_api_criterion_weight(self):
        from rnavail.pipeline.score import Criterion
        with pytest.raises(ValueError, match="invalid weight"):
            score_candidate(
                {}, (Criterion("x", -1.0, lambda value: value, "x"),)
            )


class TestConsensus:
    def test_collects_the_same_metric_across_tools(self):
        region = Region(1, 5)
        results = []
        for tool, value in (("a", 1.0), ("b", 1.4)):
            result = ToolResult(tool=tool, tier=Tier.ACCESSIBILITY)
            result.region_metrics(region).set(M.DG_OPEN, value)
            results.append(result)
        agreement = build_consensus(results, region)[M.DG_OPEN]
        assert agreement.n == 2
        assert agreement.median == pytest.approx(1.2)
        assert agreement.spread == pytest.approx(0.4)

    def test_failed_tools_are_excluded(self):
        region = Region(1, 5)
        good = ToolResult(tool="good", tier=Tier.ACCESSIBILITY)
        good.region_metrics(region).set(M.DG_OPEN, 1.0)
        bad = ToolResult(tool="bad", tier=Tier.ACCESSIBILITY, status="failed")
        bad.region_metrics(region).set(M.DG_OPEN, 99.0)
        assert build_consensus([good, bad], region)[M.DG_OPEN].n == 1

    def test_median_resists_one_bad_tool(self):
        region = Region(1, 5)
        results = []
        for tool, value in (("a", 1.0), ("b", 1.1), ("c", 500.0)):
            result = ToolResult(tool=tool, tier=Tier.ACCESSIBILITY)
            result.region_metrics(region).set(M.DG_OPEN, value)
            results.append(result)
        flat = flatten_metrics(build_consensus(results, region))
        assert flat[M.DG_OPEN] == pytest.approx(1.1)

    def test_a_validation_pair_counts_as_one_independent_measurement(self):
        """The exact scenario from the GFP run this was written against:
        rnaplfold and rnaplfold-cli sharing a group must not be able to
        outvote a third, genuinely independent tool.
        """
        region = Region(1, 20)
        results = [
            ToolResult(tool="rnaplfold", tier=Tier.ACCESSIBILITY,
                       independence_group="vienna-rnaplfold"),
            ToolResult(tool="rnaplfold-cli", tier=Tier.ACCESSIBILITY,
                       independence_group="vienna-rnaplfold"),
            ToolResult(tool="vienna-exact", tier=Tier.ACCESSIBILITY,
                       independence_group="vienna-exact"),
        ]
        for result, value in zip(results, (0.04895, 0.04895, 0.0002417)):
            result.region_metrics(region).set(M.P_UNPAIRED, value)

        agreement = build_consensus(results, region)[M.P_UNPAIRED]
        assert agreement.n == 3
        assert agreement.n_independent == 2
        # median of the two GROUP values (0.04895 and 0.0002417), not the
        # three raw tool values -- the duplicate must not pin it.
        assert agreement.median == pytest.approx((0.04895 + 0.0002417) / 2)
        assert agreement.spread == pytest.approx(0.04895 - 0.0002417)

    def test_estimand_gating_excludes_non_probability_tools_from_median(self):
        region = Region(1, 20)
        results = [
            ToolResult(tool="rnafold", tier=Tier.STRUCTURE, estimand="probability"),
            ToolResult(tool="contrafold", tier=Tier.STRUCTURE, estimand="posterior"),
            ToolResult(tool="linearfold", tier=Tier.STRUCTURE, estimand="single_structure"),
        ]
        for result, value in zip(results, (0.60, 0.90, 0.10)):
            result.region_metrics(region).set(M.MEAN_BASE_UNPAIRED, value)

        agreement = build_consensus(results, region)[M.MEAN_BASE_UNPAIRED]
        assert agreement.n == 3
        assert agreement.n_independent == 1
        assert agreement.median == pytest.approx(0.60)
        assert agreement.excluded == {
            "contrafold": "posterior", "linearfold": "single_structure",
        }
        # nothing is hidden -- every raw value is still there for display.
        assert set(agreement.values) == {"rnafold", "contrafold", "linearfold"}

    def test_estimand_gating_falls_back_when_nothing_is_a_probability(self):
        """A metric reported only by non-probability tools still shows a
        number rather than silently vanishing."""
        region = Region(1, 20)
        result = ToolResult(tool="linearfold", tier=Tier.STRUCTURE,
                             estimand="single_structure")
        result.region_metrics(region).set(M.MEAN_BASE_UNPAIRED, 0.45)
        agreement = build_consensus([result], region)[M.MEAN_BASE_UNPAIRED]
        assert agreement.median == pytest.approx(0.45)
        assert agreement.excluded == {}

    def test_monte_carlo_sample_does_not_average_into_exact_probability(self):
        """Sampling checks the same ensemble but has sampling error; an exact
        partition-function value remains the primary calculation."""
        region = Region(1, 20)
        exact = ToolResult(
            tool="vienna-exact", tier=Tier.ACCESSIBILITY,
            estimand="probability", independence_group="vienna-global-pf",
        )
        sample = ToolResult(
            tool="ensemble-sample", tier=Tier.STRUCTURE,
            estimand="monte_carlo_probability",
            independence_group="vienna-global-pf",
        )
        exact.region_metrics(region).set(M.P_UNPAIRED, 0.2)
        sample.region_metrics(region).set(M.P_UNPAIRED, 0.4)

        agreement = build_consensus([exact, sample], region)[M.P_UNPAIRED]
        assert agreement.values == {"vienna-exact": 0.2, "ensemble-sample": 0.4}
        assert agreement.primary_tools == ["vienna-exact"]
        assert agreement.median == pytest.approx(0.2)
        assert agreement.excluded == {
            "ensemble-sample": "monte_carlo_probability",
        }

    def test_incompatible_probability_protocol_is_not_pooled(self):
        region = Region(1, 5)
        compatible = ToolResult(tool="bindings", tier=Tier.ACCESSIBILITY)
        incompatible = ToolResult(tool="cli", tier=Tier.ACCESSIBILITY)
        incompatible.applied_protocol = {
            "unsupported": {"salt_molar": "adapter does not support salt"}
        }
        compatible.region_metrics(region).set(M.P_UNPAIRED, 0.2)
        incompatible.region_metrics(region).set(M.P_UNPAIRED, 0.8)

        agreement = build_consensus([compatible, incompatible], region)[M.P_UNPAIRED]
        # The raw observation remains inspectable; the primary calculation
        # excludes it because it does not answer the requested protocol.
        assert agreement.values == {"bindings": 0.2, "cli": 0.8}
        assert agreement.groups == {"bindings": "bindings", "cli": "cli"}
        assert agreement.estimands == {
            "bindings": "probability", "cli": "probability",
        }
        assert agreement.eligible_tools == ["bindings"]
        assert agreement.primary_tools == ["bindings"]
        assert agreement.n == 2
        assert agreement.n_eligible == 1
        assert agreement.n_independent == 1
        assert agreement.median == pytest.approx(0.2)
        assert agreement.excluded_protocol == {
            "cli": {"salt_molar": "adapter does not support salt"}
        }
        serialized = agreement.to_dict()
        assert serialized["by_tool"] == {"bindings": 0.2, "cli": 0.8}
        assert serialized["eligible_for_primary"] == ["bindings"]
        assert serialized["primary_for_median"] == ["bindings"]

    def test_no_compatible_value_has_no_median_or_fallback(self):
        """Raw diagnostics must not become a primary estimate by fallback."""
        region = Region(1, 5)
        protocol_incompatible = ToolResult(
            tool="cli", tier=Tier.ACCESSIBILITY, estimand="single_structure",
        )
        protocol_incompatible.applied_protocol = {
            "unsupported": {"salt_molar": "adapter does not support salt"}
        }
        unsupported_conditioning = ToolResult(
            tool="unconditioned", tier=Tier.ACCESSIBILITY,
            estimand="single_structure",
            conditioning={
                "status": "unsupported",
                "conditioning_id": "unconditioned",
                "requested_method": "shape",
            },
        )
        protocol_incompatible.region_metrics(region).set(M.P_UNPAIRED, 0.8)
        unsupported_conditioning.region_metrics(region).set(M.P_UNPAIRED, 0.4)

        agreement = build_consensus(
            [protocol_incompatible, unsupported_conditioning], region,
            conditioning_id="shape:requested",
        )[M.P_UNPAIRED]

        assert agreement.values == {"cli": 0.8, "unconditioned": 0.4}
        assert agreement.n == 2
        assert agreement.n_eligible == 0
        assert agreement.n_primary == 0
        assert agreement.eligible_tools == []
        assert agreement.primary_tools == []
        assert agreement.n_independent == 0
        assert agreement.median is None
        assert agreement.spread is None
        assert agreement.excluded == {}
        assert "cli" in agreement.excluded_protocol
        assert "unconditioned" in agreement.excluded_conditioning

    def test_unsupported_conditioning_is_preserved_but_not_primary(self):
        region = Region(1, 5)
        compatible = ToolResult(
            tool="shape-aware", tier=Tier.ACCESSIBILITY,
            conditioning={
                "status": "applied",
                "conditioning_id": "shape:requested",
            },
        )
        unsupported = ToolResult(
            tool="unconditioned", tier=Tier.ACCESSIBILITY,
            conditioning={
                "status": "unsupported",
                "conditioning_id": "unconditioned",
                "requested_method": "shape",
            },
        )
        compatible.region_metrics(region).set(M.DG_OPEN, 1.5)
        unsupported.region_metrics(region).set(M.DG_OPEN, 9.0)

        agreement = build_consensus(
            [compatible, unsupported], region,
            conditioning_id="shape:requested",
        )[M.DG_OPEN]

        assert agreement.values == {"shape-aware": 1.5, "unconditioned": 9.0}
        assert agreement.eligible_values == {"shape-aware": 1.5}
        assert agreement.primary_values == {"shape-aware": 1.5}
        assert agreement.median == pytest.approx(1.5)
        assert agreement.spread == pytest.approx(0.0)
        assert agreement.excluded_conditioning["unconditioned"].startswith(
            "adapter did not apply requested conditioning"
        )


class TestRankStability:
    def test_constant_ranking_is_perfectly_stable(self):
        assert rank_stability([["a", "b"], ["a", "b"]])["a"] == 1.0

    def test_moving_candidate_is_less_stable(self):
        stability = rank_stability([["a", "b", "c"], ["c", "b", "a"]])
        assert stability["b"] > stability["a"]

    def test_empty_input(self):
        assert rank_stability([]) == {}


class TestRegionMetrics:
    def test_non_finite_values_are_dropped(self):
        metrics = RegionMetrics(region=Region(1, 3))
        metrics.set(M.DG_OPEN, float("nan"))
        metrics.set(M.P_UNPAIRED, float("inf"))
        metrics.set(M.MFE, None)
        assert metrics.values == {}


class TestEvaluateDriver:
    @staticmethod
    @pytest.fixture(scope="class")
    def report():
        return evaluate(
            TARGET, [Region(9, 20, "loose"), Region(20, 32, "hairpin")],
            settings=SETTINGS, seed_length=8,
        )

    def test_runs_many_tools(self, report):
        assert len(report.tools_ran) >= 6

    def test_no_tool_fails(self, report):
        assert report.tools_failed == []

    def test_every_region_is_scored(self, report):
        assert len(report.candidates) == 2
        assert all(c.score is not None for c in report.candidates)

    def test_ranking_matches_the_physics(self, report):
        """The loose region must outrank the GC hairpin."""
        assert report.ranked()[0].region.name == "loose"

    def test_notes_diagnose_the_hairpin(self, report):
        hairpin = next(c for c in report.candidates if c.region.name == "hairpin")
        assert any("seed" in note for note in hairpin.notes)

    def test_consensus_covers_multiple_tools(self, report):
        loose = next(c for c in report.candidates if c.region.name == "loose")
        multi = [a for a in loose.consensus.values() if a.n >= 2]
        assert multi, "no metric was reported by more than one tool"

    def test_report_serialises(self, report):
        payload = json.loads(to_json(report))
        assert payload["mode"] == "evaluate"
        assert payload["candidates"]
        assert payload["protocol"] == SETTINGS.signature()

    def test_tsv_has_a_row_per_candidate(self, report):
        lines = to_tsv(report).strip().splitlines()
        assert len(lines) == 3
        assert lines[0].startswith("region\tstart\tend")

    def test_text_report_names_the_tools(self, report):
        text = to_text(report)
        assert "rnaplfold" in text and "ranked candidates" in text

    def test_tool_subset_is_respected(self):
        report = evaluate(TARGET, [Region(9, 20)], settings=SETTINGS,
                          tools=["rnaplfold"])
        assert report.tools_ran == ["rnaplfold"]


class TestRobustness:
    def test_sweep_reports_spread_and_stability(self):
        report = evaluate(
            TARGET, [Region(9, 20), Region(20, 32)], settings=SETTINGS,
            tools=["rnaplfold"], robustness=True, seed_length=8,
        )
        assert report.detail["robustness_variants"]
        assert report.detail["rank_stability"]
        assert all(M.DG_OPEN_SPREAD in c.metrics for c in report.candidates)


class TestRibosnitch:
    """Sequence robustness: does a single point mutation change the ranking."""

    @staticmethod
    @pytest.fixture(scope="class")
    def report():
        # A short region keeps the 3 x length mutant scan fast in tests.
        return evaluate(
            TARGET, [Region(9, 12, "loose")], settings=SETTINGS,
            tools=["rnaplfold"], ribosnitch=True, seed_length=4,
        )

    def test_reports_a_nonnegative_spread(self, report):
        candidate = report.candidates[0]
        assert M.RIBOSNITCH_SPREAD in candidate.metrics
        assert candidate.metrics[M.RIBOSNITCH_SPREAD] >= 0.0

    def test_worst_and_best_mutations_are_inside_the_region_and_differ(self, report):
        scan = report.detail["ribosnitch_scan"]["9-12"]
        for mutation in (scan["worst_mutation"], scan["best_mutation"]):
            pos, ref, alt, dg = mutation
            assert 9 <= pos <= 12
            assert ref != alt
            assert ref in "ACGU" and alt in "ACGU"
            assert math.isfinite(dg)

    def test_off_by_default(self):
        report = evaluate(
            TARGET, [Region(9, 12)], settings=SETTINGS, tools=["rnaplfold"],
        )
        assert M.RIBOSNITCH_SPREAD not in report.candidates[0].metrics
        assert "ribosnitch_scan" not in report.detail


class TestContextSweep:
    """Does the ranking depend on how much flanking sequence was folded."""

    @staticmethod
    @pytest.fixture(scope="class")
    def report():
        return evaluate(
            TARGET, [Region(9, 20), Region(20, 32)], settings=SETTINGS,
            tools=["rnaplfold"], context_robustness=True, seed_length=8,
        )

    def test_reports_a_nonnegative_spread(self, report):
        for candidate in report.candidates:
            assert M.CONTEXT_DG_SPREAD in candidate.metrics
            assert candidate.metrics[M.CONTEXT_DG_SPREAD] >= 0.0

    def test_detail_has_at_least_two_distinct_context_widths(self, report):
        for key in ("9-20", "20-32"):
            values = report.detail["context_sweep"][key]
            assert len(values) >= 2

    def test_off_by_default(self):
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS, tools=["rnaplfold"],
        )
        assert M.CONTEXT_DG_SPREAD not in report.candidates[0].metrics


class TestLengthSweep:
    """Does the ranking depend on the window length, a design choice."""

    @staticmethod
    @pytest.fixture(scope="class")
    def report():
        return evaluate(
            TARGET, [Region(9, 20), Region(20, 32)], settings=SETTINGS,
            tools=["rnaplfold"], length_robustness=True, seed_length=8,
        )

    def test_reports_a_nonnegative_spread(self, report):
        for candidate in report.candidates:
            assert M.WINDOW_LENGTH_SPREAD in candidate.metrics
            assert candidate.metrics[M.WINDOW_LENGTH_SPREAD] >= 0.0

    def test_detail_has_at_least_two_distinct_lengths(self, report):
        for key in ("9-20", "20-32"):
            values = report.detail["length_sweep"][key]
            assert len(values) >= 2

    def test_off_by_default(self):
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS, tools=["rnaplfold"],
        )
        assert M.WINDOW_LENGTH_SPREAD not in report.candidates[0].metrics

    def test_frame_footnote_warns_about_the_shared_local_context(self, report):
        assert any("local context" in w for w in report.warnings)


class TestWindowExactGap:
    """The windowed-vs-exact disagreement, promoted to a first-class number."""

    def test_gap_is_none_without_vienna_exact(self):
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS, tools=["rnaplfold"],
        )
        assert M.WINDOW_EXACT_GAP not in report.candidates[0].metrics

    def test_gap_is_the_exact_minus_windowed_dg_open(self):
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS,
            tools=["rnaplfold", "vienna-exact"],
        )
        candidate = report.candidates[0]
        dg = candidate.consensus[M.DG_OPEN]
        expected = dg.values["vienna-exact"] - dg.values["rnaplfold"]
        assert candidate.metrics[M.WINDOW_EXACT_GAP] == pytest.approx(expected, abs=1e-6)

    def test_large_gap_produces_a_note(self):
        from rnavail.pipeline.run import CandidateReport, _interpret

        candidate = CandidateReport(
            region=Region(1, 20), subsequence="A" * 20,
            metrics={M.WINDOW_EXACT_GAP: 3.3},
        )
        notes = _interpret(candidate)
        assert any("3.3 kcal/mol lower" in n for n in notes)

    def test_negative_gap_names_the_opposite_direction(self):
        from rnavail.pipeline.run import CandidateReport, _interpret

        candidate = CandidateReport(
            region=Region(1, 20), subsequence="A" * 20,
            metrics={M.WINDOW_EXACT_GAP: -2.0},
        )
        notes = _interpret(candidate)
        assert any("2.0 kcal/mol higher" in n for n in notes)


class TestDiagnoseRun:
    """Report-wide checks that need every candidate scored first."""

    def test_flags_a_saturated_criterion(self):
        from rnavail.pipeline.run import CandidateReport, _diagnose_run, Report
        from rnavail.pipeline.score import Criterion, score_candidate

        criteria = (
            Criterion(key=M.P_UNPAIRED, weight=1.0,
                      desirability=lambda v: 1.0, label="always saturated"),
        )
        report = Report(sequence=TARGET, settings=SETTINGS, mode="evaluate")
        for i in range(4):
            metrics = {M.P_UNPAIRED: 0.5}
            report.candidates.append(CandidateReport(
                region=Region(1 + i, 10 + i), subsequence="A" * 10,
                metrics=metrics, score=score_candidate(metrics, criteria),
            ))
        _diagnose_run(report, criteria)
        assert any("not discriminating" in w for w in report.warnings)
        assert report.detail["score_saturation"][M.P_UNPAIRED]["n_saturated"] == 4

    def test_does_not_flag_a_discriminating_criterion(self):
        from rnavail.pipeline.run import CandidateReport, _diagnose_run, Report
        from rnavail.pipeline.score import Criterion, score_candidate

        criteria = (
            Criterion(key=M.DG_OPEN_PER_NT, weight=1.0,
                      desirability=lambda v: v, label="varies"),
        )
        report = Report(sequence=TARGET, settings=SETTINGS, mode="evaluate")
        for value in (0.1, 0.3, 0.5, 0.7, 0.9):
            metrics = {M.DG_OPEN_PER_NT: value}
            report.candidates.append(CandidateReport(
                region=Region(1, 10), subsequence="A" * 10,
                metrics=metrics, score=score_candidate(metrics, criteria),
            ))
        _diagnose_run(report, criteria)
        assert not any("not discriminating" in w for w in report.warnings)

    def test_flags_a_candidate_scored_by_fewer_independent_tools(self):
        from rnavail.pipeline.run import CandidateReport, _diagnose_run, Report
        from rnavail.pipeline.score import Consensus, score_candidate

        report = Report(sequence=TARGET, settings=SETTINGS, mode="evaluate")

        full = Consensus(metric=M.P_UNPAIRED,
                          values={"rnaplfold": 0.05, "vienna-exact": 0.04},
                          groups={"rnaplfold": "rnaplfold", "vienna-exact": "vienna-exact"})
        partial = Consensus(metric=M.P_UNPAIRED, values={"rnaplfold": 0.05},
                             groups={"rnaplfold": "rnaplfold"})

        rich = CandidateReport(region=Region(1, 20), subsequence="A" * 20,
                                metrics={}, consensus={M.P_UNPAIRED: full},
                                score=score_candidate({}, ()))
        thin = CandidateReport(region=Region(30, 49), subsequence="A" * 20,
                                metrics={}, consensus={M.P_UNPAIRED: partial},
                                score=score_candidate({}, ()))
        report.candidates = [rich, thin]

        _diagnose_run(report, ())
        assert not any("independent measurements" in n for n in rich.notes)
        assert any("independent measurements" in n for n in thin.notes)
        assert "vienna-exact" in thin.notes[0]


class TestAccessibilityProfile:
    """The whole-transcript, single-nucleotide-resolution profile."""

    @staticmethod
    @pytest.fixture(scope="class")
    def report():
        return scan(
            TARGET, window=12, step=5, settings=SETTINGS, keep=2,
            tools=["rnaplfold"], seed_length=8,
        )

    def test_profile_has_one_entry_per_position_regardless_of_step(self, report):
        # step=5 tiled candidates coarsely; the profile must still be dense.
        expected_positions = len(TARGET) - 12 + 1
        assert len(report.detail["profile"]) == expected_positions

    def test_profile_window_matches_the_scan_window(self, report):
        assert report.detail["profile_window"] == 12

    def test_raw_table_is_kept_for_rendering_but_not_serialised(self, report):
        assert report.profile_table is not None
        payload = report.to_dict()
        assert "profile_table" not in payload

    def test_profile_agrees_with_the_screened_windows(self, report):
        """The profile at a position the screen also tiled must match the
        screening tool's own number for that same window -- same table,
        just read at every position instead of only the tiled ones.
        """
        screen_result = report.tool_results[0]
        for key, metrics in screen_result.regions.items():
            start = int(key.split("-")[0])
            expected = metrics.get(M.DG_OPEN_PER_NT)
            if expected is None:
                continue
            assert report.detail["profile"][str(start)] == pytest.approx(
                expected, rel=1e-6
            )

    def test_profile_tsv_has_a_row_per_position(self, report, tmp_path):
        path = tmp_path / "profile.tsv"
        text = to_profile_tsv(report, path)
        lines = text.strip().splitlines()
        assert lines[0] == "start\tend\tdg_open_per_nt_window12"
        assert len(lines) - 1 == len(report.detail["profile"])
        assert path.exists()

    def test_profile_tsv_is_none_for_evaluate(self):
        report = evaluate(TARGET, [Region(9, 20)], settings=SETTINGS,
                          tools=["rnaplfold"])
        assert to_profile_tsv(report) is None


class TestIO:
    def test_reads_multi_record_fasta(self, tmp_path):
        path = tmp_path / "s.fa"
        path.write_text(">a desc here\nGGGAAA\nCCC\n>b\nUUUU\n")
        records = read_fasta(path)
        assert len(records) == 2
        assert records[0].seq == "GGGAAACCC"
        assert records[0].description == "desc here"

    def test_literal_sequence_is_accepted(self):
        assert read_sequence("GGGAAACCC").seq == "GGGAAACCC"

    def test_multi_record_target_requires_explicit_selection(self, tmp_path):
        path = tmp_path / "many.fa"
        path.write_text(">a\nGGG\n>b\nAAA\n")
        with pytest.raises(Exception, match="--record"):
            read_sequence(path)
        assert read_sequence(path, record="b").seq == "AAA"

    def test_probing_missing_values_stay_missing(self, tmp_path):
        path = tmp_path / "r.shape"
        path.write_text("1\t0.5\n2\tNA\n3\t-999\n4\t1.2\n")
        data = read_probing(path, length=4)
        assert data.reactivities == (0.5, None, None, 1.2)
        assert data.coverage == 0.5

    def test_probing_accepts_three_columns(self, tmp_path):
        path = tmp_path / "r.shape"
        path.write_text("1\tG\t0.5\n2\tG\t0.9\n")
        assert read_probing(path, length=2).reactivities == (0.5, 0.9)

    def test_probing_conversion_parameters_are_preserved(self, tmp_path):
        path = tmp_path / "r.shape"
        path.write_text("1\t0.5\n")
        data = read_probing(
            path, length=1, method="zarringhalam", slope=2.1,
            intercept=-0.4, beta=0.75,
        )
        assert (data.slope, data.intercept, data.beta) == (2.1, -0.4, 0.75)

    def test_probing_base_mismatch_and_duplicate_are_rejected(self, tmp_path):
        mismatch = tmp_path / "mismatch.shape"
        mismatch.write_text("1\tA\t0.5\n")
        with pytest.raises(Exception, match="does not match"):
            read_probing(mismatch, Sequence("s", "G"))
        duplicate = tmp_path / "duplicate.shape"
        duplicate.write_text("1\t0.5\n1\t0.7\n")
        with pytest.raises(Exception, match="duplicate"):
            read_probing(duplicate, length=2)

    def test_probing_beyond_the_sequence_is_rejected(self, tmp_path):
        path = tmp_path / "r.shape"
        path.write_text("1\t0.5\n99\t0.5\n")
        with pytest.raises(Exception, match="only 4 nt"):
            read_probing(path, length=4)


class TestCLI:
    def test_tools_command_lists_adapters(self, capsys):
        from rnavail.cli import main
        assert main(["tools"]) == 0
        assert "adapters available" in capsys.readouterr().out

    def test_tools_json_is_parseable(self, capsys):
        from rnavail.cli import main
        main(["tools", "--json"])
        rows = json.loads(capsys.readouterr().out)
        assert all("name" in row and "available" in row for row in rows)

    def test_evaluate_end_to_end(self, capsys, tmp_path):
        from rnavail.cli import main
        out = tmp_path / "r.json"
        code = main([
            "evaluate", TARGET.seq, "--region", "9-20", "--region", "38-50",
            "--tools", "rnaplfold,vienna-exact", "--seed-length", "8",
            "--max-bp-span", "60", "--window-size", "67",
            "--json", str(out), "-q",
        ])
        assert code == 0
        payload = json.loads(out.read_text())
        assert len(payload["candidates"]) == 2

    def test_scan_end_to_end(self, tmp_path):
        from rnavail.cli import main
        out = tmp_path / "r.tsv"
        code = main([
            "scan", TARGET.seq, "--window", "12", "--step", "4", "--keep", "3",
            "--tools", "rnaplfold", "--seed-length", "8",
            "--max-bp-span", "60", "--window-size", "67",
            "--tsv", str(out), "-q",
        ])
        assert code == 0
        assert len(out.read_text().strip().splitlines()) == 4

    def test_bad_region_exits_cleanly(self, capsys):
        from rnavail.cli import main
        assert main(["evaluate", TARGET.seq, "--region", "not-a-region",
                     "--tools", "rnaplfold", "-q"]) == 2

    def test_ribosnitch_and_context_robustness_flags_end_to_end(self, tmp_path):
        from rnavail.cli import main
        out = tmp_path / "r.json"
        code = main([
            "evaluate", TARGET.seq, "--region", "9-12",
            "--tools", "rnaplfold", "--seed-length", "4",
            "--max-bp-span", "60", "--window-size", "67",
            "--ribosnitch", "--context-robustness",
            "--json", str(out), "-q",
        ])
        assert code == 0
        metrics = json.loads(out.read_text())["candidates"][0]["metrics"]
        assert M.RIBOSNITCH_SPREAD in metrics
        assert M.CONTEXT_DG_SPREAD in metrics

    def test_gquad_with_a_windowed_engine_fails_the_tool_not_the_process(self):
        """Regression test: ViennaRNA segfaults combining gquad with
        OPTION_WINDOW rather than raising. rnaplfold must degrade to a
        failed-tool row instead of crashing the interpreter (exit 0)."""
        from rnavail.cli import main
        assert main([
            "evaluate", TARGET.seq, "--region", "9-20", "--gquad",
            "--tools", "rnaplfold", "--max-bp-span", "60",
            "--window-size", "67", "-q",
        ]) == 0

    def test_length_robustness_flag_end_to_end(self, tmp_path):
        from rnavail.cli import main
        out = tmp_path / "r.json"
        code = main([
            "evaluate", TARGET.seq, "--region", "9-20",
            "--tools", "rnaplfold", "--seed-length", "8",
            "--max-bp-span", "60", "--window-size", "67",
            "--length-robustness", "--json", str(out), "-q",
        ])
        assert code == 0
        metrics = json.loads(out.read_text())["candidates"][0]["metrics"]
        assert M.WINDOW_LENGTH_SPREAD in metrics

    def test_profile_tsv_flag_writes_a_per_position_file(self, tmp_path):
        from rnavail.cli import main
        out = tmp_path / "profile.tsv"
        code = main([
            "scan", TARGET.seq, "--window", "12", "--step", "5", "--keep", "2",
            "--tools", "rnaplfold", "--seed-length", "8",
            "--max-bp-span", "60", "--window-size", "67",
            "--profile-tsv", str(out), "-q",
        ])
        assert code == 0
        lines = out.read_text().strip().splitlines()
        assert lines[0].startswith("start\tend\tdg_open_per_nt")
        assert len(lines) > 1

    def test_profile_tsv_is_not_written_for_evaluate(self):
        """--profile-tsv is a scan-only flag; evaluate's parser has no such
        argument at all."""
        from rnavail.cli import build_parser
        with pytest.raises(SystemExit):
            build_parser().parse_args([
                "evaluate", TARGET.seq, "--region", "9-20",
                "--profile-tsv", "x.tsv",
            ])


class TestDemoRecovery:
    """End-to-end: the scan must find a site engineered to be accessible.

    examples/demo_target.fa contains a deliberately unstructured A/U/C loop at
    196-230 and a GC-rich hairpin around 117-136. Any change that breaks the
    ranking logic shows up here as the wrong window winning.
    """

    @staticmethod
    @pytest.fixture(scope="class")
    def report():
        from rnavail.pipeline.run import scan
        target = read_fasta("examples/demo_target.fa")[0]
        return scan(
            target, window=20, step=2, keep=6,
            settings=ModelSettings(max_bp_span=120, window_size=160),
            seed_length=8,
        )

    def test_top_hit_is_the_engineered_accessible_loop(self, report):
        best = report.ranked()[0]
        assert 196 <= best.region.start <= 230
        assert best.metrics[M.P_UNPAIRED] > 0.5
        assert best.metrics[M.DG_OPEN] < 1.0

    def test_gc_hairpin_ranks_last(self, report):
        worst = report.ranked()[-1]
        assert worst.metrics[M.DG_OPEN_PER_NT] > 0.3

    def test_shortlisted_windows_do_not_overlap(self, report):
        regions = sorted((c.region for c in report.candidates),
                         key=lambda r: r.start)
        for earlier, later in zip(regions, regions[1:]):
            assert not earlier.overlaps(later)

    def test_screening_pass_is_recorded(self, report):
        assert report.detail["windows_screened"] > 100
        assert report.tool_results[0].tool == "rnaplfold"


class TestReproducibility:
    def test_repeated_runs_give_identical_numbers(self):
        """The sampling adapter is seeded, so a rerun must not drift."""
        def run():
            return evaluate(
                TARGET, [Region(9, 20)], settings=SETTINGS,
                tools=["ensemble-sample"], seed_length=8,
                options={"samples": 400},
            ).candidates[0].metrics

        assert run() == run()

    def test_a_different_seed_draws_a_different_ensemble(self):
        def run(seed):
            return evaluate(
                TARGET, [Region(9, 20)], settings=SETTINGS,
                tools=["ensemble-sample"], seed_length=8,
                options={"samples": 400, "sampling_seed": seed},
            ).candidates[0].metrics[M.MEAN_BASE_UNPAIRED]

        assert run(1) != run(999)


class TestRunTracking:
    def test_save_run_creates_a_timestamped_directory(self, tmp_path):
        from rnavail.cli import main
        base = tmp_path / "runs"
        code = main([
            "evaluate", TARGET.seq, "--region", "9-20",
            "--tools", "rnaplfold", "--max-bp-span", "60", "--window-size", "67",
            "--save-run", str(base), "-q",
        ])
        assert code == 0
        run_dirs = [p for p in base.iterdir() if p.is_dir() and p.name != "latest"]
        assert len(run_dirs) == 1
        run_dir = run_dirs[0]
        assert (run_dir / "report.json").is_file()
        assert (run_dir / "report.tsv").is_file()
        assert (run_dir / "report.txt").is_file()
        assert (run_dir / "meta.json").is_file()

    def test_latest_points_at_the_most_recent_run(self, tmp_path):
        from rnavail.cli import main
        base = tmp_path / "runs"
        for _ in range(2):
            main([
                "evaluate", TARGET.seq, "--region", "9-20",
                "--tools", "rnaplfold", "--max-bp-span", "60",
                "--window-size", "67", "--save-run", str(base), "-q",
            ])
        latest = base / "latest"
        assert latest.is_symlink()
        run_dirs = sorted(p.name for p in base.iterdir() if p.name != "latest")
        assert latest.readlink().name == run_dirs[-1] or \
            str(latest.resolve().name) == run_dirs[-1]

    def test_meta_records_inputs_and_outcome(self, tmp_path):
        from rnavail.cli import main
        base = tmp_path / "runs"
        main([
            "evaluate", TARGET.seq, "--region", "9-20", "--region", "20-32",
            "--tools", "rnaplfold", "--max-bp-span", "60", "--window-size", "67",
            "--save-run", str(base), "-q",
        ])
        meta = json.loads((base / "latest" / "meta.json").read_text())
        assert meta["mode"] == "evaluate"
        assert meta["n_candidates"] == 2
        assert meta["tools_ran"] == ["rnaplfold"]
        assert meta["sequence"]["length"] == len(TARGET)
        assert isinstance(meta["duration_s"], float)
        assert meta["duration_human"]
        report_json = json.loads((base / "latest" / "report.json").read_text())
        assert report_json["detail"]["duration_human"]
        assert "elapsed runtime:" in (base / "latest" / "report.txt").read_text()
        assert len(meta["top_candidates"]) == 2

    def test_repeated_runs_do_not_overwrite_each_other(self, tmp_path):
        from rnavail.cli import main
        base = tmp_path / "runs"
        for region in ("9-20", "20-32"):
            main([
                "evaluate", TARGET.seq, "--region", region,
                "--tools", "rnaplfold", "--max-bp-span", "60",
                "--window-size", "67", "--save-run", str(base), "-q",
            ])
        run_dirs = [p for p in base.iterdir() if p.name != "latest"]
        assert len(run_dirs) == 2
        regions_seen = {
            json.loads((d / "meta.json").read_text())["n_candidates"]
            for d in run_dirs
        }
        assert regions_seen == {1}

    def test_save_run_is_off_by_default(self, tmp_path):
        from rnavail.cli import main
        import os
        cwd = os.getcwd()
        os.chdir(tmp_path)
        try:
            main([
                "evaluate", TARGET.seq, "--region", "9-20",
                "--tools", "rnaplfold", "--max-bp-span", "60",
                "--window-size", "67", "-q",
            ])
            assert not (tmp_path / "runs").exists()
        finally:
            os.chdir(cwd)


class TestRecognitionAndConditionSemantics:
    def test_seed_modes_restrict_candidate_seed_starts(self):
        sequence = Sequence("s", "A" * 30)
        region = Region(10, 20)
        settings = ModelSettings()
        five = AccessibilityRequest(
            sequence, [region], settings, seed_length=4,
            recognition=RecognitionSpec(seed_mode="five_prime", seed_lengths=(4,)),
        )
        three = AccessibilityRequest(
            sequence, [region], settings, seed_length=4,
            recognition=RecognitionSpec(seed_mode="three_prime", seed_lengths=(4,)),
        )
        fixed = AccessibilityRequest(
            sequence, [region], settings, seed_length=4,
            recognition=RecognitionSpec(
                seed_mode="fixed", seed_start=13, seed_lengths=(4,)
            ),
        )
        assert five.seed_starts(region) == [10]
        assert three.seed_starts(region) == [17]
        assert fixed.seed_starts(region) == [13]

    def test_invalid_fixed_seed_and_seed_length_mismatch_fail_before_tools_run(self):
        sequence = Sequence("s", "A" * 30)
        region = Region(10, 20)
        with pytest.raises(ValueError, match="does not fit"):
            AccessibilityRequest(
                sequence, [region], ModelSettings(), seed_length=4,
                recognition=RecognitionSpec(
                    seed_mode="fixed", seed_start=21, seed_lengths=(4,)
                ),
            )
        with pytest.raises(ValueError, match="one seed length"):
            AccessibilityRequest(
                sequence, [region], ModelSettings(), seed_length=4,
                recognition=RecognitionSpec(seed_lengths=(6,)),
            )

    def test_listed_seed_without_a_placement_fails_before_tools_run(self):
        sequence = Sequence("s", "A" * 30)
        with pytest.raises(ValueError, match="does not fit"):
            AccessibilityRequest(
                sequence, [Region(10, 20)], ModelSettings(), seed_length=4,
                recognition=RecognitionSpec(
                    seed_mode="listed", listed_seed_starts=(2, 25),
                    seed_lengths=(4,),
                ),
            )

    def test_condition_temperature_must_match_model_temperature(self):
        with pytest.raises(ValueError, match="must match"):
            evaluate(
                TARGET, [Region(9, 20)], settings=SETTINGS,
                condition=ConditionSpec(temperature_c=25.0), tools=["rnaplfold"],
            )

    def test_condition_sodium_must_match_model_salt(self):
        with pytest.raises(ValueError, match="sodium_molar"):
            evaluate(
                TARGET, [Region(9, 20)],
                settings=ModelSettings(max_bp_span=60, window_size=67, salt_molar=0.1),
                condition=ConditionSpec(temperature_c=37.0, sodium_molar=0.2),
                tools=["rnaplfold"],
            )

    def test_scan_filters_fixed_and_listed_seed_events_before_screening(self):
        fixed = scan(
            TARGET, window=12, step=1, settings=SETTINGS, keep=2,
            tools=["rnaplfold"], seed_length=4,
            recognition=RecognitionSpec(
                seed_mode="fixed", seed_start=9, seed_lengths=(4,),
            ),
        )
        assert fixed.detail["windows_excluded_by_recognition"] > 0
        assert fixed.candidates
        assert all(9 <= candidate.region.end - 4 + 1 for candidate in fixed.candidates)
        assert all(candidate.region.start <= 9 for candidate in fixed.candidates)

        listed = scan(
            TARGET, window=12, step=1, settings=SETTINGS, keep=2,
            tools=["rnaplfold"], seed_length=4,
            recognition=RecognitionSpec(
                seed_mode="listed", listed_seed_starts=(9, 35), seed_lengths=(4,),
            ),
        )
        assert listed.candidates
        assert not listed.detail.get("screening_failure")

    def test_shortlist_uses_opening_cost_when_seed_nucleation_is_unsupported(self):
        from rnavail.pipeline.run import _shortlist

        seed_favored = Region(1, 4)
        opening_favored = Region(10, 13)
        result = ToolResult(tool="screen", tier=Tier.ACCESSIBILITY)
        result.region_metrics(seed_favored).set(M.SEED_P_UNPAIRED, 0.99)
        result.region_metrics(seed_favored).set(M.DG_OPEN_PER_NT, 0.9)
        result.region_metrics(opening_favored).set(M.SEED_P_UNPAIRED, 0.01)
        result.region_metrics(opening_favored).set(M.DG_OPEN_PER_NT, 0.1)

        assert _shortlist(
            result, [seed_favored, opening_favored], keep=1, use_seed=True,
        ) == [seed_favored]
        assert _shortlist(
            result, [seed_favored, opening_favored], keep=1, use_seed=False,
        ) == [opening_favored]

    def test_noncomplementary_binder_excludes_seed_from_candidate_rank(self):
        recognition = RecognitionSpec(
            binder_class="protein", seed_lengths=(8,),
        )
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS, seed_length=8,
            recognition=recognition, tools=["rnaplfold"],
        )
        candidate = report.candidates[0]

        assert report.detail["recognition_scoring"] == {
            "seed_nucleation_status": "not_applicable",
            "seed_metrics": "diagnostic_only",
            "shortlist_order": "opening_cost_only",
            "active_criteria": [
                M.DG_OPEN_PER_NT, M.DG_OPEN_SPREAD,
                M.WINDOW_LENGTH_SPREAD,
            ],
            "excluded_criteria": [M.SEED_P_UNPAIRED],
        }
        assert "seed_nucleation_ranking" in report.detail["unsupported_assumptions"]
        assert any("not a binding-affinity prediction" in w for w in report.warnings)
        assert M.SEED_P_UNPAIRED not in candidate.metrics
        assert M.SEED_P_UNPAIRED in candidate.consensus
        assert all(
            component.criterion.key != M.SEED_P_UNPAIRED
            for component in candidate.score.components
        )
        assert candidate.detail["seed_nucleation"]["status"] == "not_applicable"
        assert any("not used because" in note for note in candidate.notes)

    def test_complementary_binder_keeps_seed_scoring(self):
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS, seed_length=8,
            recognition=RecognitionSpec(
                binder_class="dna_probe", seed_lengths=(8,),
            ),
            tools=["rnaplfold"],
        )
        candidate = report.candidates[0]

        assert report.detail["recognition_scoring"]["seed_nucleation_status"] == \
            "complementary"
        assert report.detail["recognition_scoring"]["seed_metrics"] == "ranked"
        assert M.SEED_P_UNPAIRED in candidate.metrics
        assert any(
            component.criterion.key == M.SEED_P_UNPAIRED
            for component in candidate.score.components
        )

    def test_noncomplementary_fixed_seed_does_not_filter_scan_windows(self):
        report = scan(
            TARGET, window=12, step=10, settings=SETTINGS, keep=2,
            tools=["rnaplfold"], seed_length=4,
            recognition=RecognitionSpec(
                binder_class="small_molecule", seed_mode="fixed",
                seed_start=999, seed_lengths=(4,),
            ),
        )
        assert report.detail["windows_screened"] == report.detail["windows_tiled"]
        assert "windows_excluded_by_recognition" not in report.detail
        assert report.candidates

    def test_probing_must_match_target_and_declared_condition(self):
        bad_hash = ProbingData((0.0,) * len(TARGET), sequence_hash="wrong")
        with pytest.raises(ValueError, match="sequence_hash"):
            evaluate(TARGET, [Region(9, 20)], settings=SETTINGS,
                     probing=bad_hash, tools=["rnaplfold"])
        mismatched_condition = ProbingData(
            (0.0,) * len(TARGET), condition_id="assay-A"
        )
        with pytest.raises(ValueError, match="condition_id"):
            evaluate(
                TARGET, [Region(9, 20)], settings=SETTINGS,
                probing=mismatched_condition,
                condition=ConditionSpec(condition_id="assay-B", temperature_c=37.0),
                tools=["rnaplfold"],
            )


class TestOpeningObservationSemantics:
    def test_primary_observation_keeps_probability_and_energy_consistent(self):
        settings = ModelSettings(
            max_bp_span=60, global_max_bp_span=60, window_size=67
        )
        report = evaluate(
            TARGET, [Region(9, 20)], settings=settings,
            tools=["rnaplfold", "vienna-exact"], seed_length=8,
        )
        candidate = report.candidates[0]
        primary = next(
            observation for observation in candidate.opening_observations
            if observation.observation_id == candidate.primary_opening_observation_id
        )
        assert primary.tool == "vienna-exact"
        assert candidate.metrics[M.P_UNPAIRED] == pytest.approx(
            math.exp(-candidate.metrics[M.DG_OPEN] / (0.0019872041 * 310.15))
        )
        assert candidate.metrics[M.SEED_START] == primary.seed_start

    def test_schema_and_conditioned_profile_preserve_provenance(self):
        probing = ProbingData((0.0,) * len(TARGET))
        report = scan(
            TARGET, window=12, step=4, settings=SETTINGS, probing=probing,
            tools=["rnaplfold"], keep=2, seed_length=8,
        )
        payload = report.to_dict()
        assert payload["report_schema_version"] == "2.0"
        assert payload["recognition_spec_id"].startswith("recognition:")
        assert payload["detail"]["probing"]["coverage"] == 1.0
        assert report.tool_results[0].conditioning["conditioning_id"] == \
            probing.conditioning_id()
        for candidate in payload["candidates"]:
            assert any(
                observation["observation_id"] == candidate["primary_opening_observation_id"]
                for observation in candidate["opening_observations"]
            )

    def test_sequence_only_gquad_diagnostic_survives_probing(self):
        sequence = Sequence("g4", "GGGUUAGGGUUAGGGUUAGGG" * 2)
        report = evaluate(
            sequence, [Region(1, len(sequence))], probing=ProbingData((0.0,) * len(sequence)),
            tools=["gquad-scan"],
        )
        assert report.candidates[0].metrics[M.GQUAD_SCORE] >= 1.2
        assert report.tool_results[0].conditioning["status"] == "not_applicable"

    def test_inverse_probability_underflow_is_censored_not_emitted_as_zero(self):
        from rnavail.pipeline.run import _opening_observations

        region = Region(1, 2)
        result = ToolResult(
            tool="synthetic", tier=Tier.ACCESSIBILITY,
            settings={"temperature_c": 37.0},
        )
        result.region_metrics(region).set(M.DG_OPEN, 1000.0)
        observation = _opening_observations([result], region)[0]
        assert observation.estimate_kind == "point"
        assert observation.p_unpaired is None
        assert observation.p_upper_bound is not None
        assert observation.censor_reason is not None

    def test_backend_zero_is_censored_without_claiming_an_exact_bound(self):
        from rnavail.pipeline.run import _opening_observations

        region = Region(1, 2)
        result = ToolResult(tool="synthetic", tier=Tier.ACCESSIBILITY)
        result.region_metrics(region).set(M.P_UNPAIRED, 0.0)
        observation = _opening_observations([result], region)[0]
        assert observation.estimate_kind == "censored"
        assert observation.p_upper_bound is None

    def test_zero_or_underflowed_seed_never_serializes_an_infinite_energy(self):
        from rnavail.pipeline.run import _opening_observations

        region = Region(1, 2)
        result = ToolResult(tool="synthetic", tier=Tier.ACCESSIBILITY)
        metrics = result.region_metrics(region)
        metrics.set(M.P_UNPAIRED, 0.5)
        metrics.set(M.SEED_P_UNPAIRED, 0.0)
        zero_seed = _opening_observations([result], region)[0]
        assert zero_seed.seed_p_unpaired is None
        assert zero_seed.seed_dg_open_kcal_mol is None
        assert "zero seed probability" in zero_seed.censor_reason
        json.dumps(zero_seed.to_dict(), allow_nan=False)

        metrics.values.pop(M.SEED_P_UNPAIRED)
        metrics.set(M.SEED_DG_OPEN, 1000.0)
        underflowed_seed = _opening_observations([result], region)[0]
        assert underflowed_seed.seed_p_unpaired is None
        assert underflowed_seed.seed_dg_open_kcal_mol == 1000.0
        assert "seed inverse probability conversion underflowed" in \
            underflowed_seed.censor_reason
        json.dumps(underflowed_seed.to_dict(), allow_nan=False)

    def test_api_track_without_hash_is_explicitly_unverified(self):
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS,
            probing=ProbingData((0.0,) * len(TARGET)), tools=["rnaplfold"],
        )
        result = report.tool_results[0]
        assert result.conditioning["sequence_identity"] == "unverified"
        assert any("identity is unverified" in warning for warning in result.warnings)


class TestCliProbingSemantics:
    def test_cli_records_probing_conversion_parameters(self, tmp_path):
        from rnavail.cli import main

        track = tmp_path / "track.tsv"
        output = tmp_path / "report.json"
        track.write_text("1\t0.1\n2\t0.2\n")
        assert main([
            "evaluate", "GG", "--region", "1-2", "--tools", "rnaplfold",
            "--shape", str(track), "--shape-slope", "2.1",
            "--shape-intercept", "-0.4", "--shape-beta", "0.75",
            "--json", str(output), "-q",
        ]) == 0
        conversion = json.loads(output.read_text())["probing"]["conversion"]
        assert conversion == {
            "explicit": False, "slope": 2.1, "intercept": -0.4, "beta": 0.75,
        }

    def test_dms_requires_an_explicit_conversion(self, tmp_path):
        from rnavail.cli import main
        track = tmp_path / "track.tsv"
        track.write_text("1\t0.1\n2\t0.2\n")
        assert main([
            "evaluate", "GG", "--region", "1-2", "--tools", "rnaplfold",
            "--shape", str(track), "--probing-chemistry", "DMS", "-q",
        ]) == 2

    def test_cli_adapter_refuses_api_dms_track_without_conversion(self):
        from rnavail.adapters.registry import get

        adapter = get("rnaplfold-cli")
        if not adapter.availability().available:
            pytest.skip("RNAplfold CLI is not installed")
        result = adapter.run_accessibility(AccessibilityRequest(
            Sequence("dms", "GGGAAACCC"), [Region(1, 4)], ModelSettings(),
            probing=ProbingData(
                (0.1,) * 9, chemistry="DMS", conversion_explicit=False,
            ),
        ))
        assert result.status == "failed"
        assert "explicitly selected conversion" in result.error
