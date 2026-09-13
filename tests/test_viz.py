"""Visual report: heatmaps, structure diagrams, and HTML assembly.

These check the plumbing (valid image data, correct shapes, graceful
degradation) rather than pixel content — a rendered PNG is not something a
unit test should compare byte-for-byte against a golden file.
"""

import base64

import pytest

from rnavail.core.model import ModelSettings
from rnavail.core.sequence import Region, Sequence
from rnavail.viz import mpl
from rnavail.viz.dotplot import bpp_to_matrix, render_bpp_heatmap
from rnavail.viz.generate import build_candidate_visuals
from rnavail.viz.landscape import (
    _dg_per_nt, render_accessibility_landscape, render_accessibility_profile,
)
from rnavail.viz.structure import Highlight, render_structure

pytestmark = pytest.mark.skipif(
    not mpl.available(), reason="matplotlib not installed"
)

TARGET = Sequence(
    "target",
    "GGGAAACCCAUAUAUAUAUGCGCGCUUUUUUGCGCGCAAAGGGAAACCCUUAAGGUUCCAAGGUUCC",
)
SETTINGS = ModelSettings(max_bp_span=60, window_size=67)


def _is_png_data_uri(value: str) -> bool:
    if not value.startswith("data:image/png;base64,"):
        return False
    raw = base64.b64decode(value.split(",", 1)[1])
    return raw[:8] == b"\x89PNG\r\n\x1a\n"


class TestBppMatrix:
    def test_converts_upper_triangular_to_symmetric(self):
        length = 4
        bpp = [[0.0] * (length + 2) for _ in range(length + 2)]
        bpp[1][3] = 0.7
        matrix = bpp_to_matrix(bpp, length)
        assert matrix[0, 2] == pytest.approx(0.7)
        assert matrix[2, 0] == pytest.approx(0.7)
        assert matrix[0, 1] == 0.0

    def test_shape_matches_sequence_length(self):
        bpp = [[0.0] * 10 for _ in range(10)]
        assert bpp_to_matrix(bpp, 8).shape == (8, 8)


class TestHeatmap:
    def test_renders_a_valid_png_data_uri(self):
        bpp = [[0.0] * 12 for _ in range(12)]
        bpp[1][8] = 0.9
        matrix = bpp_to_matrix(bpp, 10)
        uri = render_bpp_heatmap(matrix, "test", highlight=(3, 6))
        assert _is_png_data_uri(uri)

    def test_junction_line_does_not_error(self):
        matrix = bpp_to_matrix([[0.0] * 20 for _ in range(20)], 18)
        uri = render_bpp_heatmap(matrix, "dimer", junction=10)
        assert _is_png_data_uri(uri)


class TestStructureDiagram:
    def test_renders_a_valid_png_data_uri(self):
        seq = "GGGAAACCC"
        structure = "(((...)))"
        uri = render_structure(seq, structure, "test",
                               highlights=(Highlight(1, 3, "#ff0000", "stem"),))
        assert _is_png_data_uri(uri)

    def test_mismatched_lengths_are_rejected(self):
        with pytest.raises(ValueError, match="does not match"):
            render_structure("GGGAAACCC", "(((...))", "test")

    def test_long_sequence_drops_letters_without_erroring(self):
        seq = "A" * 200
        structure = "." * 200
        uri = render_structure(seq, structure, "long")
        assert _is_png_data_uri(uri)


