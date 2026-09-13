"""Rendering reports as text, JSON and TSV."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core.result import UNITS, M
from .rundir import format_duration
from ..pipeline.run import CandidateReport, Report

#: Columns shown in the ranked summary table, in order.
SUMMARY_COLUMNS: tuple[tuple[str, str, str], ...] = (
    ("region", "region", ""),
    ("length", "len", ""),
    ("heuristic_rank_score", "rank", ""),
    (M.SEED_P_UNPAIRED, "seedP", ""),
    (M.P_UNPAIRED, "P_unp", ""),
    (M.DG_OPEN, "dGopen", "kcal/mol"),
    (M.DG_OPEN_PER_NT, "dG/nt", "kcal/mol"),
)


def _format(value: float | None, metric: str) -> str:
    if value is None:
        return "-"
    if metric in (M.SEED_P_UNPAIRED, M.P_UNPAIRED):
        return f"{value:.2e}" if value < 0.01 else f"{value:.3f}"
    if metric in ("score", "heuristic_rank_score"):
        return f"{value:.3f}"
    if metric == "length":
        return str(int(value))
    return f"{value:.2f}"


def to_json(report: Report, path: str | Path | None = None, indent: int = 2) -> str:
    text = json.dumps(report.to_dict(), indent=indent, default=str)
    if path:
        Path(path).write_text(text)
    return text


def to_tsv(report: Report, path: str | Path | None = None) -> str:
    """One row per candidate, every metric it has, for downstream analysis."""
    candidates = report.ranked()
    metrics: list[str] = []
    for candidate in candidates:
        for name in candidate.metrics:
            if name not in metrics:
                metrics.append(name)
    metrics.sort()

    header = ["region", "start", "end", "length", "subsequence", "heuristic_rank_score",
              "coverage", *metrics]
    lines = ["\t".join(header)]
    for candidate in candidates:
        row = [
            candidate.region.label,
            str(candidate.region.start),
            str(candidate.region.end),
            str(len(candidate.region)),
            candidate.subsequence,
            f"{candidate.score.value:.6f}" if candidate.score else "",
            f"{candidate.score.coverage:.3f}" if candidate.score else "",
        ]
        for name in metrics:
            value = candidate.metrics.get(name)
            row.append("" if value is None else f"{value:.6g}")
        lines.append("\t".join(row))

    text = "\n".join(lines) + "\n"
    if path:
        Path(path).write_text(text)
    return text


def to_profile_tsv(report: Report, path: str | Path | None = None) -> str | None:
    """The whole-transcript accessibility profile, one row per position.

    Only present for a ``scan`` report: dG_open per nucleotide for the
    fixed-length window starting at every position, at single-nucleotide
    resolution regardless of the ``--step`` used to tile candidates. Returns
    ``None`` (writing nothing) when no profile was computed — an
    ``evaluate`` report, or a ``scan`` run without ViennaRNA's Python
    bindings available.
    """
    profile: dict[str, float] = report.detail.get("profile", {})
    if not profile:
        return None
    window = report.detail.get("profile_window", "")

    rows = sorted(profile.items(), key=lambda kv: int(kv[0]))
    lines = [f"start\tend\tdg_open_per_nt_window{window}"]
    for start_str, dg_per_nt in rows:
        start = int(start_str)
        lines.append(f"{start}\t{start + int(window) - 1}\t{dg_per_nt:.6g}")

    text = "\n".join(lines) + "\n"
    if path:
        Path(path).write_text(text)
    return text


def to_text(report: Report, top: int = 10, verbose: bool = False) -> str:
    """A readable summary: what ran, what ranked, and what to watch out for."""
    out: list[str] = []
    add = out.append

    sequence = report.sequence
    add(f"{'=' * 78}")
    add(f"rnavail {report.mode}: {sequence.name}  "
        f"({len(sequence)} nt, {sequence.molecule.upper()}, "
        f"GC {sequence.gc_fraction:.1%})")
    add(f"protocol: {report.settings.signature()}")
    if report.recognition is not None:
        recognition = report.recognition
        add(
            f"recognition: {recognition.binder_class}; "
            f"seed {recognition.seed_mode} / {recognition.seed_lengths[0]} nt; "
            f"endpoint {recognition.endpoint}"
        )
    if report.condition is not None:
        condition = report.condition
        add(
            f"condition: {condition.condition_id}; "
            f"{condition.temperature_c:g} °C; preparation {condition.preparation}"
        )
    if report.probing is not None:
        add(
            f"probing: {report.probing.chemistry} / {report.probing.method}; "
            f"coverage {report.probing.coverage:.0%}; "
            f"{report.probing.conditioning_id()}"
        )
    if report.evidence_tracks:
        statuses = report.detail.get("evidence_tracks", {}).get(
            "condition_statuses", []
        )
        add(
            f"evidence tracks: {len(report.evidence_tracks)}; "
            f"annotation only; condition status {', '.join(statuses) or '-'}"
        )
    runtime = format_duration(report.detail.get("duration_s"))
    if runtime is not None:
        add(f"elapsed runtime: {runtime}")
    add(f"{'=' * 78}")

    ran = report.tools_ran
    add(f"\ntools that ran ({len(ran)}): {', '.join(ran)}")
    if report.tools_failed:
        add("tools that failed:")
        for tool, error in report.tools_failed:
            add(f"   {tool}: {error}")
    if report.tools_skipped:
        add("tools unavailable:")
        for tool, reason in report.tools_skipped:
            add(f"   {tool}: {reason}")
    if verbose:
        add("resolved tool protocols:")
        for result in report.tool_results:
            protocol = result.applied_protocol
            applied = protocol.get("applied", {})
            unsupported = protocol.get("unsupported", {})
            condition = result.conditioning.get("status", "unknown")
            add(
                f"   {result.tool}: conditioning={condition}; "
                f"applied={', '.join(sorted(applied)) or '-'}; "
                f"unsupported={', '.join(sorted(unsupported)) or '-'}"
            )

    if "windows_screened" in report.detail:
        add(f"\nscreened {report.detail['windows_screened']} windows, "
            f"kept {report.detail.get('windows_kept', 0)} "
            f"for detailed analysis")

    candidates = report.ranked()[:top]
    if candidates:
        add(f"\n{'-' * 78}")
        add(f"ranked candidates (top {len(candidates)} of "
            f"{len(report.candidates)})")
        add(f"{'-' * 78}")
        widths = [max(9, len(label) + 1) for _, label, _ in SUMMARY_COLUMNS]
        widths[0] = max(widths[0], 12)
        header = "".join(
            label.rjust(width) for (_, label, _), width in zip(SUMMARY_COLUMNS, widths)
        )
        add(header)
        for candidate in candidates:
            cells = []
            for (key, _, _), width in zip(SUMMARY_COLUMNS, widths):
                if key == "region":
                    cells.append(candidate.region.label.rjust(width))
                elif key == "length":
                    cells.append(str(len(candidate.region)).rjust(width))
                elif key == "heuristic_rank_score":
                    value = candidate.score.value if candidate.score else None
                    cells.append(_format(value, "heuristic_rank_score").rjust(width))
                else:
                    cells.append(
                        _format(candidate.metrics.get(key), key).rjust(width)
                    )
            add("".join(cells))

    for candidate in candidates:
        if (
            not candidate.notes and not verbose
            and candidate.primary_opening_observation_id is None
        ):
            continue
        add(f"\n{'-' * 78}")
        score = candidate.score
        add(f"{candidate.region.label}  {candidate.subsequence}")
        if score:
            add(f"   heuristic rank score {score.value:.4f} "
                f"(coverage {score.coverage:.0%} of scoring weight)")
        primary_id = candidate.primary_opening_observation_id
        primary = next(
            (o for o in candidate.opening_observations if o.observation_id == primary_id),
            None,
        )
        if primary is not None:
            if primary.estimate_kind == "point":
                add(
                    f"   primary opening: {primary.tool} / {primary.sequence_scope}; "
                    f"P={_format(primary.p_unpaired, M.P_UNPAIRED)}, "
                    f"dG={_format(primary.dg_open_kcal_mol, M.DG_OPEN)}; "
                    f"{primary.conditioning_id}"
                )
            else:
                add(
                    f"   primary opening: no point estimate; {primary.tool} "
                    f"reported {primary.estimate_kind}"
                )
        if candidate.biological_evidence:
            add("   overlapping evidence (annotation only):")
            for entry in candidate.biological_evidence:
                record = entry["record"]
                interval = record["interval"]
                value = record.get("value")
                unit = record.get("unit")
                measured = "no measured value" if value is None else str(value)
                if unit:
                    measured += f" {unit}"
                add(_wrap(
                    f"      {entry['evidence_type']} {interval['start']}-"
                    f"{interval['end']}; {entry['condition_status']}; "
                    f"{measured}; source {entry['source']}",
                    indent=7,
                ))
        for note in candidate.notes:
            add(_wrap(f"   - {note}"))
        if verbose and score:
            add("   score components:")
            for component in score.components:
                if not component.present:
                    continue
                add(f"      {component.criterion.label:38} "
                    f"value={component.value:<10.4g} "
                    f"desirability={component.desirability:.3f} "
                    f"weight={component.criterion.weight}")
            if score.missing:
                add(f"      not scored (no data): {', '.join(score.missing)}")
        if verbose and candidate.consensus:
            add("   cross-tool agreement:")
            for name, agreement in sorted(candidate.consensus.items()):
                # Gated on independent evidence, not raw tool count: a
                # validation pair (rnaplfold/rnaplfold-cli) sharing one
                # calculation is one measurement, not two, and should not
                # print as "agreement across 2 tools" when nothing
                # independent has actually confirmed it.
                if agreement.n_independent < 2:
                    continue
                unit = UNITS.get(name, "")
                by_tool = ", ".join(
                    f"{tool}={value:.4g}"
                    for tool, value in sorted(agreement.values.items())
                )
                count = (
                    f"{agreement.n_independent} compatible calculation groups "
                    f"from {agreement.n_primary} primary values; "
                    f"{agreement.n} raw tools reported"
                )
                add(_wrap(
                    f"      {name}: median {agreement.median:.4g}{' ' + unit if unit else ''} "
                    f"across {count} (spread {agreement.spread:.4g}) [{by_tool}]",
                    indent=9,
                ))
                if agreement.excluded:
                    excluded = ", ".join(
                        f"{tool} ({estimand})"
                        for tool, estimand in sorted(agreement.excluded.items())
                    )
                    add(_wrap(
                        f"         not blended into the median (different "
                        f"estimand): {excluded}",
                        indent=9,
                    ))
                if agreement.excluded_conditioning:
                    excluded = ", ".join(
                        f"{tool} ({reason})"
                        for tool, reason in sorted(
                            agreement.excluded_conditioning.items()
                        )
                    )
                    add(_wrap(
                        f"         raw only (incompatible conditioning): {excluded}",
                        indent=9,
                    ))
                if agreement.excluded_protocol:
                    excluded = ", ".join(
                        f"{tool} ({', '.join(sorted(settings))})"
                        for tool, settings in sorted(
                            agreement.excluded_protocol.items()
                        )
                    )
                    add(_wrap(
                        f"         raw only (material unsupported settings): "
                        f"{excluded}",
                        indent=9,
                    ))

    warnings = list(report.warnings)
    for result in report.tool_results:
        for warning in result.warnings:
            warnings.append(f"[{result.tool}] {warning}")
    if warnings:
        add(f"\n{'-' * 78}")
        add("warnings")
        add(f"{'-' * 78}")
        for warning in warnings:
            add(_wrap(f" - {warning}"))

    add("")
    return "\n".join(out)


def _wrap(text: str, width: int = 78, indent: int = 5) -> str:
    """Wrap a bullet so continuation lines line up under the first word."""
    import textwrap
    prefix = " " * indent
    return textwrap.fill(
        text, width=width, subsequent_indent=prefix, break_long_words=False,
        break_on_hyphens=False,
    )
