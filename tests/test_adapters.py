"""Adapter behaviour, parsers, and the cross-tool agreement that matters.

The scientific tests here are the ones that would catch a real regression:
independent engines computing the same physical quantity must agree, and the
joint accessibility must never collapse into the mean of per-base values.

Every adapter tested here answers a single-molecule question — is this region
unpaired within its own folded structure. None of them predict binding to
another RNA; that capability was deliberately removed from this tool.
"""

import math

import pytest

from rnavail.adapters.base import AccessibilityRequest
from rnavail.adapters.registry import all_adapters, get, select
from rnavail.core.model import ModelSettings, ProbingData
from rnavail.core.result import M, Tier, ToolResult
from rnavail.core.sequence import Region, Sequence

# A hairpin-rich test molecule: 9-20 sits in a loose region, 20-32 inside a
# strong GC hairpin, 38-50 in a moderately paired stretch.
TARGET = Sequence(
    "target",
    "GGGAAACCCAUAUAUAUAUGCGCGCUUUUUUGCGCGCAAAGGGAAACCCUUAAGGUUCCAAGGUUCC",
)
SETTINGS = ModelSettings(max_bp_span=60, window_size=67)
REGIONS = [Region(9, 20), Region(20, 32), Region(38, 50)]


def access_request(**kwargs):
    params = dict(sequence=TARGET, regions=REGIONS, settings=SETTINGS,
                  seed_length=8)
    params.update(kwargs)
    return AccessibilityRequest(**params)


def available(name):
    adapter = get(name)
    if not adapter.availability().available:
        pytest.skip(f"{name} is not installed in this environment")
    return adapter


class TestRegistry:
    def test_every_adapter_declares_a_name_tier_and_handles_accessibility(self):
        for adapter in all_adapters():
            assert adapter.name and adapter.description
            assert isinstance(adapter.tier, Tier)
            assert adapter.handles_accessibility

    def test_names_are_unique(self):
        names = [a.name for a in all_adapters()]
        assert len(names) == len(set(names))

    def test_max_cost_filters_by_cost(self):
        low_cost_only = {a.name for a in select(max_cost=1)}
        everything = {a.name for a in select(max_cost=None)}
        assert low_cost_only <= everything
        assert "rnaplfold" in low_cost_only  # cost 1

    def test_unknown_adapter_raises(self):
        with pytest.raises(KeyError, match="unknown adapter"):
            get("does-not-exist")


class TestGracefulDegradation:
    def test_missing_tool_is_skipped_not_raised(self):
        """A tool that cannot run must cost the report one row, not the run.

        Exercised with a stub adapter rather than a real one, so this test
        does not depend on any particular external tool being absent.
        """
        from rnavail.adapters.base import AccessibilityAdapter
        from rnavail.core.result import Availability, Tier

        class StubUnavailable(AccessibilityAdapter):
            name = "stub-unavailable"
            tier = Tier.ACCESSIBILITY
            description = "test stub"

            def availability(self):
                return Availability.no("stub tool not installed", hint="n/a")

            def compute_accessibility(self, request):
                raise AssertionError("must not be called when unavailable")

        result = StubUnavailable().run_accessibility(access_request())
        assert result.status == "skipped"
        assert "stub tool not installed" in result.error.lower()

    def test_internal_failure_is_captured_as_failed(self):
        """An adapter error must land in the report, not abort the run."""
        adapter = available("rnaplfold")
        # A parameter set no ViennaRNA build provides. Built on its own
        # instance rather than the shared SETTINGS, because these objects are
        # frozen precisely so that one test cannot poison another.
        broken = ModelSettings(max_bp_span=60, window_size=67)
        object.__setattr__(broken, "param_set", "not_a_real_set")
        result = adapter.run_accessibility(access_request(settings=broken))
        assert result.status == "failed"
        assert result.error

    def test_out_of_range_positions_raise_instead_of_crashing(self):
        """ViennaRNA's hc_add_up segfaults on a bad index; we must not reach it."""
        from rnavail.adapters._vienna import constrained_free_energy
        with pytest.raises(ValueError, match="outside the sequence"):
            constrained_free_energy("GGGAAACCC", SETTINGS, [1, 2, 10_000])

    def test_request_rejects_regions_past_the_end(self):
        with pytest.raises(ValueError, match="exceeds sequence"):
            AccessibilityRequest(
                sequence=TARGET, regions=[Region(1, 10_000)], settings=SETTINGS
            )


