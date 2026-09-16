"""Download original experimental tracks and project them onto annotated RNAs.

No predictions or folding are performed by this command.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import gzip
import json
import math
from pathlib import Path
import shutil
import sqlite3
import sys
import tarfile
import time
from urllib.parse import urlencode, unquote
from urllib.request import Request, urlopen

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from validation.multi_dataset.common import atomic_json, digest, open_text, sha256, validate_record

RASP = "https://rasp2.zhanglab.net"


def validate_dataset(d):
    for k in ("id", "study", "assay", "higher_is", "observable_bases", "conditions"):
        if k not in d:
            raise ValueError(f"Dataset missing {k}")
    if not d["id"] or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for c in d["id"]):
        raise ValueError("Dataset ID must contain letters, digits, underscore or hyphen")
    if d["higher_is"] not in ("available", "paired") or not d["observable_bases"] or set(d["observable_bases"])-set("ACGU"):
        raise ValueError("Invalid assay direction or observable bases")
    if not isinstance(d["conditions"], dict):
        raise ValueError("conditions must be a dictionary")


def download(url, cache):
    """Atomic downloads, bounded retries and content-checked reuse; never unzip paths."""
    cache.mkdir(parents=True, exist_ok=True)
    key = digest(url)
    payload, metadata = cache/(key+".payload"), cache/(key+".json")
    if payload.exists() and metadata.exists():
        info = json.loads(metadata.read_text())
        if info["url"] != url or info["sha256"] != sha256(payload):
            raise ValueError(f"Downloaded cache content changed: {payload}")
        return payload, info
    temporary = payload.with_suffix(".part")
    for attempt in range(3):
        try:
            print(f"Downloading {url}", flush=True)
            request = Request(url, headers={"User-Agent": "rnavail-availability-benchmark/1"})
            with urlopen(request, timeout=60) as response, temporary.open("wb") as stream:
                expected = response.headers.get("Content-Length")
                count, last = 0, time.monotonic()
                for chunk in iter(lambda: response.read(1024*1024), b""):
                    stream.write(chunk); count += len(chunk)
                    if time.monotonic()-last > 15:
                        print(f"  {count/1048576:.1f} MiB received", flush=True)
                        last = time.monotonic()
                if expected is not None and count != int(expected):
                    raise ValueError("Truncated HTTP response")
            temporary.replace(payload)
            info = {"url": url, "sha256": sha256(payload), "bytes": count,
                    "downloaded_utc": datetime.now(timezone.utc).isoformat()}
            atomic_json(metadata, info)
            return payload, info
        except Exception:
            temporary.unlink(missing_ok=True)
            if attempt == 2:
                raise
            time.sleep(2**attempt)


def gzip_asset(url, cache):
    """RASP serves single assets either as gzip or a TAR containing one gzip."""
    payload, info = download(url, cache)
    target = cache/(digest(url)+".gz")
    extraction = target.with_suffix(".extraction.json")
    if target.exists() and extraction.exists():
        saved = json.loads(extraction.read_text())
        if saved["payload_sha256"] == info["sha256"] and saved["sha256"] == sha256(target):
            return target, dict(info, asset_sha256=saved["sha256"], archive_member=saved["archive_member"])
        raise ValueError(f"Extracted cache content changed: {target}")
    temporary = target.with_suffix(".part")
    try:
        with payload.open("rb") as stream:
            magic = stream.read(2)
        member_name = None
        if magic == b"\x1f\x8b":
            shutil.copyfile(payload, temporary)
        else:
            with tarfile.open(payload, "r:*") as archive:
                members = [m for m in archive if m.isfile()]
                if len(members) != 1 or not members[0].name.endswith(".gz"):
                    raise ValueError("Expected exactly one gzip file in downloaded archive")
                member_name = members[0].name
                with archive.extractfile(members[0]) as stream, temporary.open("wb") as out:
                    shutil.copyfileobj(stream, out)
        # Check magic now; gzip CRC is checked while the whole asset is parsed.
        with temporary.open("rb") as stream:
            if stream.read(2) != b"\x1f\x8b":
                raise ValueError("Downloaded asset is not gzip")
        temporary.replace(target)
        saved = {"payload_sha256": info["sha256"], "sha256": sha256(target), "archive_member": member_name}
        atomic_json(extraction, saved)
        return target, dict(info, asset_sha256=saved["sha256"], archive_member=member_name)
    finally:
        temporary.unlink(missing_ok=True)


def rasp_asset(kind, name, cache):
    return gzip_asset(RASP+"/api/downloadfile/?"+urlencode({"filetype": kind, "filelist": name}), cache)


def track_metadata(d, cache):
    path, provenance = download(RASP+"/api/query_bwfiles/?"+urlencode({"species": d["species"]}), cache)
    response = json.loads(path.read_text())
    if response.get("error_code") != 0:
        raise ValueError("RASP metadata query failed")
    matches = [r for r in response["bw_files"] if r.get("bed_file_path", "").strip() == d["track"]
               and r.get("tracktype") == "raw" and r.get("doi") == d["doi"]
               and r.get("condition") == d["track_condition"] and r.get("species") == d["species"]]
    if not matches:
        raise ValueError(f"Original, non-imputed RASP track/DOI/condition not found: {d['id']}")
    return {"catalog_query": provenance, "tracks": matches,
            "processing": "RASP original/non-imputed processed score track; no additional normalization applied"}


def bed_database(path, cache, missing_values=()):
    """A disk index keeps large mouse tracks out of RAM; zero/negative are measured."""
    identity = {"bed_sha256": sha256(path), "parser_version": 2, "missing_values": list(missing_values)}
    destination = cache/(digest(identity)+".sqlite")
    audit_path = destination.with_suffix(".audit.json")
    if destination.exists() and audit_path.exists():
        return destination, json.loads(audit_path.read_text())
    temporary = destination.with_suffix(".part")
    temporary.unlink(missing_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    audit = Counter()
    database = sqlite3.connect(temporary)
    try:
        database.execute("PRAGMA journal_mode=OFF")
        database.execute("CREATE TABLE score(chrom TEXT, strand TEXT, pos INTEGER, value REAL, PRIMARY KEY(chrom,strand,pos)) WITHOUT ROWID")
        batch = []
        with open_text(path) as stream:
            for line_number, line in enumerate(stream, 1):
                if not line.strip() or line.startswith(("#", "track", "browser")):
                    continue
                fields = line.split()
                if len(fields) != 6:
                    raise ValueError(f"Expected BED6 at line {line_number}")
                chrom, start, end, _, value, strand = fields
                start, end = int(start), int(end)
                if start < 0 or end <= start or strand not in ("+", "-"):
                    raise ValueError(f"Invalid BED coordinate/strand at line {line_number}")
                if value in ("NA", "NaN", "nan", ".", "NULL"):
                    audit["explicit_missing"] += 1
                    continue
                value = float(value)
                if not math.isfinite(value):
                    raise ValueError(f"Nonfinite BED score at line {line_number}")
                if value in missing_values:
                    audit["sentinel_missing_bases"] += end-start
                    continue
                audit["intervals"] += 1
                audit["measured"] += end-start
                audit["zero"] += (end-start)*(value == 0)
                audit["negative"] += (end-start)*(value < 0)
                for pos in range(start, end):
                    batch.append((chrom, strand, pos, value))
                    if len(batch) == 50000:
                        database.executemany("INSERT INTO score VALUES(?,?,?,?)", batch)
                        database.commit(); batch.clear()
                        print(f"  Indexed {audit['measured']:,} measured bases", flush=True)
        database.executemany("INSERT INTO score VALUES(?,?,?,?)", batch)
        database.commit()
        if not audit["measured"]:
            raise ValueError("No measured BED positions")
        database.close()
        temporary.replace(destination)
        report = dict(identity, counts=dict(audit))
        atomic_json(audit_path, report)
        return destination, report
    finally:
        database.close()
        temporary.unlink(missing_ok=True)


def attributes(text):
    return {k: unquote(v) for k, v in (f.split("=", 1) for f in text.split(";") if "=" in f)}


def representative_transcripts(path):
    """Choose the longest exon-annotated transcript per gene without using scores."""
    transcripts, genes, exons = {}, {}, defaultdict(list)
    audit = Counter()
    with open_text(path) as stream:
        for line in stream:
            if line.startswith("##FASTA"):
                break
            if not line.strip() or line.startswith("#"):
                continue
            fields = line.rstrip().split("\t")
            if len(fields) != 9:
                raise ValueError("Expected GFF3 with nine columns")
            chrom, _, feature, start, end, _, strand, _, raw = fields
            a = attributes(raw)
            start, end = int(start)-1, int(end)
            if start < 0 or end <= start:
                raise ValueError("Invalid GFF3 coordinate")
            if feature in ("gene", "ncRNA_gene", "pseudogene"):
                if "ID" in a:
                    genes[a["ID"]] = a.get("gene_id", a["ID"])
            elif feature == "exon":
                for parent in a.get("Parent", "").split(","):
                    if parent:
                        exons[parent].append((chrom, start, end, strand))
            elif feature not in ("CDS", "five_prime_UTR", "three_prime_UTR") and "ID" in a and "Parent" in a:
                if a["ID"] in transcripts:
                    raise ValueError(f"Duplicate transcript ID: {a['ID']}")
                transcripts[a["ID"]] = {"id": a["ID"], "parent": a["Parent"],
                    "chrom": chrom, "strand": strand, "start": start, "end": end}
    grouped = defaultdict(list)
    for tid, t in transcripts.items():
        if t["parent"] not in genes or not exons[tid]:
            audit["unresolved_parent_or_no_exons"] += 1
            continue
        blocks = sorted(exons[tid], key=lambda x: x[1])
        if (t["strand"] not in ("+", "-") or any(c != t["chrom"] or s != t["strand"]
                or lo < t["start"] or hi > t["end"] for c, lo, hi, s in blocks)
                or any(b[1] < a[2] for a, b in zip(blocks, blocks[1:]))):
            raise ValueError(f"Inconsistent/overlapping exons: {tid}")
        t.update(gene_id=genes[t["parent"]], exons=[(lo, hi) for _, lo, hi, _ in blocks],
                 length=sum(hi-lo for _, lo, hi, _ in blocks))
        grouped[t["gene_id"]].append(t)
    chosen = []
    for gid, candidates in sorted(grouped.items()):
        chosen.append(sorted(candidates, key=lambda t: (-t["length"], t["id"]))[0])
        audit["unchosen_isoforms"] += len(candidates)-1
    audit["representative_genes"] = len(chosen)
    if not chosen:
        raise ValueError("No gene-parented, exon-annotated transcripts in reference")
    return chosen, dict(audit)


def project_transcript(t, reference, database, circular=False):
    length = reference.get_reference_length(t["chrom"])
    blocks = []
    for lo, hi in t["exons"]:
        if lo >= length or hi-lo > length:
            raise ValueError(f"Reference interval out of bounds: {t['id']}")
        if hi > length:
            if not circular:
                raise ValueError(f"Reference interval out of bounds: {t['id']}")
            blocks.extend([(lo, length), (0, hi-length)])
        else:
            blocks.append((lo, hi))
    if t["strand"] == "-":
        blocks.reverse()
    sequence, measurements, offset = [], {}, 0
    for lo, hi in blocks:
        chunk = reference.fetch(t["chrom"], lo, hi).upper()
        if len(chunk) != hi-lo:
            raise ValueError(f"Truncated reference interval: {t['id']}")
        if t["strand"] == "-":
            chunk = chunk.translate(str.maketrans("ACGTRYMKBDHV", "TGCAYRKMVHDB"))[::-1]
        sequence.append(chunk)
        for pos, value in database.execute("SELECT pos,value FROM score WHERE chrom=? AND strand=? AND pos>=? AND pos<? ORDER BY pos",
                                            (t["chrom"], t["strand"], lo, hi)):
            p = offset+(pos-lo+1 if t["strand"] == "+" else hi-pos)
            measurements[p] = value
        offset += hi-lo
    return validate_record({"id": t["id"], "gene_id": t["gene_id"], "sequence": "".join(sequence),
                            "measurements": measurements, "projection": dict(t, projected_blocks=blocks)})


def reference_fasta(path, cache):
    import pysam
    destination = cache/(sha256(path)+".fa")
    cache.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        temporary = destination.with_suffix(".part")
        try:
            with gzip.open(path, "rb") as stream, temporary.open("wb") as out:
                shutil.copyfileobj(stream, out)
            temporary.replace(destination)
        finally:
            temporary.unlink(missing_ok=True)
    if not Path(str(destination)+".fai").exists():
        pysam.faidx(str(destination))
    return pysam.FastaFile(str(destination))


def genbank_transcripts(path, reference, accession):
    """Use deposited gene locations only after checking the complete DNA sequence."""
    from Bio import SeqIO
    from Bio.SeqFeature import ExactPosition
    record = SeqIO.read(str(path), "genbank")
    if record.id != accession or reference.fetch(accession).upper() != str(record.seq).upper():
        raise ValueError("GenBank accession/full genome sequence does not match probing reference")
    audit = Counter()
    chosen, seen = [], set()
    for feature in record.features:
        if feature.type != "gene":
            continue
        gid = feature.qualifiers.get("locus_tag", [None])[0]
        parts = feature.location.parts if feature.location is not None else []
        strand = feature.location.strand if parts else None
        if not gid or strand not in (1, -1) or any(p.strand != strand or not isinstance(p.start, ExactPosition)
                or not isinstance(p.end, ExactPosition) or p.ref is not None for p in parts):
            audit["unresolved_or_fuzzy_gene"] += 1
            continue
        if gid in seen:
            raise ValueError(f"Duplicate GenBank gene: {gid}")
        seen.add(gid)
        # Biopython parts are in biological extraction order, including origin joins.
        blocks = [(int(p.start), int(p.end)) for p in parts]
        if strand == -1:
            blocks.reverse()
        chosen.append({"id": "gene:"+gid, "gene_id": gid, "chrom": accession,
            "strand": "+" if strand == 1 else "-", "start": min(lo for lo, _ in blocks),
            "end": max(hi for _, hi in blocks), "exons": blocks,
            "length": len(feature.location), "source_feature_type": "gene"})
    if not chosen:
        raise ValueError("No exact annotated genes in GenBank reference")
    audit["representative_genes"] = len(chosen)
    audit["full_reference_sequence_verified"] = 1
    return sorted(chosen, key=lambda t: t["gene_id"]), dict(audit)


def prepare_rasp(d, work):
    cache = work/"downloads"
    metadata = track_metadata(d, cache)
    bed, bed_info = rasp_asset("bed", d["track"], cache)
    fa, fa_info = rasp_asset("fasta", d["species"]+".fa.gz", cache)
    if d.get("annotation_provider") == "genbank":
        annotation_path, annotation_info = download(d["annotation_url"], cache)
        with reference_fasta(fa, work/"references") as reference:
            transcripts, annotation_audit = genbank_transcripts(annotation_path, reference, d["genbank_accession"])
        mapping = "Version-matched GenBank gene intervals; complete genome DNA checked against RASP reference"
    else:
        annotation_path, annotation_info = rasp_asset("gff", d["species"]+".gff3.gz", cache)
        transcripts, annotation_audit = representative_transcripts(annotation_path)
        mapping = "RASP matched genome/GFF3, exon concatenation in transcript orientation; longest transcript per gene"
    db_path, bed_audit = bed_database(bed, work/"indexes", d.get("missing_values", ()))
    audit = {"annotation": annotation_audit, "bed": bed_audit, "mapping_counts": Counter(), "excluded": []}
    def records():
        with reference_fasta(fa, work/"references") as reference, sqlite3.connect(db_path) as database:
            for t in transcripts:
                try:
                    record = project_transcript(t, reference, database, d.get("reference_topology") == "circular")
                except (ValueError, KeyError) as exc:
                    audit["mapping_counts"]["excluded"] += 1
                    audit["excluded"].append({"id": t["id"], "gene_id": t["gene_id"], "reason": str(exc)})
                    continue
                audit["mapping_counts"]["retained"] += 1
                yield record
    provenance = dict(metadata, bed=bed_info, fasta=fa_info, annotation=annotation_info,
        mapping=mapping,
        scope="Genomic tracks cannot resolve isoforms. Bacterial annotation units do not reconstruct all author-defined polycistronic RNAs.")
    return records(), provenance, audit


def prepare_pars(source):
    from validation.controls_2010.compare_all_genes import (
        SOURCE_FILES, read_fasta, read_annotation, read_transcript_blocks,
        read_wig, validate_mapping, map_measurements,
    )
    paths = {k: source/v for k, v in SOURCE_FILES.items()}
    provenance = {k: {"filename": p.name, "sha256": sha256(p)} for k, p in paths.items()}
    sequences, genome = read_fasta(paths["transcripts"]), read_fasta(paths["genome"])
    annotation, blocks, wig = read_annotation(paths["annotation"]), read_transcript_blocks(paths["annotation"]), read_wig(paths["pars"])
    intervals = defaultdict(list)
    for chrom, start, end in annotation.values():
        intervals[(chrom, start > end)].append((min(start, end), max(start, end)))
    audit = {"counts": Counter(), "excluded": []}
    def records():
        for name, sequence in sorted(sequences.items()):
            if name not in annotation:
                audit["counts"]["missing_annotation"] += 1
                audit["excluded"].append({"id": name, "reason": "missing_annotation"})
                continue
            try:
                location = annotation[name]
                coordinates = validate_mapping(sequence, location, genome, blocks.get(name, ()))
            except ValueError as exc:
                audit["counts"]["mapping_failure"] += 1
                audit["excluded"].append({"id": name, "reason": str(exc)})
                continue
            chrom, start, end = location
            measurements, ambiguous = map_measurements(location, wig, intervals[(chrom, start <= end)], True, coordinates)
            audit["counts"]["retained"] += 1
            audit["counts"]["excluded_antisense_measured_bases"] += ambiguous
            yield validate_record({"id": name, "gene_id": name, "sequence": sequence,
                                   "measurements": measurements, "mapping_mode": "exact_deposited_sequence"})
    return records(), dict(files=provenance, mapping="Exact deposited RNA reconstruction; ambiguous antisense measurements excluded"), audit


def write_dataset(d, records, provenance, audit, prepared):
    validate_dataset(d)
    prepared.mkdir(parents=True, exist_ok=True)
    destination = prepared/(d["id"]+".jsonl.gz")
    temporary = destination.with_suffix(".part")
    seen, n_measured = set(), 0
    try:
        with gzip.open(temporary, "wt") as stream:
            for record in records:
                record = validate_record(record)
                if record["id"] in seen:
                    raise ValueError("Duplicate experimental record ID")
                seen.add(record["id"]); n_measured += len(record["measurements"])
                stream.write(json.dumps(record, allow_nan=False, separators=(",", ":"))+"\n")
        if not seen:
            raise ValueError("No canonical records produced")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)
    atomic_json(prepared/(d["id"]+".audit.json"), audit)
    return dict(d, records=destination.name, records_sha256=sha256(destination),
                n_records=len(seen), n_measured=n_measured, provenance=provenance)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--catalog", type=Path, default=Path(__file__).with_name("catalog.json"))
    p.add_argument("--work-dir", type=Path, default=Path(__file__).parent/"work")
    p.add_argument("--pars-source-dir", type=Path, default=REPO/"validation/controls_2010/source")
    p.add_argument("--dataset", action="append", help="Repeat to select datasets; default: all seven")
    p.add_argument("--list", action="store_true")
    p.add_argument("--import-jsonl", type=Path, help="Import canonical JSONL instead of downloading")
    p.add_argument("--metadata", type=Path, help="Metadata JSON for --import-jsonl (one dataset)")
    args = p.parse_args(argv)
    prepared = args.work_dir/"prepared"
    index_path = prepared/"index.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else {"schema_version": 1, "datasets": []}
    by_id = {d["id"]: d for d in index["datasets"]}
    if args.import_jsonl:
        if not args.metadata or args.dataset:
            p.error("--import-jsonl requires --metadata; cannot combine with --dataset")
        from validation.multi_dataset.common import read_records
        datasets = [json.loads(args.metadata.read_text())]
    else:
        catalog = json.loads(args.catalog.read_text())
        datasets = [d for d in catalog["datasets"] if not args.dataset or d["id"] in args.dataset]
        if not datasets or args.dataset and set(args.dataset)-{d["id"] for d in datasets}:
            p.error("Unknown dataset selection")
    for d in datasets:
        validate_dataset(d)
        if args.list:
            print(f"{d['id']}: {d['study']}, {d['assay']}, {d['conditions']}")
            continue
        if d["id"] in by_id:
            old = by_id[d["id"]]
            if all(old.get(k) == v for k, v in d.items()) and sha256(prepared/old["records"]) == old["records_sha256"]:
                if not args.import_jsonl or old["provenance"].get("input_sha256") == sha256(args.import_jsonl):
                    print(f"Already prepared: {d['id']}", flush=True)
                    continue
            p.error(f"Prepared dataset {d['id']} changed; choose a new --work-dir")
        print(f"Preparing {d['id']} (no folds)", flush=True)
        if args.import_jsonl:
            records, provenance, audit = read_records(args.import_jsonl), {"input_sha256": sha256(args.import_jsonl), "metadata_sha256": sha256(args.metadata)}, {}
        elif d["provider"] == "geo_pars":
            records, provenance, audit = prepare_pars(args.pars_source_dir)
        elif d["provider"] == "rasp":
            records, provenance, audit = prepare_rasp(d, args.work_dir)
        else:
            p.error("Unknown dataset provider")
        by_id[d["id"]] = write_dataset(d, records, provenance, audit, prepared)
        atomic_json(index_path, {"schema_version": 1, "datasets": [by_id[k] for k in sorted(by_id)]})
        print(f"Prepared {d['id']}: {by_id[d['id']]['n_records']:,} records", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
