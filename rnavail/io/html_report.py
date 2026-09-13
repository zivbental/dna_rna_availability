"""Self-contained HTML report: metrics tables, notes, and per-candidate
base-pair probability heatmaps and structure diagrams.

Modelled on the "one card per candidate" style used for reporting toehold-
switch designs: a properties table, a set of interpretive bullets, and a
structure/probability diagram pair. Only the shape is borrowed — the content
is whatever rnavail actually measured (self-folding accessibility; this tool
does not predict binding to another RNA), not toehold-specific fields (RBS,
AUG, reading frame, trigger binding) it has no opinion about.

Everything is embedded as base64 PNG data URIs, so the resulting file is a
single portable artifact with no companion image directory.
"""

from __future__ import annotations

import html
import time
from pathlib import Path
from typing import Sequence as TSequence

from ..core.result import M, UNITS
from ..pipeline.run import CandidateReport, Report
from ..viz.generate import CandidateVisuals
from .report import SUMMARY_COLUMNS, _format

#: (metric key, display label, kind) shown in each candidate's properties
#: table, in this order, skipping whatever the candidate does not have.
#: kind picks the formatter: "pct" for a 0-1 probability, "kcal" for an
#: energy, "kcal_per_nt" for a length-normalised energy, "nt" for a position
#: or length, "num" for anything else.
#:
#: A dozen tools and a handful of opt-in sweeps between them produce far more
#: than this many distinct metrics (``report.json``'s per-candidate
#: ``metrics`` has ~19 on a typical run) — this table is deliberately curated
#: for a card meant to be read at a glance, not a dump of everything
#: computed. What's curated out is never hidden, only elsewhere: every raw
#: number is in ``report.json``, the composite-score components (a distinct,
#: smaller set — see ``DEFAULT_CRITERIA`` — that decides the ranking) are
#: rendered in their own table below, and anything that changes what you'd
#: do next is already in the notes above.
PROPERTY_ROWS: tuple[tuple[str, str, str], ...] = (
    (M.P_UNPAIRED, "Full-site joint accessibility", "pct"),
    (M.SEED_P_UNPAIRED, "Seed accessibility", "pct"),
    (M.DG_OPEN, "Opening cost, full site", "kcal"),
    (M.DG_OPEN_PER_NT, "Opening cost per nucleotide", "kcal_per_nt"),
    (M.SEED_DG_OPEN, "Opening cost, seed", "kcal"),
    (M.DG_OPEN_SPREAD, "Opening-cost spread across model settings", "kcal"),
    (M.WINDOW_LENGTH_SPREAD, "Opening-cost spread across window length", "kcal_per_nt"),
    (M.WINDOW_EXACT_GAP, "Windowed-vs-exact opening-cost gap", "kcal"),
    (M.RIBOSNITCH_SPREAD, "Opening-cost spread across point mutations", "kcal"),
    (M.CONTEXT_DG_SPREAD, "Opening-cost spread across flanking context", "kcal"),
    (M.GQUAD_SCORE, "Signed G-rich/C-rich sequence propensity (G4Hunter)", "num"),
    (M.PSEUDOKNOT_PAIRED_FRACTION, "Paired into a pseudoknot (ProbKnot)", "pct"),
    (M.CO_TX_TRAP_LENGTH, "Co-transcriptional trap length", "nt"),
    (M.MEAN_BASE_UNPAIRED, "Mean per-base unpaired (diagnostic only)", "pct"),
    (M.MIN_BASE_UNPAIRED, "Min per-base unpaired (diagnostic only)", "pct"),
    (M.PAIRED_FRACTION, "Paired fraction (diagnostic only)", "pct"),
)


def _fmt_value(value: float, kind: str) -> str:
    if kind == "pct":
        return f"{value * 100:.1f}%" if 0.0 <= value <= 1.0 else f"{value:.3g}"
    if kind == "kcal":
        return f"{value:.2f} kcal/mol"
    if kind == "kcal_per_nt":
        return f"{value:.3f} kcal/mol/nt"
    if kind == "nt":
        return f"{value:.0f} nt"
    return f"{value:.3g}"


def _esc(text: str) -> str:
    return html.escape(str(text))