class TestAccessibilityAgreement:
    """Independent engines must agree on the same physical quantity."""

    def test_exact_and_local_engines_agree_on_opening_energy(self):
        matched = ModelSettings(
            max_bp_span=60, global_max_bp_span=60, window_size=67
        )
        exact = available("vienna-exact").run_accessibility(
            access_request(settings=matched)
        )
        local = available("rnaplfold").run_accessibility(
            access_request(settings=matched)
        )
        assert exact.ok and local.ok
        for region in REGIONS:
            key = f"{region.start}-{region.end}"
            a = exact.regions[key].get(M.DG_OPEN)
            b = local.regions[key].get(M.DG_OPEN)
            # Same energy model, different recursions: agreement to well under
            # 0.1 kcal/mol is expected, and drift beyond that is a real bug.
            assert abs(a - b) < 0.1, f"{key}: exact {a} vs plfold {b}"

    def test_bindings_and_command_line_agree(self):
        binding = available("rnaplfold").run_accessibility(access_request())
        cli = available("rnaplfold-cli").run_accessibility(access_request())
        for key, metrics in cli.regions.items():
            if M.DG_OPEN in metrics.values:
                assert metrics.values[M.DG_OPEN] == pytest.approx(
                    binding.regions[key].values[M.DG_OPEN], abs=0.01
                )
            # The command-line cross-check must expose the same permitted
            # seed event and its individual placements as the bindings.
            assert metrics.get(M.SEED_P_UNPAIRED) == pytest.approx(
                binding.regions[key].get(M.SEED_P_UNPAIRED), abs=0.01
            )
            assert [trial["start"] for trial in metrics.detail["seed_trials"]] == \
                [trial["start"] for trial in binding.regions[key].detail["seed_trials"]]

    def test_independent_codebases_agree_on_per_base_pairing(self):
        vienna = available("rnafold").run_accessibility(access_request())
        other = available("rnastructure-partition").run_accessibility(
            access_request()
        )
        for region in REGIONS:
            key = f"{region.start}-{region.end}"
            a = vienna.regions[key].get(M.MEAN_BASE_UNPAIRED)
            b = other.regions[key].get(M.MEAN_BASE_UNPAIRED)
            # Different parameter tables, so agreement is looser here.
            assert abs(a - b) < 0.15, f"{key}: ViennaRNA {a} vs RNAstructure {b}"


class TestJointVersusPerBase:
    def test_joint_probability_is_not_the_mean_of_per_base(self):
        """The central correctness claim of the whole pipeline.

        Region 9-20 is individually open most of the time but almost never
        open all at once. Confusing the two is the mistake this tool exists
        to prevent, so it is asserted rather than merely documented.
        """
        result = available("rnaplfold").run_accessibility(access_request())
        metrics = result.regions["9-20"]
        joint = metrics.get(M.P_UNPAIRED)
        mean = metrics.get(M.MEAN_BASE_UNPAIRED)
        assert mean > 0.5
        assert joint < mean / 100

    def test_seed_is_more_available_than_the_full_site(self):
        result = available("rnaplfold").run_accessibility(access_request())
        metrics = result.regions["9-20"]
        assert metrics.get(M.SEED_P_UNPAIRED) > metrics.get(M.P_UNPAIRED)

    def test_local_seed_trials_cover_all_permitted_placements(self):
        region = Region(9, 20)
        result = available("rnaplfold").run_accessibility(
            access_request(regions=[region])
        )
        trials = result.regions[region.label].detail["seed_trials"]
        assert [trial["start"] for trial in trials] == list(range(9, 14))
        assert trials[-1]["end"] == 20
        assert all(
            {"start", "end", "p_unpaired", "dg_open_kcal_mol", "estimate_kind"}
            <= trial.keys()
            for trial in trials
        )
        assert all(trial["estimate_kind"] == "point" for trial in trials)

    def test_structured_site_costs_more_to_open_than_a_loose_one(self):
        result = available("vienna-exact").run_accessibility(access_request())
        hairpin = result.regions["20-32"].get(M.DG_OPEN_PER_NT)
        loose = result.regions["9-20"].get(M.DG_OPEN_PER_NT)
        assert hairpin > loose