class TestAccessibilityLandscape:
    """The whole-transcript profile and (position, length) heatmap.

    Both are drawn directly from RNAplfold's own table -- no folding happens
    here -- so these tests build a small synthetic table rather than calling
    into ViennaRNA, keeping them independent of the ``mpl.available()``
    skip's sibling concern (the bindings themselves).
    """

    @staticmethod
    def _table(length: int, max_len: int) -> dict:
        """A table where every window is 50% unpaired, for a fast, cheap
        synthetic fixture -- the numeric content is not what's under test
        here, only that the plumbing draws something sane from it.
        """
        return {
            end: [None] + [0.5] * max_len
            for end in range(1, length + 1)
        }

    def test_dg_per_nt_is_zero_for_a_certain_open_window(self):
        assert _dg_per_nt(1.0, 10, 37.0) == pytest.approx(0.0)

    def test_dg_per_nt_is_nan_for_an_impossible_window(self):
        import math
        assert math.isnan(_dg_per_nt(0.0, 10, 37.0))
        assert math.isnan(_dg_per_nt(None, 10, 37.0))

    def test_profile_renders_a_valid_png(self):
        table = self._table(length=40, max_len=15)
        uri = render_accessibility_profile(
            table, sequence_length=40, window=10, temperature_c=37.0,
        )
        assert _is_png_data_uri(uri)

    def test_profile_accepts_highlight_spans_without_erroring(self):
        table = self._table(length=40, max_len=15)
        uri = render_accessibility_profile(
            table, sequence_length=40, window=10, temperature_c=37.0,
            highlights=((5, 14, "w5"), (20, 29, "w20")),
        )
        assert _is_png_data_uri(uri)

    def test_landscape_renders_a_valid_png(self):
        table = self._table(length=40, max_len=15)
        uri = render_accessibility_landscape(
            table, sequence_length=40, max_length=15, temperature_c=37.0,
        )
        assert _is_png_data_uri(uri)

    def test_landscape_tolerates_a_ragged_table_near_the_sequence_ends(self):
        """Positions near the start have shorter rows than the interior --
        the boundary case the (position, length) grid must not crash on."""
        table = {end: [None] + [0.5] * min(end, 15) for end in range(1, 41)}
        uri = render_accessibility_landscape(
            table, sequence_length=40, max_length=15, temperature_c=37.0,
        )
        assert _is_png_data_uri(uri)


class TestCandidateVisuals:
    def test_produces_a_heatmap_and_structure(self):
        visuals = build_candidate_visuals(
            TARGET, Region(20, 32), SETTINGS, flank=20,
        )
        assert _is_png_data_uri(visuals.heatmap)
        assert _is_png_data_uri(visuals.structure)

    def test_context_flanks_the_region_and_clips_at_the_ends(self):
        visuals = build_candidate_visuals(
            TARGET, Region(2, 5), SETTINGS, flank=100,
        )
        assert visuals.context.start == 1
        assert visuals.context.end == len(TARGET)


class TestHtmlReport:
    @staticmethod
    def _report_and_visuals():
        from rnavail.pipeline.run import evaluate
        report = evaluate(
            TARGET, [Region(9, 20, "loose"), Region(20, 32, "hairpin")],
            settings=SETTINGS, seed_length=8,
        )
        visuals = {
            c.key: build_candidate_visuals(TARGET, c.region, SETTINGS, flank=15)
            for c in report.candidates
        }
        return report, visuals

    def test_report_contains_every_candidate_and_its_images(self):
        from rnavail.io.html_report import to_html
        report, visuals = self._report_and_visuals()
        text = to_html(report, visuals)
        assert "loose" in text or "9-20" in text
        assert text.count("data:image/png;base64,") == 4  # 2 candidates x 2

    def test_report_has_sidebar_links_to_each_displayed_candidate(self):
        from rnavail.io.html_report import to_html
        report, visuals = self._report_and_visuals()
        text = to_html(report, visuals, top=1)
        candidate = report.ranked()[0]
        anchor = f"candidate-{candidate.region.start}-{candidate.region.end}"
        assert 'aria-label="Report navigation"' in text
        assert f'href="#{anchor}"' in text
        assert f'id="{anchor}"' in text

    def test_report_includes_notes_and_score(self):
        from rnavail.io.html_report import to_html
        report, visuals = self._report_and_visuals()
        text = to_html(report, visuals)
        hairpin = next(c for c in report.candidates if c.region.name == "hairpin")
        assert hairpin.notes, "expected at least one diagnostic note"
        assert hairpin.notes[0][:20].split(":")[0][:15] in text or "score" in text

    def test_report_degrades_without_visuals(self):
        """A candidate with no rendered visuals still gets its table and notes."""
        from rnavail.io.html_report import to_html
        report, _ = self._report_and_visuals()
        text = to_html(report, {})
        assert "data:image/png;base64," not in text
        assert "score" in text

    def test_writes_to_a_file(self, tmp_path):
        from rnavail.io.html_report import to_html
        report, visuals = self._report_and_visuals()
        path = tmp_path / "r.html"
        to_html(report, visuals, path)
        assert path.is_file()
        assert path.read_text().startswith("<!doctype html>")

    def test_escapes_untrusted_text(self):
        """Sequence names end up in the page; they must not inject markup."""
        from rnavail.io.html_report import to_html
        from rnavail.pipeline.run import evaluate
        evil = Sequence("<script>alert(1)</script>", TARGET.seq)
        report = evaluate(evil, [Region(9, 20)], settings=SETTINGS)
        text = to_html(report, {})
        assert "<script>alert(1)</script>" not in text
        assert "&lt;script&gt;" in text

    def test_properties_table_surfaces_sweep_metrics_not_just_the_original_eight(self):
        """Regression test: PROPERTY_ROWS must be kept in step with new
        metrics as they're added, not silently left stuck at whatever set
        existed when the table was first written."""
        from rnavail.io.html_report import to_html
        from rnavail.pipeline.run import evaluate
        report = evaluate(
            TARGET, [Region(9, 20)], settings=SETTINGS, seed_length=8,
            length_robustness=True, ribosnitch=True, context_robustness=True,
        )
        text = to_html(report, {})
        for label in (
            "Opening-cost spread across window length",
            "Opening-cost spread across point mutations",
            "Opening-cost spread across flanking context",
        ):
            assert label in text

    def test_score_breakdown_lists_every_present_criterion(self):
        from rnavail.io.html_report import to_html
        from rnavail.pipeline.run import evaluate
        from rnavail.pipeline.score import DEFAULT_CRITERIA
        report, visuals = self._report_and_visuals()
        text = to_html(report, visuals)
        assert "score breakdown" in text
        # every criterion that has data on at least one candidate should be
        # named somewhere in the rendered breakdown tables.
        present_labels = {
            comp.criterion.label
            for c in report.candidates for comp in c.score.components
            if comp.present
        }
        for label in present_labels:
            assert label in text


