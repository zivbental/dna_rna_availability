"""Coordinates, thermodynamic conversions and sequence handling."""

import math

import pytest

from rnavail.core import thermo
from rnavail.core.model import ModelSettings, ProbingData, RecognitionSpec
from rnavail.core.sequence import (
    Region, Sequence, SequenceError, parse_region, tile_regions,
)


class TestSequence:
    def test_normalises_case_whitespace_and_thymine(self):
        seq = Sequence("s", "gg ac\ntt")
        assert seq.seq == "GGACUU"

    def test_dna_round_trip(self):
        assert Sequence("s", "GGACTT", molecule="dna").as_dna() == "GGACTT"

    def test_rejects_non_iupac(self):
        with pytest.raises(SequenceError, match="non-IUPAC"):
            Sequence("s", "GGACXZ")

    def test_rejects_empty(self):
        with pytest.raises(SequenceError, match="empty"):
            Sequence("s", "   ")

    def test_flags_ambiguous_codes(self):
        assert Sequence("s", "GGACNN").has_ambiguous
        assert not Sequence("s", "GGACUU").has_ambiguous

    def test_gc_fraction(self):
        assert Sequence("s", "GGCCAAUU").gc_fraction == 0.5


class TestRegion:
    def test_is_one_based_and_inclusive(self):
        seq = Sequence("s", "AAAGGGCCC")
        region = Region(4, 6)
        assert len(region) == 3
        assert region.slice(seq) == "GGG"

    def test_rejects_out_of_range_slice(self):
        with pytest.raises(SequenceError, match="only 9 nt"):
            Region(8, 12).slice(Sequence("s", "AAAGGGCCC"))

    def test_rejects_inverted_and_zero_based(self):
        with pytest.raises(SequenceError):
            Region(9, 4)
        with pytest.raises(SequenceError):
            Region(0, 4)

    def test_overlap(self):
        assert Region(1, 10).overlaps(Region(10, 20))
        assert not Region(1, 10).overlaps(Region(11, 20))

    def test_flanks_are_clipped_to_the_sequence(self):
        region = Region(3, 6).with_flanks(10, 10, limit=20)
        assert (region.start, region.end) == (1, 16)

    def test_local_coordinates_round_trip(self):
        context = Region(105, 324)
        assert Region(205, 224).to_local(context).start == 101

    def test_local_coordinates_reject_escape(self):
        with pytest.raises(SequenceError, match="not contained"):
            Region(1, 5).to_local(Region(10, 20))


class TestParseRegion:
    def test_numeric_forms(self):
        assert parse_region("4-9") == Region(4, 9)
        assert parse_region("4..9") == Region(4, 9)
        assert parse_region("seed:4-9").name == "seed"

    def test_locates_a_unique_subsequence(self):
        seq = Sequence("s", "AAAGGGCCCUUU")
        assert parse_region("GGGCCC", seq) == Region(4, 9, name="match")

    def test_rejects_ambiguous_subsequence(self):
        seq = Sequence("s", "AAAGGGAAAGGG")
        with pytest.raises(SequenceError, match="more than once"):
            parse_region("GGG", seq)

    def test_rejects_absent_subsequence(self):
        with pytest.raises(SequenceError, match="does not occur"):
            parse_region("UUUU", Sequence("s", "AAAGGG"))


class TestTiling:
    def test_covers_every_offset(self):
        windows = tile_regions(10, 4, 1)
        assert len(windows) == 7
        assert windows[0] == Region(1, 4, name="w1")
        assert windows[-1] == Region(7, 10, name="w7")

    def test_rejects_window_longer_than_sequence(self):
        with pytest.raises(SequenceError, match="longer than"):
            tile_regions(5, 10)


class TestThermo:
    def test_probability_and_energy_round_trip(self):
        for probability in (1.0, 0.5, 1e-3, 1e-9):
            dg = thermo.dg_open_from_probability(probability)
            assert thermo.probability_from_dg_open(dg) == pytest.approx(
                probability, rel=1e-9
            )

    def test_zero_probability_maps_to_infinite_opening_cost(self):
        """A true zero is not silently converted into a finite point estimate."""
        dg = thermo.dg_open_from_probability(0.0)
        assert math.isinf(dg) and dg > 0

    def test_certain_site_costs_nothing(self):
        assert thermo.dg_open_from_probability(1.0) == pytest.approx(0.0)

    def test_temperature_changes_the_conversion(self):
        assert thermo.dg_open_from_probability(0.1, 37.0) != \
            thermo.dg_open_from_probability(0.1, 25.0)

    def test_extreme_favourable_energy_stays_a_bounded_probability(self):
        assert thermo.probability_from_dg_open(-500.0) == 1.0