class TestScientificSemantics:
    def test_local_accessibility_applies_probing_constraints(self):
        sequence = Sequence("probe", "GGGCGCGCGCAAAAGCGCGCGCCC")
        region = Region(1, 8)
        settings = ModelSettings(max_bp_span=20, window_size=24)
        baseline = available("rnaplfold").run_accessibility(
            AccessibilityRequest(sequence, [region], settings)
        )
        conditioned = available("rnaplfold").run_accessibility(
            AccessibilityRequest(
                sequence, [region], settings,
                probing=ProbingData((10.0,) * len(sequence)),
            )
        )
        assert conditioned.conditioning["status"] == "applied"
        assert conditioned.regions["1-8"].get(M.P_UNPAIRED) > \
            baseline.regions["1-8"].get(M.P_UNPAIRED) * 1e6

    def test_gquad_joint_event_fails_instead_of_counting_g4_as_unpaired(self):
        sequence = Sequence("g4", "GGGAGGGAGGGAGGG")
        result = available("vienna-exact").run_accessibility(
            AccessibilityRequest(
                sequence, [Region(1, len(sequence))],
                ModelSettings(gquad=True),
            )
        )
        assert result.status == "failed"
        assert "G-quadruplexes" in result.error

    def test_mfe_dominance_does_not_trigger_a_diffuse_ensemble_warning(self):
        result = available("rnafold").run_accessibility(
            AccessibilityRequest(
                Sequence("unstructured", "A" * 30), [Region(1, 10)], SETTINGS
            )
        )
        assert not any("substantial ensemble weight" in warning for warning in result.warnings)

    def test_exact_seed_scan_keeps_the_terminal_placement_when_subsampled(self):
        from rnavail.adapters.vienna_exact import ViennaExactAdapter

        region = Region(1, 50)
        starts = list(range(1, 42))
        result = ToolResult(tool="test", tier=Tier.ACCESSIBILITY)
        best = ViennaExactAdapter()._scan_seed(
            region, 10, starts,
            lambda seed: 0.0 if seed.start == 41 else 1.0,
            37.0, result,
        )
        assert best == (41, 0.0)
        scan = result.detail["seed_scans"][region.label]
        assert 41 in scan["tested_starts"]
        assert [trial["start"] for trial in scan["trials"]] == starts
        assert scan["trials"][-1] == {
            "start": 41,
            "end": 50,
            "p_unpaired": 1.0,
            "dg_open_kcal_mol": 0.0,
            "estimate_kind": "point",
        }
        assert any(
            trial["estimate_kind"] == "not_evaluated" for trial in scan["trials"]
        )

    def test_sampled_zero_hit_seed_is_an_upper_bound(self):
        from rnavail.adapters.vienna_sample import ViennaSampleAdapter

        seed = ViennaSampleAdapter._sample_seed(
            [[False] * 8 for _ in range(20)], Region(1, 8), 4, 20,
            [1, 2, 3, 4, 5],
        )
        assert seed is not None
        _, probability, trials = seed
        assert probability is None
        assert all(trial["p_unpaired"] is None for trial in trials)
        assert all(trial["estimate_kind"] == "upper_bound" for trial in trials)
        assert all(trial["p_unpaired_upper_bound"] > 0 for trial in trials)

    def test_global_span_is_distinct_from_the_local_screening_span(self):
        sequence = Sequence("long_range", "GGGGAAAAAAAAAAAAACCCC")
        region = Region(1, 4)
        unrestricted = available("vienna-exact").run_accessibility(
            AccessibilityRequest(
                sequence, [region],
                ModelSettings(max_bp_span=6, window_size=10),
            )
        )
        limited = available("vienna-exact").run_accessibility(
            AccessibilityRequest(
                sequence, [region],
                ModelSettings(
                    max_bp_span=6, global_max_bp_span=6, window_size=10
                ),
            )
        )
        assert unrestricted.regions["1-4"].get(M.P_UNPAIRED) < 0.01
        assert limited.regions["1-4"].get(M.P_UNPAIRED) == pytest.approx(1.0)
        assert unrestricted.applied_protocol["applied"]["global_max_bp_span"] is None