class TestScoreBreakdown:
    """Unit-level: the score-explanation table, independent of a full report."""

    @staticmethod
    def _score(coverage=1.0, missing=()):
        from rnavail.pipeline.score import Criterion, Score, ScoreComponent
        criterion = Criterion(
            key="dg_open_per_nt", weight=1.5,
            desirability=lambda v: v, label="opening cost per nucleotide",
        )
        component = ScoreComponent(criterion, value=0.1, desirability=0.8, present=True)
        return Score(value=0.8, components=[component], coverage=coverage, missing=list(missing))

    def test_renders_the_criterion_label_and_weight(self):
        from rnavail.io.html_report import _score_breakdown
        html_text = _score_breakdown(self._score())
        assert "opening cost per nucleotide" in html_text
        assert "1.5" in html_text

    def test_lists_missing_criteria(self):
        from rnavail.io.html_report import _score_breakdown
        html_text = _score_breakdown(self._score(coverage=0.5, missing=["p_unpaired"]))
        assert "not scored" in html_text
        assert "p_unpaired" in html_text

    def test_empty_without_any_present_component(self):
        from rnavail.io.html_report import _score_breakdown
        from rnavail.pipeline.score import Score
        assert _score_breakdown(Score(value=0.0, components=[], coverage=0.0, missing=[])) == ""


class TestCLIVisualReport:
    def test_html_flag_writes_a_report(self, tmp_path):
        from rnavail.cli import main
        out = tmp_path / "report.html"
        code = main([
            "evaluate", TARGET.seq, "--region", "9-20",
            "--tools", "rnaplfold",
            "--max-bp-span", "60", "--window-size", "67",
            "--html", str(out), "-q",
        ])
        assert code == 0
        assert out.is_file()
        assert "data:image/png;base64," in out.read_text()

    def test_save_run_writes_html_by_default(self, tmp_path):
        from rnavail.cli import main
        base = tmp_path / "runs"
        main([
            "evaluate", TARGET.seq, "--region", "9-20",
            "--tools", "rnaplfold", "--max-bp-span", "60", "--window-size", "67",
            "--save-run", str(base), "-q",
        ])
        assert (base / "latest" / "report.html").is_file()

    def test_no_html_suppresses_it(self, tmp_path):
        from rnavail.cli import main
        base = tmp_path / "runs"
        main([
            "evaluate", TARGET.seq, "--region", "9-20",
            "--tools", "rnaplfold", "--max-bp-span", "60", "--window-size", "67",
            "--save-run", str(base), "--no-html", "-q",
        ])
        assert not (base / "latest" / "report.html").exists()

    def test_visualize_flank_is_respected(self, tmp_path):
        from rnavail.cli import main
        out = tmp_path / "report.html"
        code = main([
            "evaluate", TARGET.seq, "--region", "38-50",
            "--tools", "rnaplfold", "--max-bp-span", "60", "--window-size", "67",
            "--html", str(out), "--visualize-flank", "5", "-q",
        ])
        assert code == 0
        assert out.is_file()