class TestModelSettings:
    def test_window_must_contain_the_span(self):
        with pytest.raises(ValueError, match="at least"):
            ModelSettings(max_bp_span=300, window_size=100)

    @pytest.mark.parametrize(
        ("kwargs", "message"),
        (
            ({"temperature_c": float("nan")}, "temperature_c"),
            ({"temperature_c": float("inf")}, "temperature_c"),
            ({"salt_molar": float("nan")}, "salt_molar"),
            ({"salt_molar": -0.001}, "salt_molar"),
        ),
    )
    def test_rejects_nonphysical_protocol_scalars(self, kwargs, message):
        with pytest.raises(ValueError, match=message):
            ModelSettings(**kwargs)

    def test_molecule_switches_parameter_set(self):
        assert ModelSettings().for_molecule("dna").param_set == "dna_mathews2004"
        assert ModelSettings(param_set="dna_mathews2004").for_molecule(
            "rna"
        ).param_set == "turner2004"

    def test_variants_are_distinct_protocols(self):
        signatures = [v.signature() for v in ModelSettings().variants()]
        assert len(set(signatures)) >= 5

    def test_rejects_unknown_parameter_set(self):
        with pytest.raises(ValueError, match="unknown parameter set"):
            ModelSettings(param_set="nonsense")


class TestProbingData:
    def test_missing_values_become_vienna_sentinels(self):
        data = ProbingData((0.1, None, 0.9))
        assert data.as_vienna_vector() == [-999.0, 0.1, -999.0, 0.9]

    def test_coverage_counts_only_measured_positions(self):
        assert ProbingData((0.1, None, 0.9, None)).coverage == 0.5

    def test_slicing_is_one_based_inclusive(self):
        assert ProbingData((1.0, 2.0, 3.0, 4.0)).sliced(2, 3).reactivities == (2.0, 3.0)

    def test_rejects_nonfinite_values(self):
        with pytest.raises(ValueError, match="not finite"):
            ProbingData((0.1, float("nan")))

    @pytest.mark.parametrize("parameter", ("slope", "intercept", "beta"))
    def test_rejects_nonfinite_conversion_parameters(self, parameter):
        with pytest.raises(ValueError, match=parameter):
            ProbingData((0.1,), **{parameter: float("nan")})


class TestRecognitionSpec:
    def test_rejects_unknown_seed_mode(self):
        with pytest.raises(ValueError, match="unknown seed_mode"):
            RecognitionSpec(seed_mode="somewhere")

    def test_fixed_seed_requires_a_coordinate(self):
        with pytest.raises(ValueError, match="requires seed_start"):
            RecognitionSpec(seed_mode="fixed")

    @pytest.mark.parametrize(
        ("binder_class", "status", "supported"),
        (
            ("dna_probe", "complementary", True),
            ("RNA probe", "complementary", True),
            ("cas13", "complementary", True),
            ("unspecified", "exploratory", True),
            ("protein", "not_applicable", False),
            ("small-molecule", "not_applicable", False),
            ("custom", "not_applicable", False),
        ),
    )
    def test_seed_nucleation_depends_on_declared_binder_mechanism(
        self, binder_class, status, supported,
    ):
        recognition = RecognitionSpec(binder_class=binder_class)
        assert recognition.seed_nucleation_status == status
        assert recognition.supports_seed_nucleation is supported

    def test_fixed_seed_is_not_a_validity_constraint_for_a_protein(self):
        recognition = RecognitionSpec(
            binder_class="protein", seed_mode="fixed", seed_start=100,
        )
        assert not recognition.requires_declared_seed


class TestLocalAndGlobalSpan:
    def test_global_span_is_unrestricted_by_default(self):
        from rnavail.adapters import _vienna as V
        settings = ModelSettings(max_bp_span=60, window_size=67)
        assert V.make_md(settings, local=True).max_bp_span == 60
        assert V.make_md(settings, local=False).max_bp_span == -1

    def test_global_span_can_be_explicitly_limited(self):
        from rnavail.adapters import _vienna as V
        settings = ModelSettings(
            max_bp_span=60, global_max_bp_span=40, window_size=67
        )
        assert V.make_md(settings, local=False).max_bp_span == 40
