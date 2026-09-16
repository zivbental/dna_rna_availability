"""Benchmark the unchanged rnavail pipeline against prepared probing datasets."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
import csv
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import statistics
import sys
import time

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from validation.multi_dataset.common import (
    aggregate, atomic_json, correlation_stats, digest, file_lock, measured_window,
    open_text, ranking_stats, read_records, sha256,
)

CONFIG = {}
OUTPUT = None


def progress(message):
    # A detached terminal must never turn a finished prediction into a failure.
    try:
        print(message, flush=True)
    except BrokenPipeError:
        sys.stdout = open(os.devnull, "w")


def initialize(config, output):
    global CONFIG, OUTPUT
    CONFIG, OUTPUT = config, Path(output)


def predict(sequence):
    from rnavail.core.sequence import Sequence, Region
    from rnavail.core.model import ModelSettings, RecognitionSpec
    from rnavail.core.result import M
    from rnavail.pipeline.run import evaluate
    from rnavail.pipeline.score import DEFAULT_CRITERIA, score_candidate

    key = digest({"sequence": sequence, "prediction": CONFIG["prediction"]})
    path = OUTPUT/"prediction_cache"/(key+".json.gz")
    with file_lock(path.with_suffix(".lock")):
        if path.exists():
            with open_text(path) as stream:
                saved = json.load(stream)
            if saved["cache_key"] != key:
                raise ValueError("Prediction cache identity mismatch")
            if not CONFIG["retry_failed"] or not saved["has_failures"]:
                return saved
        p = CONFIG["prediction"]
        n = len(sequence)
        footprint, step = p["footprint"], p["step"]
        # Every window is evaluated; no prediction-dependent shortlist.
        windows = [Region(s, s+footprint-1) for s in range(1, n-footprint+2, step)]
        singles = [Region(i, i) for i in range(1, n+1)]
        settings = ModelSettings(temperature_c=p["temperature"],
            window_size=min(n, p["window_size"]),
            max_bp_span=min(n, p["max_bp_span"]),
            max_unpaired=min(n, max(footprint, p["seed_length"])))
        global_limit = p["global_max_length"]
        selected_tools = [t for t in p["tools"] if t == "rnaplfold" or not global_limit or n <= global_limit]
        skipped = {t: f"Sequence length {n} exceeds explicit global-model limit {global_limit}"
                   for t in p["tools"] if t not in selected_tools}
        report = evaluate(Sequence("benchmark", sequence), singles+windows,
            settings=settings, seed_length=p["seed_length"], tools=selected_tools,
            recognition=RecognitionSpec(binder_class="unspecified", seed_lengths=(p["seed_length"],)),
            robustness=p["robustness"], length_robustness=p["length_robustness"],
            max_cost=None)
        model_predictions, protocols = {}, {}
        failures = {}
        for tool in report.tool_results:
            protocols[tool.tool] = {"status": tool.status, "version": tool.version,
                "model_family": tool.model_family, "algorithm": tool.algorithm,
                "applied_protocol": tool.applied_protocol, "warnings": tool.warnings}
            if not tool.ok:
                failures[tool.tool] = tool.error
                continue
            model_predictions[tool.tool] = [
                tool.regions.get(f"{i}-{i}").get(M.MEAN_BASE_UNPAIRED)
                if f"{i}-{i}" in tool.regions else None for i in range(1, n+1)]
        candidates = []
        for candidate in report.candidates:
            if len(candidate.region) != footprint:
                continue
            c = {"start": candidate.region.start, "end": candidate.region.end,
                "metrics": candidate.metrics, "pipeline_score": candidate.score.value,
                "score_coverage": candidate.score.coverage,
                "score_components": [x for x in candidate.score.to_dict()["components"]],
                "primary_opening_observation_id": candidate.primary_opening_observation_id,
                "opening_observations": [o.to_dict() for o in candidate.opening_observations]}
            for suffix, omitted in [("without_seed", M.SEED_P_UNPAIRED),
                                     ("without_opening_cost", M.DG_OPEN_PER_NT)]:
                criteria = [x for x in DEFAULT_CRITERIA if x.key != omitted]
                score = score_candidate(candidate.metrics, criteria)
                c["pipeline_"+suffix] = score.value if score.coverage else None
            candidates.append(c)
        saved = {"cache_key": key, "sequence_sha256": hashlib.sha256(sequence.encode()).hexdigest(),
            "per_base": model_predictions, "candidates": candidates,
            "protocols": protocols, "failures": failures,
            "has_failures": bool(failures), "model_skips": skipped, "warnings": report.warnings,
            "recognition_scoring": report.detail.get("recognition_scoring")}
        atomic_json(path, saved)
        return saved


def compare(record, dataset, predictions):
    direction = 1 if dataset["higher_is"] == "available" else -1
    bases = dataset["observable_bases"]
    observed = {p: direction*v for p, v in record["measurements"].items()
                if record["sequence"][p-1] in bases}
    statistics_by_feature = {}
    for model, values in predictions["per_base"].items():
        positions = [p for p in observed if values[p-1] is not None]
        statistics_by_feature["per_base:"+model] = correlation_stats(
            [observed[p] for p in positions], [values[p-1] for p in positions], CONFIG["min_pairs"])
    rows = []
    from rnavail.core.result import M
    for candidate in predictions["candidates"]:
        start, end = candidate["start"], candidate["end"]
        positions = measured_window(record, start, end, bases, CONFIG["coverage"], CONFIG["min_window_bases"])
        if positions is None:
            continue
        metrics = candidate["metrics"]
        row = {"start": start, "end": end, "n_measured": len(positions),
            "experimental_availability": statistics.mean(observed[p] for p in positions),
            "pipeline_score": candidate["pipeline_score"] if candidate["score_coverage"] else None,
            "pipeline_without_seed": candidate["pipeline_without_seed"],
            "pipeline_without_opening_cost": candidate["pipeline_without_opening_cost"],
            "score_coverage": candidate["score_coverage"],
            "full_p": metrics.get(M.P_UNPAIRED), "seed_p": metrics.get(M.SEED_P_UNPAIRED),
            "negative_dg_open_per_nt": -metrics[M.DG_OPEN_PER_NT] if M.DG_OPEN_PER_NT in metrics else None,
            "seed_start": metrics.get(M.SEED_START)}
        for model, values in predictions["per_base"].items():
            all_values = values[start-1:end]
            row["mean_base:"+model] = statistics.mean(all_values) if all(v is not None for v in all_values) else None
            measured = [values[p-1] for p in positions]
            row["mean_observed_base:"+model] = statistics.mean(measured) if all(v is not None for v in measured) else None
        rows.append(row)
    features = {"pipeline_score", "pipeline_without_seed", "pipeline_without_opening_cost",
                "full_p", "seed_p", "negative_dg_open_per_nt"}
    features.update(k for row in rows for k in row if k.startswith("mean_"))
    for feature in sorted(features):
        statistics_by_feature["window:"+feature] = ranking_stats(rows, feature, CONFIG["top_fraction"], CONFIG["min_pairs"])
    # Direct ranking comparisons must use exactly the same measured windows.
    matched_features = {"pipeline_score", "pipeline_without_seed", "pipeline_without_opening_cost"}
    matched_features.update(k for k in features if k.startswith("mean_base:") or k.startswith("mean_observed_base:"))
    matched = [row for row in rows if all(row.get(k) is not None for k in matched_features)]
    for row in rows:
        row["matched_comparison_cohort"] = all(row.get(k) is not None for k in matched_features)
    for feature in sorted(matched_features):
        statistics_by_feature["matched_window:"+feature] = ranking_stats(matched, feature, CONFIG["top_fraction"], CONFIG["min_pairs"])
    seeds = []
    for row in rows:
        if row["seed_start"] is None or row["seed_p"] is None:
            continue
        start = int(row["seed_start"])
        positions = measured_window(record, start, start+CONFIG["prediction"]["seed_length"]-1,
            bases, CONFIG["coverage"], min(CONFIG["min_window_bases"], CONFIG["prediction"]["seed_length"]))
        if positions:
            seeds.append({"experimental_availability": statistics.mean(observed[p] for p in positions),
                          "seed_p": row["seed_p"]})
    statistics_by_feature["seed:own_measurements"] = ranking_stats(seeds, "seed_p", CONFIG["top_fraction"], CONFIG["min_pairs"])
    return statistics_by_feature, rows


def work(item):
    dataset, record = item
    key = digest({"dataset": dataset["id"], "record": record["id"]})
    path = OUTPUT/"records"/key/"result.json"
    if path.exists():
        old = json.loads(path.read_text())
        if old["fingerprint"] != CONFIG["fingerprint"]:
            raise ValueError("Checkpoint fingerprint mismatch")
        if not CONFIG["retry_failed"] or old["status"] not in ("failed", "partial_model_failure"):
            if not (path.parent/"REPORT.md").exists(): write_record_report(path.parent, old)
            return old
    result = {"dataset": dataset["id"], "study": dataset["study"],
        "id": record["id"], "gene_id": record["gene_id"], "sequence_sha256": record["sequence_sha256"],
        "record_metadata": {k: v for k, v in record.items() if k not in ("sequence", "measurements")},
        "length": len(record["sequence"]), "n_measured": len(record["measurements"]),
        "fingerprint": CONFIG["fingerprint"], "status": "ok", "statistics": {}}
    started = time.monotonic()
    try:
        if set(record["sequence"])-set("ACGU"):
            result["status"] = "ambiguous_sequence"
        elif CONFIG["max_length"] and result["length"] > CONFIG["max_length"]:
            result["status"] = "length_limit"
        elif sum(record["sequence"][p-1] in dataset["observable_bases"] for p in record["measurements"]) < CONFIG["min_pairs"]:
            result["status"] = "insufficient_measurements"
        else:
            prediction = predict(record["sequence"])
            result["prediction_cache_key"] = prediction["cache_key"]
            result["model_failures"] = prediction["failures"]
            result["model_skips"] = prediction["model_skips"]
            result["prediction_warnings"] = prediction["warnings"]
            if prediction["has_failures"]:
                result["status"] = "partial_model_failure" if prediction["per_base"] else "failed"
            result["statistics"], rows = compare(record, dataset, prediction)
            result["n_covered_windows"] = len(rows)
            result["n_matched_windows"] = sum(r["matched_comparison_cohort"] for r in rows)
            result["prediction_protocols"] = prediction["protocols"]
            coverages = [r["score_coverage"] for r in rows]
            result["score_coverage"] = {"minimum": min(coverages), "median": statistics.median(coverages),
                "maximum": max(coverages)} if coverages else {}
            if CONFIG["details"] and rows:
                details_path = path.parent/"windows.tsv.gz"
                details_path.parent.mkdir(parents=True, exist_ok=True)
                with gzip.open(details_path.with_suffix(".tmp"), "wt") as stream:
                    columns = sorted({k for row in rows for k in row})
                    writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t")
                    writer.writeheader(); writer.writerows(rows)
                details_path.with_suffix(".tmp").replace(details_path)
    except Exception as exc:
        result.update(status="failed", error=f"{type(exc).__name__}: {exc}")
    result["runtime_s"] = time.monotonic()-started
    atomic_json(path, result)
    write_record_report(path.parent, result)
    return result


def write_record_report(folder, result):
    lines = [f"# {result['dataset']} / {result['id']}\n\n",
        f"Gene: {result['gene_id']}. RNA length: {result['length']}. Measured bases: {result['n_measured']}. Status: {result['status']}.\n\n"]
    for key in ("error", "model_failures", "model_skips", "score_coverage"):
        if result.get(key): lines.append(f"{key}: {result[key]}\n\n")
    lines.append("| Feature | Pairs | Pearson | Spearman | Scaled top-fraction gain |\n|---|---:|---:|---:|---:|\n")
    def fmt(x): return "undefined" if x is None else f"{x:.4f}"
    for name, stats in sorted(result["statistics"].items()):
        lines.append(f"| {name} | {stats['n_pairs']} | {fmt(stats['pearson'])} | {fmt(stats['spearman'])} | {fmt(stats.get('top_fraction_gain_scaled'))} |\n")
    temporary = folder/"REPORT.md.tmp"
    temporary.write_text("".join(lines)); temporary.replace(folder/"REPORT.md")


def bounded_results(items, workers):
    if workers == 1:
        initialize(CONFIG, OUTPUT)
        for item in items:
            yield work(item)
        return
    with ProcessPoolExecutor(max_workers=workers, initializer=initialize, initargs=(CONFIG, str(OUTPUT))) as pool:
        pending = set()
        iterator = iter(items)
        exhausted = False
        while pending or not exhausted:
            while not exhausted and len(pending) < 2*workers:
                try:
                    pending.add(pool.submit(work, next(iterator)))
                except StopIteration:
                    exhausted = True
            if pending:
                done, pending = wait(pending, timeout=30, return_when=FIRST_COMPLETED)
                if not done:
                    progress(f"Still computing; {len(pending)} transcripts queued/running")
                for future in done:
                    yield future.result()


def write_reports(results, datasets):
    by_dataset = defaultdict(list)
    for r in results:
        by_dataset[r["dataset"]].append(r)
    selected = sum(min(d["n_records"], CONFIG["limit"]) if CONFIG["limit"] else d["n_records"] for d in datasets)
    summary = {"fingerprint": CONFIG["fingerprint"], "completed_records": len(results), "selected_records": selected,
        "complete": len(results) == selected,
        "status_counts": dict(Counter(r["status"] for r in results)), "datasets": {}}
    lines = ["# Multi-dataset RNA availability benchmark\n\n",
        f"Completed {len(results)} of {selected} selected records.\n\n",
        "Experimental scores are oriented so higher means more available; positive association is expected.\n\n",
        "Windows and per-base statistics are reported separately. Window comparisons test ranking against a per-base probing proxy, not experimentally measured simultaneous opening. No probing scores constrain predictions.\n\n",
        "Conditions, assays and studies are never pooled into one correlation. No independence-based significance tests are used.\n\n"]
    table_rows = []
    for dataset in datasets:
        records = by_dataset[dataset["id"]]
        stats = aggregate(records, CONFIG["min_pairs"])
        counts = dict(Counter(r["status"] for r in records))
        exclusions = dict(Counter(t for r in records for t in r.get("model_skips", {})))
        failures = dict(Counter(t for r in records for t in r.get("model_failures", {})))
        summary["datasets"][dataset["id"]] = {"metadata": dataset, "status_counts": counts,
            "model_skip_counts": exclusions, "model_failure_counts": failures, "statistics": stats}
        lines.extend([f"## {dataset['id']}\n\n", f"Study: {dataset['study']}. Conditions: {dataset.get('conditions', {})}. Statuses: {counts}.\n\n",
            f"Model exclusions: {exclusions}. Model failures: {failures}.\n\n",
            "| Feature | Observations | Pooled Pearson | Median per-record Spearman | Median scaled top-fraction gain |\n|---|---:|---:|---:|---:|\n"])
        for feature, s in sorted(stats.items()):
            def fmt(x): return "undefined" if x is None else f"{x:.4f}"
            lines.append(f"| {feature} | {s['n_pairs']} | {fmt(s['pooled_pearson'])} | {fmt(s['median_gene_spearman'])} | {fmt(s['median_top_fraction_gain_scaled'])} |\n")
        for r in sorted(records, key=lambda r: r["id"]):
            for feature, s in r["statistics"].items() or [("", {})]:
                table_rows.append({"dataset": r["dataset"], "study": r["study"], "id": r["id"], "gene_id": r["gene_id"],
                    "sequence_sha256": r["sequence_sha256"], "status": r["status"], "length": r["length"],
                    "feature": feature, "n_pairs": s.get("n_pairs"), "pearson": s.get("pearson"), "spearman": s.get("spearman"),
                    "top_fraction_gain_scaled": s.get("top_fraction_gain_scaled"), "error": r.get("error"),
                    "checkpoint": f"records/{digest({'dataset':r['dataset'],'record':r['id']})}/result.json"})
    atomic_json(OUTPUT/"summary.json", summary)
    (OUTPUT/"REPORT.md").write_text("".join(lines))
    if table_rows:
        with (OUTPUT/"per_record.tsv").open("w") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(table_rows[0]), delimiter="\t")
            writer.writeheader(); writer.writerows(table_rows)


def main(argv=None):
    global CONFIG, OUTPUT
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--prepared-dir", type=Path, default=Path(__file__).parent/"work/prepared")
    p.add_argument("--output-dir", type=Path, default=Path(__file__).parent/"work/results")
    p.add_argument("--dataset", action="append")
    p.add_argument("--tools", default="rnaplfold,rnafold")
    p.add_argument("--workers", type=int, default=1)
    p.add_argument("--temperature", type=float, default=37.)
    p.add_argument("--window-size", type=int, default=200)
    p.add_argument("--max-bp-span", type=int, default=150)
    p.add_argument("--footprint", type=int, default=20)
    p.add_argument("--seed-length", type=int, default=8)
    p.add_argument("--step", type=int, default=1)
    p.add_argument("--min-pairs", type=int, default=20)
    p.add_argument("--coverage", type=float, default=.8)
    p.add_argument("--min-window-bases", type=int, default=4)
    p.add_argument("--top-fraction", type=float, default=.1)
    p.add_argument("--max-length", type=int)
    p.add_argument("--global-max-length", type=int, default=6000,
                   help="Skip global models above this RNA length, report exclusions; 0 disables limit (default: 6000)")
    p.add_argument("--limit", type=int, help="Explicit per-dataset smoke-test limit")
    p.add_argument("--robustness", action="store_true")
    p.add_argument("--length-robustness", action="store_true")
    p.add_argument("--details", action="store_true")
    p.add_argument("--resume", action="store_true")
    p.add_argument("--retry-failed", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)
    if not (args.workers > 0 and 2 <= args.footprint <= args.window_size and 1 <= args.seed_length <= args.footprint
            and 1 <= args.max_bp_span <= args.window_size and args.step > 0 and args.min_pairs >= 3
            and 0 < args.coverage <= 1 and 0 < args.top_fraction <= 1 and math.isfinite(args.temperature) and args.temperature > -273.15
            and args.global_max_length >= 0
            and args.min_window_bases > 0 and (args.max_length is None or args.max_length > 0)
            and (args.limit is None or args.limit > 0)):
        p.error("Invalid sizes, coverage, workers, temperature or minimum observations")
    if args.retry_failed and not args.resume:
        p.error("--retry-failed requires --resume")
    from rnavail.adapters.registry import get
    tools = args.tools.split(",")
    allowed = {"rnaplfold", "rnafold", "rnastructure-partition", "contrafold", "eternafold"}
    if not set(tools) <= allowed or len(set(tools)) != len(tools) or "rnaplfold" not in tools:
        p.error("Use unique per-base tools including rnaplfold")
    inventory = {name: {"available": get(name).availability().available, "version": get(name).availability().version} for name in tools}
    if any(not v["available"] for v in inventory.values()):
        p.error(f"Requested tools unavailable: {inventory}; install them first")
    index = json.loads((args.prepared_dir/"index.json").read_text())
    from validation.multi_dataset.prepare import validate_dataset
    if index.get("schema_version") != 1 or len({d["id"] for d in index["datasets"]}) != len(index["datasets"]):
        p.error("Invalid prepared dataset index")
    for d in index["datasets"]: validate_dataset(d)
    datasets = [d for d in index["datasets"] if not args.dataset or d["id"] in args.dataset]
    if not datasets or args.dataset and set(args.dataset)-{d["id"] for d in datasets}:
        p.error("Unknown/empty dataset selection")
    implementation = {str(path.relative_to(REPO)): sha256(path) for path in
        sorted(list((REPO/"rnavail").rglob("*.py"))+list(Path(__file__).parent.glob("*.py"))+
               [REPO/"validation/controls_2010/compare_all_genes.py"])}
    for path in (REPO/"rnavail/adapters/data").glob("*"):
        if path.is_file(): implementation[str(path.relative_to(REPO))] = sha256(path)
    prediction = {k: getattr(args, k) for k in ["temperature", "window_size", "max_bp_span", "footprint", "seed_length", "step", "robustness", "length_robustness", "global_max_length"]}
    prediction.update(tools=tools, inventory=inventory, implementation=implementation)
    inputs = {d["id"]: sha256(args.prepared_dir/d["records"]) for d in datasets}
    if any(inputs[d["id"]] != d["records_sha256"] for d in datasets):
        p.error("Prepared input checksum mismatch; do not run changed inputs against an old index")
    CONFIG = {k: getattr(args, k) for k in ["min_pairs", "coverage", "min_window_bases", "top_fraction", "max_length", "limit", "details"]}
    CONFIG.update(prediction=prediction, datasets=datasets, inputs=inputs)
    CONFIG["fingerprint"] = digest(CONFIG)
    CONFIG["retry_failed"] = args.retry_failed
    OUTPUT = args.output_dir
    def items():
        for dataset in datasets:
            for i, record in enumerate(read_records(args.prepared_dir/dataset["records"])):
                if args.limit and i >= args.limit: break
                yield dataset, record
    if args.dry_run:
        counts = Counter(d["id"] for d, r in items())
        progress(f"No folds run. Selected records: {dict(counts)}; tools: {inventory}")
        return 0
    if OUTPUT.exists() and not args.resume:
        p.error("Output exists; choose a new directory or --resume")
    manifest = OUTPUT/"manifest.json"
    if args.resume and OUTPUT.exists() and not manifest.exists() and any(OUTPUT.iterdir()):
        p.error("Cannot resume a nonempty output directory without its manifest")
    if manifest.exists() and json.loads(manifest.read_text())["fingerprint"] != CONFIG["fingerprint"]:
        p.error("Resume configuration/data/code/version mismatch; choose a new output directory")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    if not manifest.exists():
        atomic_json(manifest, {"fingerprint": CONFIG["fingerprint"], "config": CONFIG,
            "created_utc": datetime.now(timezone.utc).isoformat(), "initial_workers": args.workers})
    results = []
    try:
        for r in bounded_results(items(), args.workers):
            results.append(r)
            progress(f"[{len(results)}] {r['dataset']} / {r['id']}: {r['status']}")
    finally:
        write_reports(results, datasets)
    failed = sum(r["status"] in ("failed", "partial_model_failure") for r in results)
    progress(f"Finished {len(results)} records; {failed} failures. Report: {OUTPUT/'REPORT.md'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