class TestSampling:
    def test_reports_a_bound_rather_than_a_point_estimate_for_rare_events(self):
        adapter = available("ensemble-sample")
        result = adapter.run_accessibility(access_request(options={"samples": 500}))
        metrics = result.regions["20-32"]
        # This site is open roughly once in 10^10 draws; sampling cannot see
        # it, and must say so instead of reporting zero as a probability.
        assert metrics.detail["sampling_limited"] is True
        assert M.P_UNPAIRED not in metrics.values
        assert "p_unpaired_upper_bound" in metrics.detail

    def test_state_populations_sum_to_one(self):
        result = available("ensemble-sample").run_accessibility(
            access_request(options={"samples": 300})
        )
        for metrics in result.regions.values():
            populations = metrics.detail["state_populations"]
            assert sum(populations.values()) == pytest.approx(1.0)


class TestDNA:
    def test_dna_parameters_change_the_energy(self):
        dna = Sequence("t", TARGET.as_dna(), molecule="dna")
        rna_result = available("vienna-exact").run_accessibility(access_request())
        dna_result = available("vienna-exact").run_accessibility(
            access_request(sequence=dna, settings=SETTINGS.for_molecule("dna"))
        )
        assert rna_result.globals[M.ENSEMBLE_FREE_ENERGY] != pytest.approx(
            dna_result.globals[M.ENSEMBLE_FREE_ENERGY], abs=0.5
        )


class TestGQuad:
    """Sequence-based G-quadruplex / i-motif propensity: no binary, no fold."""

    def test_telomeric_repeat_scores_above_the_published_threshold(self):
        from rnavail.adapters.gquad import (
            G4HUNTER_THRESHOLD, g4hunter_track, _window_scores,
        )

        telomere = "GGGUUAGGGUUAGGGUUAGGG" * 2
        track = g4hunter_track(telomere)
        scores = _window_scores(track, min(25, len(telomere)))
        assert max(scores, key=abs) >= G4HUNTER_THRESHOLD

    def test_c_rich_run_scores_negative_for_an_i_motif(self):
        from rnavail.adapters.gquad import g4hunter_track
        track = g4hunter_track("CCCAAACCCAAACCC")
        assert all(v <= 0 for v in track)
        assert any(v < 0 for v in track)

    def test_no_run_scores_zero(self):
        from rnavail.adapters.gquad import g4hunter_track
        assert g4hunter_track("AUAUAUAUAU") == [0.0] * 10

    def test_adapter_is_always_available_and_flags_a_quadruplex_region(self):
        from rnavail.core.result import M as _M

        adapter = available("gquad-scan")
        g4_region = Sequence("g4", "GGGUUAGGGUUAGGGUUAGGG" * 2)
        request = AccessibilityRequest(
            sequence=g4_region,
            regions=[Region(1, len(g4_region))],
            settings=SETTINGS, seed_length=8,
        )
        result = adapter.run_accessibility(request)
        assert result.ok
        metrics = next(iter(result.regions.values()))
        assert metrics.get(_M.GQUAD_SCORE) >= 1.2
        assert metrics.detail["gquad_above_threshold"] is True


