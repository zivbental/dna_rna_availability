"""Command-line interface.

Three commands:

``tools``       what is installed, what is missing and how to get it
``evaluate``    characterise named regions with every applicable tool
``scan``        tile a transcript, screen cheaply, dig into the survivors
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from importlib.metadata import PackageNotFoundError, version as _pkg_version
from pathlib import Path

from .adapters.registry import DEFAULT_MAX_COST, inventory
from .core.model import ConditionSpec, ModelSettings, ProbingData, RecognitionSpec
from .core.sequence import Region, Sequence, parse_region
from .io.evidence import read_evidence_tracks
from .io.fasta import read_probing, read_sequence
from .io.report import to_json, to_profile_tsv, to_text, to_tsv
from .io.rundir import format_duration, make_run_dir, write_meta
from .pipeline.run import evaluate, scan
from .pipeline.score import DEFAULT_CRITERIA, load_weights

#: Hard ceiling on how many candidates get full visual write-ups (heatmaps +
#: structure diagrams), independent of --top. Rendering is cheap per
#: candidate but a "scan --keep 200 --html" should not silently attempt 200
#: of them.
MAX_VISUALIZED_CANDIDATES = 12


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rnavail",
        description=(
            "Estimate target-region self-accessibility under a declared "
            "folding protocol, and report what the calculation does not model."
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    tools = subparsers.add_parser(
        "tools", help="list every adapter and whether it can run here"
    )
    tools.add_argument("--json", action="store_true", help="machine-readable output")

    for name, help_text in (
        ("evaluate", "characterise specific regions in depth"),
        ("scan", "tile a transcript and rank every candidate window"),
    ):
        sub = subparsers.add_parser(name, help=help_text)
        _add_common_arguments(sub)
        if name == "evaluate":
            sub.add_argument(
                "--region", action="append", default=[], required=True,
                metavar="SPEC",
                help="target region as start-end, name:start-end, or a "
                     "literal subsequence; repeatable",
            )
        else:
            sub.add_argument("--window", type=int, default=25,
                             help="candidate window length in nt (default 25)")
            sub.add_argument("--step", type=int, default=1,
                             help="window step in nt (default 1)")
            sub.add_argument("--keep", type=int, default=25,
                             help="non-overlapping windows kept for the deep "
                                  "stage (default 25)")
            sub.add_argument("--screen-tool", default="rnaplfold",
                             help="adapter used for the cheap first pass")
            sub.add_argument(
                "--profile-tsv", metavar="FILE",
                help="write the whole-transcript accessibility profile as "
                     "its own TSV: dG_open per nucleotide for a --window "
                     "nt window starting at every position, at "
                     "single-nucleotide resolution regardless of --step",
            )

    return parser


def _add_common_arguments(sub: argparse.ArgumentParser) -> None:
    sub.add_argument("target", help="FASTA file or literal sequence")
    sub.add_argument(
        "--record", default=None,
        help="record name when the target FASTA contains multiple sequences",
    )
    sub.add_argument("--molecule", choices=("rna", "dna"), default="rna",
                     help="selects the energy parameter set (default rna)")
    sub.add_argument("--seed-length", type=int, default=10,
                     help="nucleation seed length scanned in each region")

    recognition = sub.add_argument_group("recognition event")
    recognition.add_argument("--binder-class", default="unspecified")
    recognition.add_argument("--partner-sequence", default=None)
    recognition.add_argument("--partner-chemistry", default="unspecified")
    recognition.add_argument(
        "--seed-mode", choices=("any", "five_prime", "three_prime", "fixed", "listed"),
        default="any", help="allowed seed placement within each target",
    )
    recognition.add_argument("--seed-start", type=int, action="append", default=None,
                             help="one-based seed start; repeat with --seed-mode listed")
    recognition.add_argument("--orientation", default="unspecified",
                             help="partner orientation relative to the target")
    recognition.add_argument(
        "--endpoint", default="structural_opening",
        help="declared endpoint, such as structural_opening, binding or cleavage",
    )

    model = sub.add_argument_group("folding model")
    model.add_argument("--temperature", type=float, default=37.0)
    model.add_argument("--param-set", default=None,
                       help="turner2004, turner1999, andronescu2007, "
                            "langdon2018, dna_mathews2004, dna_mathews1999")
    model.add_argument("--dangles", type=int, default=2, choices=(0, 1, 2, 3))
    model.add_argument("--max-bp-span", type=int, default=150,
                       help="longest allowed base pair in local folds (RNAplfold -L)")
    model.add_argument(
        "--global-max-bp-span", type=int, default=None,
        help="optional longest allowed base pair in whole-sequence folds; "
             "default is unrestricted",
    )
    model.add_argument("--window-size", type=int, default=200,
                       help="local folding window (RNAplfold -W)")
    model.add_argument("--salt", type=float, default=None,
                       help="monovalent salt in mol/L")
    model.add_argument("--no-lonely-pairs", action="store_true")
    model.add_argument("--no-gu", action="store_true")
    model.add_argument("--gquad", action="store_true",
                       help="allow G-quadruplex formation")
    model.add_argument("--circular", action="store_true")

    condition = sub.add_argument_group("experimental condition")
    condition.add_argument("--condition-id", default="unspecified")
    condition.add_argument("--potassium", type=float, default=None,
                           help="K+ concentration in mol/L (recorded; unmodeled)")
    condition.add_argument("--magnesium-total", type=float, default=None,
                           help="total Mg2+ in mol/L (recorded; unmodeled)")
    condition.add_argument("--magnesium-free", type=float, default=None,
                           help="free Mg2+ in mol/L (recorded; unmodeled)")
    condition.add_argument("--ph", type=float, default=None,
                           help="pH (recorded; unmodeled)")
    condition.add_argument("--incubation-seconds", type=float, default=None,
                           help="binder exposure time (recorded; unmodeled)")
    condition.add_argument("--preparation", default="unspecified",
                           help="e.g. cotranscriptional, heat_refolded, in_cell")
    condition.add_argument("--partner-concentration", type=float, default=None,
                           help="free partner concentration in mol/L (recorded; unmodeled)")
    condition.add_argument("--crowding-agent", default=None,
                           help="crowding agent identity (recorded; unmodeled)")
    condition.add_argument("--crowding-concentration", default=None,
                           help="crowding concentration and units (recorded; unmodeled)")
    condition.add_argument("--organism", default=None)
    condition.add_argument("--cell-type", default=None)
    condition.add_argument("--compartment", default=None)

    data = sub.add_argument_group("experimental data")
    data.add_argument("--shape", metavar="FILE",
                      help="SHAPE/DMS reactivities as position<TAB>reactivity")
    data.add_argument("--shape-method", default=None,
                      choices=("deigan", "zarringhalam", "eddy2"))
    data.add_argument("--probing-chemistry", default="SHAPE",
                      help="assay chemistry recorded with the probing track")
    data.add_argument(
        "--shape-slope", type=float, default=1.8, metavar="M",
        help="Deigan probing pseudoenergy slope (default 1.8)",
    )
    data.add_argument(
        "--shape-intercept", type=float, default=-0.6, metavar="B",
        help="Deigan probing pseudoenergy intercept in kcal/mol (default -0.6)",
    )
    data.add_argument(
        "--shape-beta", type=float, default=0.89, metavar="BETA",
        help="Zarringhalam probing conversion beta (default 0.89)",
    )
    data.add_argument(
        "--evidence", metavar="JSON", action="append", default=[],
        help="versioned condition-linked evidence track or manifest; repeatable "
             "(annotates reports and does not alter the structural rank)",
    )

    control = sub.add_argument_group("tools and scoring")
    control.add_argument("--tools", metavar="NAMES",
                         help="comma-separated adapter names (default: all "
                              "available)")
    control.add_argument("--weights", metavar="JSON",
                         help="JSON file overriding scoring weights")
    control.add_argument("--max-cost", type=int, default=None, metavar="N",
                         help="runtime-cost ceiling for adapters (default: "
                              "none, every applicable tool runs); pass e.g. "
                              "--max-cost 2 to skip the slowest tools for a "
                              "faster run")
    control.add_argument("--robustness", action="store_true",
                         help="re-fold under perturbed model settings and "
                              "report the spread")
    control.add_argument("--ribosnitch", action="store_true",
                         help="fold every single-point mutant of each region "
                              "on its local context and report how far one "
                              "natural substitution can move dG_open "
                              "(riboSNitch sensitivity; slower, opt in)")
    control.add_argument("--context-robustness", action="store_true",
                         help="refold each region with several different "
                              "amounts of flanking sequence and report the "
                              "spread; a candidate whose ranking depends on "
                              "how much context you happened to include is "
                              "not one you can defend")
    control.add_argument("--length-robustness", action="store_true",
                         help="refold each region at several nearby window "
                              "lengths and report the spread in opening cost "
                              "per nucleotide; the window length is a design "
                              "choice, not a physical constant, and a site "
                              "that only looks cheap at exactly one length "
                              "is a narrower bet than one that holds up "
                              "nearby")
    control.add_argument("--samples", type=int, default=2000,
                         help="ensemble samples for the sampling adapter")
    control.add_argument("--sampling-seed", type=int, default=None,
                         metavar="N",
                         help="RNG seed for ensemble sampling; runs are "
                              "reproducible by default, pass a different seed "
                              "to draw an independent ensemble")

    output = sub.add_argument_group("output")
    output.add_argument("--json", metavar="FILE", help="write the full report")
    output.add_argument("--tsv", metavar="FILE", help="write a metrics table")
    output.add_argument("--top", type=int, default=10)
    output.add_argument("-v", "--verbose", action="store_true",
                        help="show score components and cross-tool agreement")
    output.add_argument("-q", "--quiet", action="store_true")

    tracking = sub.add_argument_group("run tracking")
    tracking.add_argument(
        "--save-run", nargs="?", const="runs", default=None, metavar="DIR",
        help="save this run's json/tsv/text/html report and a meta.json into "
             "a timestamped subdirectory of DIR (default 'runs' if given "
             "with no value); repeated runs never overwrite each other",
    )
    tracking.add_argument(
        "--run-tag", default=None, metavar="LABEL",
        help="short label appended to the run's timestamped folder name",
    )

    viz = sub.add_argument_group("visual report")
    viz.add_argument(
        "--html", metavar="FILE",
        help="write a standalone HTML report with base-pair probability "
             "heatmaps and structure diagrams for the top-ranked candidates "
             "(requires matplotlib)",
    )
    viz.add_argument(
        "--no-html", action="store_true",
        help="skip the HTML report that --save-run would otherwise write "
             "automatically",
    )
    viz.add_argument(
        "--visualize-flank", type=int, default=60, metavar="N",
        help="nt of context folded on each side of a candidate for its "
             "heatmap and structure diagram (default 60); a bare site would "
             "remove exactly the neighbouring sequence that might bury or "
             "expose it",
    )


def _settings_from(args: argparse.Namespace) -> ModelSettings:
    param_set = args.param_set or (
        "dna_mathews2004" if args.molecule == "dna" else "turner2004"
    )
    window_size = max(args.window_size, args.max_bp_span)
    return ModelSettings(
        temperature_c=args.temperature,
        param_set=param_set,
        dangles=args.dangles,
        no_lonely_pairs=args.no_lonely_pairs,
        no_gu=args.no_gu,
        gquad=args.gquad,
        circular=args.circular,
        salt_molar=args.salt,
        max_bp_span=args.max_bp_span,
        global_max_bp_span=args.global_max_bp_span,
        window_size=window_size,
    )


def _load_inputs(args: argparse.Namespace):
    sequence = read_sequence(
        args.target, args.molecule, name="target", record=args.record
    )
    chemistry = args.probing_chemistry
    shape_method = args.shape_method
    if args.shape and shape_method is None:
        if chemistry.upper().startswith("DMS"):
            raise ValueError(
                "DMS probing needs an explicit --shape-method; rnavail will "
                "not choose a SHAPE conversion for it"
            )
        shape_method = "deigan"
    probing = (
        read_probing(
            args.shape, sequence, method=shape_method,
            slope=args.shape_slope, intercept=args.shape_intercept,
            beta=args.shape_beta,
            chemistry=chemistry, condition_id=args.condition_id,
            conversion_explicit=args.shape_method is not None,
        )
        if args.shape else None
    )
    evidence_tracks = tuple(
        track
        for path in args.evidence
        for track in read_evidence_tracks(path, sequence)
    )
    return sequence, probing, evidence_tracks


def _recognition_from(args: argparse.Namespace) -> RecognitionSpec:
    starts = tuple(args.seed_start or ())
    if starts and args.seed_mode not in ("fixed", "listed"):
        raise ValueError("--seed-start requires --seed-mode fixed or listed")
    if args.seed_mode == "fixed" and len(starts) != 1:
        raise ValueError("--seed-mode fixed requires exactly one --seed-start")
    return RecognitionSpec(
        binder_class=args.binder_class,
        partner_sequence=args.partner_sequence,
        partner_chemistry=args.partner_chemistry,
        seed_mode=args.seed_mode,
        seed_lengths=(args.seed_length,),
        seed_start=starts[0] if len(starts) == 1 else None,
        listed_seed_starts=starts,
        orientation=args.orientation,
        endpoint=args.endpoint,
    )


def _condition_from(args: argparse.Namespace) -> ConditionSpec:
    return ConditionSpec(
        condition_id=args.condition_id,
        temperature_c=args.temperature,
        sodium_molar=args.salt,
        potassium_molar=args.potassium,
        magnesium_total_molar=args.magnesium_total,
        magnesium_free_molar=args.magnesium_free,
        ph=args.ph,
        incubation_seconds=args.incubation_seconds,
        preparation=args.preparation,
        partner_concentration_molar=args.partner_concentration,
        crowding_agent=args.crowding_agent,
        crowding_concentration=args.crowding_concentration,
        organism=args.organism,
        cell_type=args.cell_type,
        compartment=args.compartment,
    )


def _rnavail_version() -> str:
    try:
        return _pkg_version("rnavail")
    except PackageNotFoundError:
        return "unknown"


def _run_summary(report, args: argparse.Namespace) -> dict:
    """The record written to a saved run's meta.json.

    Enough to know what was run and how it turned out without re-opening
    report.json: the exact inputs, the folding protocol, which tools ran or
    failed, and a glance at the winner.
    """
    top = report.ranked()[:5]
    return {
        "rnavail_version": _rnavail_version(),
        "mode": report.mode,
        "duration_s": report.detail.get("duration_s"),
        "duration_human": report.detail.get("duration_human"),
        "target_arg": args.target,
        "shape_arg": getattr(args, "shape", None),
        "evidence_args": list(getattr(args, "evidence", [])),
        "sequence": {
            "name": report.sequence.name,
            "length": len(report.sequence),
            "molecule": report.sequence.molecule,
            "gc_fraction": round(report.sequence.gc_fraction, 4),
            "sha256": report.sequence.sha256,
        },
        "protocol": report.settings.signature(),
        "settings": report.settings.to_dict(),
        "recognition": report.recognition.to_dict() if report.recognition else None,
        "condition": report.condition.to_dict() if report.condition else None,
        "evidence_tracks": [
            {
                "track_id": track.track_id,
                "evidence_type": track.evidence_type,
                "condition_id": track.condition_id,
                "source": track.source,
            }
            for track in getattr(report, "evidence_tracks", ())
        ],
        "source_revision": "unavailable",
        "tools_requested": args.tools.split(",") if args.tools else None,
        "tools_ran": report.tools_ran,
        "tools_failed": [{"tool": t, "error": e} for t, e in report.tools_failed],
        "tools_skipped": [{"tool": t, "reason": e} for t, e in report.tools_skipped],
        "n_candidates": len(report.candidates),
        "top_candidates": [
            {
                "region": c.region.label,
                "heuristic_rank_score": c.score.value if c.score else None,
            }
            for c in top
        ],
    }


def _build_visuals(report, args: argparse.Namespace) -> tuple[dict, dict | None]:
    """Render self-folding heatmaps/structures, plus the transcript-wide
    accessibility profile and landscape when a ``scan`` computed one.

    Returns ``({}, None)`` (rather than raising) when matplotlib is missing
    or a candidate fails to render, printing a warning instead: a broken
    image should cost the report one card's pictures, not the whole run.
    """
    from .viz.generate import build_candidate_visuals
    from .viz.mpl import available as mpl_available, unavailable_reason

    if not mpl_available():
        print(
            f"rnavail: matplotlib is not installed ({unavailable_reason()}); "
            "skipping visual report. Install it with 'pip install matplotlib'.",
            file=sys.stderr,
        )
        return {}, None

    visuals = {}
    candidates = report.ranked()[:MAX_VISUALIZED_CANDIDATES]
    for candidate in candidates:
        try:
            visuals[candidate.key] = build_candidate_visuals(
                report.sequence, candidate.region, report.settings,
                flank=args.visualize_flank, probing=report.probing,
            )
        except Exception as exc:                        # noqa: BLE001
            print(
                f"rnavail: could not render visuals for "
                f"{candidate.region.label}: {type(exc).__name__}: {exc}",
                file=sys.stderr,
            )

    transcript_visuals = None
    if getattr(report, "profile_table", None) is not None:
        from .viz.landscape import (
            render_accessibility_landscape, render_accessibility_profile,
        )
        window = report.detail.get("profile_window")
        try:
            highlights = tuple(
                (c.region.start, c.region.end, c.region.label) for c in candidates
            )
            transcript_visuals = {
                "profile": render_accessibility_profile(
                    report.profile_table, len(report.sequence), window,
                    report.settings.temperature_c, highlights=highlights,
                ),
                "landscape": render_accessibility_landscape(
                    report.profile_table, len(report.sequence),
                    max(len(row) - 1 for row in report.profile_table.values()),
                    report.settings.temperature_c,
                ),
            }
        except Exception as exc:                        # noqa: BLE001
            print(
                f"rnavail: could not render the transcript-wide "
                f"accessibility profile/landscape: {type(exc).__name__}: {exc}",
                file=sys.stderr,
            )
    return visuals, transcript_visuals


def _emit(report, args: argparse.Namespace) -> None:
    if args.json:
        to_json(report, args.json)
    if args.tsv:
        to_tsv(report, args.tsv)
    profile_tsv_arg = getattr(args, "profile_tsv", None)
    if profile_tsv_arg:
        to_profile_tsv(report, profile_tsv_arg)
    if not args.quiet:
        print(to_text(report, top=args.top, verbose=args.verbose))
    written_paths = [p for p in (args.json, args.tsv, profile_tsv_arg) if p]
    if written_paths:
        print(f"wrote {', '.join(written_paths)}", file=sys.stderr)

    wants_html = args.html or (args.save_run and not args.no_html)
    visuals, transcript_visuals = (
        _build_visuals(report, args) if wants_html else ({}, None)
    )

    if args.html:
        from .io.html_report import to_html
        to_html(report, visuals, args.html, top=args.top,
                transcript_visuals=transcript_visuals)
        print(f"wrote {args.html}", file=sys.stderr)

    if getattr(args, "save_run", None):
        run_dir = make_run_dir(args.save_run, tag=args.run_tag)
        to_json(report, run_dir / "report.json")
        to_tsv(report, run_dir / "report.tsv")
        to_profile_tsv(report, run_dir / "report.profile.tsv")
        (run_dir / "report.txt").write_text(
            to_text(report, top=args.top, verbose=args.verbose)
        )
        if not args.no_html:
            from .io.html_report import to_html
            to_html(report, visuals, run_dir / "report.html", top=args.top,
                    transcript_visuals=transcript_visuals)
        write_meta(run_dir, _run_summary(report, args))
        print(f"run saved to {run_dir}/", file=sys.stderr)


def cmd_tools(args: argparse.Namespace) -> int:
    rows = inventory()
    if args.json:
        print(json.dumps(rows, indent=2))
        return 0

    ready = [r for r in rows if r["available"]]
    print(f"{len(ready)} of {len(rows)} adapters available\n")
    current_tier = None
    for row in rows:
        if row["tier"] != current_tier:
            current_tier = row["tier"]
            print(f"\n{current_tier.upper()}")
        mark = "OK  " if row["available"] else "--  "
        version = f"  [{row['version']}]" if row["version"] else ""
        print(f"  {mark}{row['name']:24}{row['description']}{version}")
        if not row["available"]:
            print(f"      unavailable: {row['reason']}")
            if row["hint"]:
                print(f"      fix: {row['hint']}")
    return 0


def cmd_evaluate(args: argparse.Namespace) -> int:
    sequence, probing, evidence_tracks = _load_inputs(args)
    regions = [parse_region(spec, sequence) for spec in args.region]
    criteria = load_weights(args.weights) if args.weights else DEFAULT_CRITERIA

    started = time.perf_counter()
    report = evaluate(
        sequence=sequence,
        regions=regions,
        settings=_settings_from(args),
        probing=probing,
        evidence_tracks=evidence_tracks,
        recognition=_recognition_from(args),
        condition=_condition_from(args),
        seed_length=args.seed_length,
        tools=args.tools.split(",") if args.tools else None,
        criteria=criteria,
        robustness=args.robustness,
        ribosnitch=args.ribosnitch,
        context_robustness=args.context_robustness,
        length_robustness=args.length_robustness,
        max_cost=args.max_cost if args.max_cost is not None else DEFAULT_MAX_COST,
        options={
            "samples": args.samples,
            **({"sampling_seed": args.sampling_seed}
               if args.sampling_seed is not None else {}),
        },
        progress=_progress(args),
    )
    report.detail["duration_s"] = round(time.perf_counter() - started, 3)
    report.detail["duration_human"] = format_duration(report.detail["duration_s"])
    _emit(report, args)
    return 0


def cmd_scan(args: argparse.Namespace) -> int:
    sequence, probing, evidence_tracks = _load_inputs(args)
    criteria = load_weights(args.weights) if args.weights else DEFAULT_CRITERIA

    started = time.perf_counter()
    report = scan(
        sequence=sequence,
        window=args.window,
        step=args.step,
        settings=_settings_from(args),
        probing=probing,
        evidence_tracks=evidence_tracks,
        recognition=_recognition_from(args),
        condition=_condition_from(args),
        seed_length=args.seed_length,
        keep=args.keep,
        screen_tool=args.screen_tool,
        tools=args.tools.split(",") if args.tools else None,
        criteria=criteria,
        robustness=args.robustness,
        ribosnitch=args.ribosnitch,
        context_robustness=args.context_robustness,
        length_robustness=args.length_robustness,
        max_cost=args.max_cost if args.max_cost is not None else DEFAULT_MAX_COST,
        options={
            "samples": args.samples,
            **({"sampling_seed": args.sampling_seed}
               if args.sampling_seed is not None else {}),
        },
        progress=_progress(args),
    )
    report.detail["duration_s"] = round(time.perf_counter() - started, 3)
    report.detail["duration_human"] = format_duration(report.detail["duration_s"])
    _emit(report, args)
    return 0


def _progress(args: argparse.Namespace):
    if args.quiet:
        return lambda message: None
    return lambda message: print(f"  .. {message}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    handlers = {
        "tools": cmd_tools,
        "evaluate": cmd_evaluate,
        "scan": cmd_scan,
    }
    try:
        return handlers[args.command](args)
    except (FileNotFoundError, ValueError, RuntimeError, KeyError) as exc:
        print(f"rnavail: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
