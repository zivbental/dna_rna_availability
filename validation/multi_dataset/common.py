"""Canonical experimental records and statistics; no folding on import."""
from __future__ import annotations

from collections import defaultdict
from contextlib import contextmanager
import gzip
import hashlib
import json
import math
from pathlib import Path
import statistics
import tempfile

from validation.controls_2010.compare_all_genes import (
    correlation_stats, sha256, summarize_models,
)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


def open_text(path, mode="rt"):
    return gzip.open(path, mode) if str(path).endswith(".gz") else open(path, mode)


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, suffix=".tmp", delete=False) as f:
        temporary = Path(f.name)
    try:
        with open_text(temporary, "wt") if not str(path).endswith(".gz") else gzip.open(temporary, "wt") as stream:
            json.dump(value, stream, allow_nan=False, separators=(",", ":"))
            stream.write("\n")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def validate_record(record):
    r = dict(record)
    for key in ("id", "gene_id", "sequence", "measurements"):
        if key not in r:
            raise ValueError(f"Record missing {key}")
    r["sequence"] = r["sequence"].upper().replace("T", "U")
    if not r["id"] or not r["sequence"]:
        raise ValueError("Empty record ID or sequence")
    expected = hashlib.sha256(r["sequence"].encode()).hexdigest()
    if r.get("sequence_sha256", expected) != expected:
        raise ValueError(f"Sequence hash mismatch: {r['id']}")
    r["sequence_sha256"] = expected
    scores = {}
    for pos, value in r["measurements"].items():
        p = int(pos)
        if str(p) != str(pos) or not 1 <= p <= len(r["sequence"]):
            raise ValueError(f"Invalid one-based position {pos}: {r['id']}")
        if p in scores or not math.isfinite(float(value)):
            raise ValueError(f"Duplicate/nonfinite measurement: {r['id']}")
        scores[p] = float(value)
    r["measurements"] = scores
    return r


def read_records(path):
    seen = set()
    with open_text(path) as stream:
        for line in stream:
            if not line.strip():
                continue
            r = validate_record(json.loads(line))
            if r["id"] in seen:
                raise ValueError(f"Duplicate record ID: {r['id']}")
            seen.add(r["id"])
            yield r


def measured_window(record, start, end, bases, coverage, minimum):
    """Coverage denominator is assay-observable bases, including missing ones."""
    eligible = [p for p in range(start, end + 1) if record["sequence"][p-1] in bases]
    observed = [p for p in eligible if p in record["measurements"]]
    if len(observed) < minimum or not eligible or len(observed)/len(eligible) < coverage:
        return None
    return observed


def ranking_stats(rows, feature, top_fraction, min_pairs):
    valid = [r for r in rows if r.get(feature) is not None]
    stats = correlation_stats([r["experimental_availability"] for r in valid],
                              [r[feature] for r in valid], min_pairs)
    stats["top_fraction_gain"] = None
    stats["top_fraction_gain_scaled"] = None
    if len(valid) >= min_pairs:
        values = [r["experimental_availability"] for r in valid]
        k = max(1, math.ceil(len(valid)*top_fraction))
        # Fractional inclusion of ties at the cutoff avoids positional bias.
        cutoff = sorted((r[feature] for r in valid), reverse=True)[k-1]
        above = [r["experimental_availability"] for r in valid if r[feature] > cutoff]
        tied = [r["experimental_availability"] for r in valid if r[feature] == cutoff]
        selected = (sum(above)+(k-len(above))*statistics.mean(tied))/k
        gain = selected-statistics.mean(values)
        stats["top_fraction_gain"] = gain
        spread = statistics.pstdev(values)
        stats["top_fraction_gain_scaled"] = gain/spread if spread else None
    return stats


def aggregate(results, min_pairs):
    groups = defaultdict(list)
    for r in results:
        for key, stats in r.get("statistics", {}).items():
            groups[key].append(stats)
    summaries = summarize_models(groups, min_pairs)
    for key, entries in groups.items():
        for metric in ("top_fraction_gain", "top_fraction_gain_scaled"):
            values = [s[metric] for s in entries if s.get(metric) is not None]
            summaries[key]["median_"+metric] = statistics.median(values) if values else None
    return summaries


@contextmanager
def file_lock(path):
    """POSIX advisory locks are released even when a worker is terminated."""
    import fcntl
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        yield
        fcntl.flock(stream, fcntl.LOCK_UN)