def to_html(
    report: Report,
    visuals: dict[str, CandidateVisuals],
    path: str | Path | None = None,
    top: int = 10,
    transcript_visuals: dict[str, str] | None = None,
) -> str:
    """Render the full visual report and optionally write it to ``path``."""
    ranked = report.ranked()
    displayed = ranked[:top]
    parts: list[str] = [
        _HEAD,
        _header(report),
        _navigation(displayed, has_transcript=bool(transcript_visuals)),
        '<main id="report-content">',
    ]

    if transcript_visuals:
        parts.append(_transcript_section(transcript_visuals))

    parts.append(_summary_table(displayed))

    for candidate in displayed:
        parts.append(_candidate_card(candidate, visuals.get(candidate.key)))

    parts.append(_footer(report))
    text = "\n".join(parts) + "\n</body>\n</html>\n"
    if path:
        Path(path).write_text(text)
    return text


_HEAD = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>rnavail report</title>
<style>
  :root { color-scheme: light; }
  body { font-family: -apple-system, Segoe UI, Helvetica, Arial, sans-serif;
         background: #fafafa; color: #1a1a1a; margin: 0; padding: 0 0 3em 0; }
  header { background: #20303f; color: #fff; padding: 1.5em 2em; }
  header h1 { margin: 0 0 0.2em 0; font-size: 1.5em; }
  header .sub { color: #cfd8e0; font-size: 0.92em; }
  .report-layout { display: grid; grid-template-columns: minmax(180px, 235px) minmax(0, 1100px);
                   gap: 2em; max-width: 1400px; margin: 0 auto; padding: 0 2em; }
  .report-nav { position: sticky; top: 1em; align-self: start; margin-top: 1.6em;
                max-height: calc(100vh - 2em); overflow-y: auto; }
  .report-nav h2 { font-size: 0.9em; text-transform: uppercase; letter-spacing: 0.06em;
                   color: #586575; border: 0; margin: 0 0 0.65em; padding: 0; }
  .report-nav ul { list-style: none; margin: 0; padding: 0; }
  .report-nav li { margin: 0.12em 0; }
  .report-nav a { display: block; padding: 0.35em 0.5em; border-radius: 4px; color: #314e66;
                  font-size: 0.88em; text-decoration: none; }
  .report-nav a:hover, .report-nav a:focus { background: #eaf0f5; text-decoration: underline; }
  .report-nav .nav-candidates { border-top: 1px solid #d8dee4; margin-top: 0.65em;
                                padding-top: 0.65em; }
  main { min-width: 0; }
  h2 { border-bottom: 2px solid #d8dee4; padding-bottom: 0.3em; margin-top: 2.2em; }
  table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 0.92em; }
  th, td { border: 1px solid #d8dee4; padding: 0.4em 0.6em; text-align: left; }
  th { background: #eef1f4; }
  td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
  tr.best { background: #fff6e8; }
  .card { background: #fff; border: 1px solid #d8dee4; border-radius: 8px;
          padding: 1.2em 1.4em; margin: 1.4em 0; }
  .card h3 { margin-top: 0; }
  .seq { font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 0.85em;
         background: #f3f5f7; padding: 0.3em 0.5em; border-radius: 4px;
         word-break: break-all; }
  .score-badge { display: inline-block; background: #20303f; color: #fff;
         border-radius: 4px; padding: 0.15em 0.6em; font-weight: 600;
         margin-left: 0.6em; font-size: 0.85em; }
  .notes { margin: 0.9em 0; padding-left: 1.3em; }
  .notes li { margin-bottom: 0.4em; }
  .viz-row { display: flex; flex-wrap: wrap; gap: 1em; margin: 1em 0; }
  .viz-row figure { margin: 0; flex: 1 1 320px; text-align: center; }
  .viz-row img { max-width: 100%; border: 1px solid #e2e6ea; border-radius: 4px; }
  .viz-row figcaption { font-size: 0.82em; color: #555; margin-top: 0.3em; }
  .warnings, .toolinfo { background: #fff; border: 1px solid #e6d9a8;
         border-left: 4px solid #d9a52b; border-radius: 4px; padding: 0.9em 1.2em;
         margin: 1.2em 0; font-size: 0.9em; }
  .toolinfo { border-left-color: #6b8fb0; }
  code { background: #f0f2f4; padding: 0.05em 0.35em; border-radius: 3px; }
  footer { max-width: 1100px; margin: 2em auto 0 auto; padding: 0 2em;
           color: #888; font-size: 0.82em; }
  @media (max-width: 850px) {
    .report-layout { display: block; padding: 0 1em; }
    .report-nav { position: static; max-height: none; margin: 1em 0; }
    .report-nav ul { display: flex; flex-wrap: wrap; gap: 0.2em; }
    .report-nav li { margin: 0; }
    .report-nav .nav-candidates { width: 100%; }
    .report-nav .nav-candidates ul { max-height: 9em; overflow-y: auto; display: block; }
  }
</style>
</head>
<body>
"""


def _header(report: Report) -> str:
    sequence = report.sequence
    generated = time.strftime("%Y-%m-%d %H:%M:%S")
    recognition = report.recognition
    condition = report.condition
    recognition_text = (
        f"{recognition.binder_class}; seed {recognition.seed_mode} / "
        f"{recognition.seed_lengths[0]} nt; endpoint {recognition.endpoint}"
        if recognition else "recognition unspecified"
    )
    condition_text = (
        f"{condition.condition_id}; {condition.temperature_c:g} °C; "
        f"{condition.preparation}"
        if condition else "condition unspecified"
    )
    evidence_text = (
        f" &middot; {len(report.evidence_tracks)} evidence track(s), annotation only"
        if report.evidence_tracks else ""
    )
    return f"""
<header id="overview">
  <h1>rnavail {_esc(report.mode)} report — {_esc(sequence.name)}</h1>
  <div class="sub">{len(sequence)} nt &middot; {sequence.molecule.upper()} &middot;
    GC {sequence.gc_fraction:.1%} &middot; protocol {_esc(report.settings.signature())}
    &middot; generated {generated}<br>
    recognition {_esc(recognition_text)} &middot; condition {_esc(condition_text)}
    {evidence_text}</div>
</header>
<div class="report-layout">
"""


def _candidate_anchor(candidate: CandidateReport) -> str:
    """Stable in-page target for a candidate's one-based interval."""
    return f"candidate-{candidate.region.start}-{candidate.region.end}"


def _navigation(
    candidates: TSequence[CandidateReport], *, has_transcript: bool,
) -> str:
    """Fast, no-JavaScript navigation through a portable report."""
    links = [
        '<nav class="report-nav" aria-label="Report navigation">',
        "<h2>Jump to</h2>",
        "<ul>",
        '<li><a href="#overview">Overview</a></li>',
        '<li><a href="#ranked-candidates">Ranked candidates</a></li>',
        "</ul>",
    ]
    if has_transcript:
        links.insert(4, '<li><a href="#transcript">Transcript plots</a></li>')
    if candidates:
        links.extend(['<div class="nav-candidates">', "<h2>Candidate locations</h2>", "<ul>"])
        for rank, candidate in enumerate(candidates, 1):
            label = f"{rank}. {candidate.region.start}&ndash;{candidate.region.end}"
            links.append(
                f'<li><a href="#{_candidate_anchor(candidate)}">{label}</a></li>'
            )
        links.extend(["</ul>", "</div>"])
    links.append("</nav>")
    return "\n".join(links)


def _transcript_section(transcript_visuals: dict[str, str]) -> str:
    """The whole-transcript accessibility profile and (position, length)
    landscape, shown once above the per-candidate cards.

    Both come from RNAplfold's own table, computed once during screening;
    see :mod:`rnavail.viz.landscape` for what each answers. Shaded bands on
    the profile mark the candidates ranked below.
    """
    parts = [
        '<section id="transcript">',
        "<h2>Whole-transcript accessibility</h2>",
        '<p style="color:#555; font-size:0.9em; max-width:70ch;">'
        "Every position, not just the ones <code>--step</code> tiled as "
        "candidates — the underlying calculation is already at this "
        "resolution. The landscape below sweeps window length too, so a "
        "site that is only cheap to open at one specific length shows up as "
        "an isolated fleck rather than a broad, robust streak.</p>",
    ]
    if "profile" in transcript_visuals:
        parts.append(
            '<figure style="margin:0 0 1em 0;">'
            f'<img src="{transcript_visuals["profile"]}" '
            'style="max-width:100%; border:1px solid #e2e6ea; border-radius:4px;" '
            'alt="accessibility profile">'
            '<figcaption style="font-size:0.82em; color:#555; margin-top:0.3em;">'
            "shaded bands: the ranked candidates below</figcaption>"
            "</figure>"
        )
    if "landscape" in transcript_visuals:
        parts.append(
            '<figure style="margin:0;">'
            f'<img src="{transcript_visuals["landscape"]}" '
            'style="max-width:100%; border:1px solid #e2e6ea; border-radius:4px;" '
            'alt="accessibility landscape">'
            '<figcaption style="font-size:0.82em; color:#555; margin-top:0.3em;">'
            "dG_open per nucleotide, every (start position, window length)"
            "</figcaption>"
            "</figure>"
        )
    parts.append("</section>")
    return "\n".join(parts)


def _summary_table(candidates: TSequence[CandidateReport]) -> str:
    rows = ['<h2 id="ranked-candidates">Ranked candidates</h2>', "<table>", "<tr>"]
    for _, label, unit in SUMMARY_COLUMNS:
        suffix = f" ({unit})" if unit else ""
        rows.append(f'<th class="num">{_esc(label)}{_esc(suffix)}</th>')
    rows.append("</tr>")
    for index, candidate in enumerate(candidates):
        css = ' class="best"' if index == 0 else ""
        rows.append(f"<tr{css}>")
        for key, _, _ in SUMMARY_COLUMNS:
            if key == "region":
                value = (
                    f'<a href="#{_candidate_anchor(candidate)}">'
                    f"{_esc(candidate.region.label)}</a>"
                )
            elif key == "length":
                value = str(len(candidate.region))
            elif key == "heuristic_rank_score":
                value = _format(
                    candidate.score.value if candidate.score else None,
                    "heuristic_rank_score",
                )
            else:
                value = _format(candidate.metrics.get(key), key)
            if key == "region":
                rows.append(f'<td class="num">{value}</td>')
            else:
                rows.append(f'<td class="num">{_esc(value)}</td>')
        rows.append("</tr>")
    rows.append("</table>")
    return "\n".join(rows)


def _candidate_card(candidate: CandidateReport, visuals: CandidateVisuals | None) -> str:
    score = candidate.score.value if candidate.score else 0.0
    coverage = candidate.score.coverage if candidate.score else 0.0
    parts = [
        f'<section class="card" id="{_candidate_anchor(candidate)}">',
        f"<h3>{_esc(candidate.region.label)}"
        f'<span class="score-badge">heuristic rank {score:.3f}</span></h3>',
        f'<div class="seq">{_esc(candidate.subsequence)}</div>',
        f'<p style="color:#666; font-size:0.88em;">'
        f"coverage: {coverage:.0%} of scoring weight had data behind it</p>",
    ]

    property_rows = [
        (label, _fmt_value(candidate.metrics[key], kind))
        for key, label, kind in PROPERTY_ROWS
        if key in candidate.metrics
    ]
    if property_rows:
        parts.append("<table>")
        for label, value in property_rows:
            parts.append(f"<tr><td>{_esc(label)}</td><td class='num'>{_esc(value)}</td></tr>")
        parts.append("</table>")

    primary = next(
        (
            observation for observation in candidate.opening_observations
            if observation.observation_id == candidate.primary_opening_observation_id
        ),
        None,
    )
    if primary is not None:
        if primary.estimate_kind == "point":
            parts.append(
                '<p style="color:#555; font-size:0.88em;">'
                f"primary opening: {_esc(primary.tool)} / "
                f"{_esc(primary.sequence_scope)} / "
                f"{_esc(primary.conditioning_id)}</p>"
            )
        else:
            parts.append(
                '<p style="color:#555; font-size:0.88em;">'
                f"primary opening has no point estimate ({_esc(primary.estimate_kind)})"
                "</p>"
            )

    if candidate.notes:
        parts.append('<div class="notes"><strong>What stands out</strong><ul>')
        for note in candidate.notes:
            parts.append(f"<li>{_esc(note)}</li>")
        parts.append("</ul></div>")

    if candidate.biological_evidence:
        parts.append(_evidence_section(candidate.biological_evidence))

    if candidate.score:
        parts.append(_score_breakdown(candidate.score))

    if visuals is not None:
        parts.append(_viz_section(visuals.heatmap, visuals.structure))

    parts.append("</section>")
    return "\n".join(parts)


def _score_breakdown(score) -> str:
    """The handful of criteria that actually decide the ranking.

    Deliberately separate from the properties table above, and usually much
    shorter: properties are everything measured worth showing, this is only
    ``DEFAULT_CRITERIA`` (or whatever ``--weights`` overrode it with) — the
    specific, curated set the weighted geometric mean combines into the
    rank badge at the top of this card. A dozen tools feeding twenty
    measured properties and a smaller set of scoring criteria are different
    counts on purpose; this table is what answers "which of them actually moved
    the number".
    """
    rows = []
    for component in score.components:
        if not component.present:
            continue
        pct = max(0, min(100, round(component.desirability * 100)))
        rows.append(
            "<tr>"
            f"<td>{_esc(component.criterion.label)}</td>"
            f'<td class="num">{component.value:.4g}</td>'
            "<td>"
            '<div style="background:#eef1f4; border-radius:3px; overflow:hidden; '
            'width:90px; display:inline-block; vertical-align:middle;">'
            f'<div style="background:#20303f; width:{pct}%; height:0.8em;"></div>'
            "</div>"
            f'<span style="font-size:0.85em; color:#666; margin-left:0.4em;">'
            f"{component.desirability:.2f}</span>"
            "</td>"
            f'<td class="num">{component.criterion.weight:g}</td>'
            "</tr>"
        )
    if not rows:
        return ""

    parts = [
        '<details open style="margin-top:0.9em;">',
        '<summary style="cursor:pointer; color:#455; font-size:0.88em;">'
        f"score breakdown &mdash; {len(rows)} criteria, "
        f"{score.coverage:.0%} coverage</summary>",
        '<table style="margin-top:0.6em;">'
        "<tr><th>criterion</th><th class='num'>value</th>"
        "<th>desirability</th><th class='num'>weight</th></tr>",
        *rows,
        "</table>",
    ]
    if score.missing:
        parts.append(
            '<p style="color:#888; font-size:0.82em; margin:0.5em 0 0 0;">'
            f"not scored (no data): {_esc(', '.join(score.missing))}</p>"
        )
    parts.append("</details>")
    return "\n".join(parts)


def _evidence_section(entries: list[dict]) -> str:
    """Render overlapping records without assigning them an effect direction."""
    rows = [
        '<details style="margin-top:0.9em;">',
        '<summary style="cursor:pointer; color:#455; font-size:0.88em;">'
        f"condition-linked evidence ({len(entries)} record(s), annotation only)"
        "</summary>",
        '<table style="margin-top:0.6em;">',
        "<tr><th>type</th><th>interval</th><th>condition</th>"
        "<th>value</th><th>interpretation</th></tr>",
    ]
    for entry in entries:
        record = entry["record"]
        interval = record["interval"]
        interval_text = f"{interval['start']}-{interval['end']}"
        value = record.get("value")
        if value is None:
            value_text = "no measured value"
        else:
            value_text = str(value)
            if record.get("unit"):
                value_text += f" {record['unit']}"
        rows.append(
            "<tr>"
            f"<td>{_esc(entry['evidence_type'])}</td>"
            f"<td class='num'>{_esc(interval_text)}</td>"
            f"<td>{_esc(entry['condition_status'])}</td>"
            f"<td>{_esc(value_text)}</td>"
            f"<td>{_esc(record.get('interpretation', ''))}</td>"
            "</tr>"
        )
    rows.extend(["</table>", "</details>"])
    return "\n".join(rows)


def _viz_section(heatmap: str, structure: str) -> str:
    figures = (
        f'<figure><img src="{heatmap}" alt="base-pair probability heatmap">'
        f'<figcaption>base-pair probability</figcaption></figure>'
        f'<figure><img src="{structure}" alt="predicted structure">'
        f"<figcaption>predicted structure</figcaption></figure>"
    )
    return f'<div class="viz-row">{figures}</div>'


def _footer(report: Report) -> str:
    parts = []
    if report.tools_failed or report.tools_skipped or report.warnings:
        parts.append('<div class="toolinfo">')
        parts.append(f"<strong>Tools that ran:</strong> {_esc(', '.join(report.tools_ran))}")
        if report.tools_skipped:
            skipped = ", ".join(t for t, _ in report.tools_skipped)
            parts.append(f"<br><strong>Unavailable:</strong> {_esc(skipped)}")
        if report.tools_failed:
            failed = ", ".join(t for t, _ in report.tools_failed)
            parts.append(f"<br><strong>Failed:</strong> {_esc(failed)}")
        parts.append("</div>")

    warnings = list(report.warnings)
    for result in report.tool_results:
        for warning in result.warnings:
            warnings.append(f"[{result.tool}] {warning}")
    if warnings:
        parts.append('<div class="warnings"><strong>Warnings</strong><ul class="notes">')
        for warning in warnings:
            parts.append(f"<li>{_esc(warning)}</li>")
        parts.append("</ul></div>")

    parts.append(
        "</main></div><footer>Generated by rnavail &middot; accessibility is "
        "predicted, not measured &mdash; treat rankings as evidence, not "
        "ground truth.</footer>"
    )
    return "\n".join(parts)