class TestProbKnot:
    """Pseudoknot-capable pairing: the one adapter not restricted to nested pairs."""

    def test_nested_pairs_never_flag_as_crossing(self):
        from rnavail.adapters.probknot import _crossing_positions
        # (1,10) and (2,9): fully nested, textbook hairpin.
        partner = [0, 10, 9, 0, 0, 0, 0, 0, 0, 2, 1]
        assert not any(_crossing_positions(partner))

    def test_interleaved_pairs_flag_as_crossing(self):
        from rnavail.adapters.probknot import _crossing_positions
        # (1,6) and (3,8) interleave: the textbook H-type pseudoknot shape.
        partner = [0, 6, 0, 8, 0, 0, 1, 0, 3]
        crossing = _crossing_positions(partner)
        assert crossing[1] and crossing[6] and crossing[3] and crossing[8]
        assert not crossing[2] and not crossing[4] and not crossing[5]

    def test_ct_parser_reads_the_partner_column(self):
        from rnavail.adapters.probknot import _parse_ct
        ct_text = "4 x\n1 G 0 2 4 1\n2 G 1 3 0 2\n3 G 2 4 0 3\n4 C 3 0 1 4\n"
        assert _parse_ct(ct_text, 4) == [0, 4, 0, 0, 1]

    def test_adapter_reports_per_base_pairing(self):
        adapter = available("probknot")
        result = adapter.run_accessibility(access_request())
        for region in REGIONS:
            metrics = result.regions[f"{region.start}-{region.end}"]
            assert 0.0 <= metrics.get(M.PAIRED_FRACTION) <= 1.0
            assert 0.0 <= metrics.get(M.PSEUDOKNOT_PAIRED_FRACTION) <= 1.0


class TestKinwalker:
    """Co-transcriptional folding: does the region get trapped before equilibrium."""

    def test_final_trap_length_is_none_when_region_ends_open(self):
        from rnavail.adapters.kinwalker import _Event, _final_trap_length
        events = [
            _Event("((....))", 8),
            _Event("((....))....", 12),
        ]
        assert _final_trap_length(events, Region(9, 12)) is None

    def test_final_trap_length_finds_the_start_of_the_last_unbroken_run(self):
        from rnavail.adapters.kinwalker import _Event, _final_trap_length
        events = [
            _Event("((....))", 8),           # region not transcribed yet
            _Event("((....))((....))", 16),  # region (9-16) paired
            _Event("((....)).........", 17),  # a refold reopens it transiently
            _Event("((....))((.....))", 18),  # paired again and stays that way
        ]
        # region 9-16 should trap at the LAST event where it becomes paired
        # and never reopens again, i.e. length 18, not the earlier length 16
        # that was subsequently undone.
        assert _final_trap_length(events, Region(9, 16)) == 18

    def test_trajectory_parser_reads_final_structure_and_events(self):
        from rnavail.adapters.kinwalker import _parse_trajectory
        text = (
            "GGGAAACCC\n"
            "(((...))) -1.2\n"
            "TRAJECTORY\n"
            "((....)) -0.2 0.01 3.1 6.4 8 \n"
            "(((...))) -1.2 0.02 6.1 6.4 9 \n"
            "Kinwalker run time:0.01 seconds\n"
        )
        final, events = _parse_trajectory(text, 9)
        assert final == "(((...)))"
        assert [e.length for e in events] == [8, 9]

    def test_adapter_reports_paired_fraction_and_optional_trap_length(self):
        adapter = available("kinwalker")
        result = adapter.run_accessibility(access_request())
        for region in REGIONS:
            metrics = result.regions[f"{region.start}-{region.end}"]
            assert 0.0 <= metrics.get(M.PAIRED_FRACTION) <= 1.0
            trap = metrics.get(M.CO_TX_TRAP_LENGTH)
            assert trap is None or region.start <= trap

    def test_refuses_a_long_sequence_instead_of_hanging(self):
        """kinwalker's runtime explodes well before typical transcript
        lengths (measured superlinear blowup past ~150 nt); the adapter must
        fail fast rather than let a default run hang on a normal-sized
        target. Exercised via a stub-length sequence so the test itself does
        not have to wait out the blowup to prove the guard exists.
        """
        from rnavail.adapters.kinwalker import MAX_PRACTICAL_LENGTH
        adapter = available("kinwalker")
        long_seq = Sequence("long", "A" * (MAX_PRACTICAL_LENGTH + 1))
        request = AccessibilityRequest(
            sequence=long_seq, regions=[Region(1, 10)],
            settings=SETTINGS, seed_length=4,
        )
        result = adapter.run_accessibility(request)
        assert result.status == "failed"
        assert "kinwalker_max_length" in result.error


class TestEternaFold:
    """Same CONTRAfold engine, different trained parameters.

    The whole point of shipping this adapter separately from ``contrafold``
    is that the two count as independent evidence in the consensus. That
    claim rests on two things holding simultaneously: they must be in
    different independence groups (structural, always checked), and the
    ``--params`` flag must actually be taking effect rather than silently
    falling back to CONTRAfold's own default weights (behavioural, needs a
    real run).
    """

    def test_not_grouped_with_contrafold(self):
        contrafold = get("contrafold")
        eternafold = get("eternafold")
        contrafold_group = contrafold.independence_group or contrafold.name
        eternafold_group = eternafold.independence_group or eternafold.name
        assert contrafold_group != eternafold_group

    def test_params_file_is_bundled_and_found(self):
        from rnavail.adapters.eternafold import PARAMS_PATH
        assert PARAMS_PATH.is_file()

    def test_live_posteriors_differ_from_stock_contrafold(self):
        """Guards against --params being silently ignored by a future change."""
        contrafold = available("contrafold").run_accessibility(access_request())
        eternafold = available("eternafold").run_accessibility(access_request())
        assert contrafold.ok and eternafold.ok
        differing = [
            key for key, metrics in eternafold.regions.items()
            if metrics.get(M.MEAN_BASE_UNPAIRED) != pytest.approx(
                contrafold.regions[key].get(M.MEAN_BASE_UNPAIRED), abs=1e-9
            )
        ]
        assert differing, "eternafold produced identical output to contrafold"


class TestParsers:
    def test_lunp_table(self):
        from rnavail.adapters.vienna_plfold import _parse_lunp
        table = _parse_lunp("#unpaired\n#i$\tl=1\t2\n1\t0.5\tNA\n2\t0.4\t0.2\n")
        assert table[1] == [None, 0.5, None]
        assert table[2] == [None, 0.4, 0.2]

    def test_probability_plot_converts_from_neg_log10(self):
        from rnavail.adapters.rnastructure import _parse_probability_plot
        paired = _parse_probability_plot("3\ni\tj\tp\n1\t3\t1.0\n", length=3)
        assert paired[1] == pytest.approx(0.1)
        assert paired[3] == pytest.approx(0.1)
        assert paired[2] == 0.0

    def test_contrafold_posteriors_counts_both_partners(self):
        """Shared by contrafold and eternafold: same posterior text format."""
        from rnavail.adapters._contrafold_family import parse_posteriors
        paired = parse_posteriors("1 G 3:0.6\n", length=3)
        assert paired[1] == pytest.approx(0.6)
        assert paired[3] == pytest.approx(0.6)
