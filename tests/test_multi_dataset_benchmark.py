"""Probing projection, fair coverage, ranking, and checkpoint integrity checks."""
import gzip
import hashlib
import json
import sqlite3

import pytest

from validation.multi_dataset import benchmark as b
from validation.multi_dataset.common import measured_window, ranking_stats, validate_record
from validation.multi_dataset.prepare import (
    bed_database, genbank_transcripts, project_transcript, representative_transcripts, write_dataset,
)


def gz(path, value):
    with gzip.open(path, "wt") as stream:
        stream.write(value)
    return path


def test_canonical_integrity_and_assay_observable_coverage():
    r = validate_record({"id": "one", "gene_id": "gene", "sequence": "actgac",
                         "measurements": {"1": 0, "2": -.2, "5": 1}})
    assert r["sequence"] == "ACUGAC"
    assert r["measurements"][1] == 0
    assert r["sequence_sha256"] == hashlib.sha256(b"ACUGAC").hexdigest()
    assert measured_window(r, 1, 6, "AC", .75, 3) == [1, 2, 5]
    assert measured_window(r, 1, 6, "AC", .8, 3) is None
    for measurements in ({0: 2}, {"01": 0}, {1: float("nan")}):
        with pytest.raises(ValueError): validate_record(dict(r, measurements=measurements))
    with pytest.raises(ValueError, match="hash mismatch"):
        validate_record(dict(r, sequence="AAAAAA"))


def test_bed_expands_constant_intervals_and_preserves_strand_zero_and_negative(tmp_path):
    path = gz(tmp_path/"score.gz", "chr\t0\t2\tNA\t0\t+\nchr\t1\t2\tNA\t-.2\t-\nchr\t2\t3\tNA\tNULL\t+\n")
    indexed, audit = bed_database(path, tmp_path/"indexes")
    with sqlite3.connect(indexed) as db:
        assert list(db.execute("SELECT strand,pos,value FROM score ORDER BY strand,pos")) == [("+", 0, 0), ("+", 1, 0), ("-", 1, -.2)]
    assert audit["counts"]["measured"] == 3
    assert audit["counts"]["negative"] == 1
    assert bed_database(path, tmp_path/"indexes")[0] == indexed
    duplicated = gz(tmp_path/"duplicate.gz", "chr\t0\t2\tNA\t0\t+\nchr\t1\t2\tNA\t1\t+\n")
    with pytest.raises(sqlite3.IntegrityError): bed_database(duplicated, tmp_path/"indexes")


class Reference:
    def fetch(self, chrom, lo, hi):
        assert chrom == "chr"
        return "ACGTAAGCCGTA"[lo:hi]

    def get_reference_length(self, chrom):
        assert chrom == "chr"
        return 12


def test_exon_orientation_and_longest_representative_are_independent_of_measurements(tmp_path):
    gff = "chr\tx\tncRNA_gene\t1\t12\t.\t-\t.\tID=g;gene_id=gene\n"
    gff += "chr\tx\tmRNA\t1\t12\t.\t-\t.\tID=long;Parent=g\n"
    gff += "chr\tx\tmRNA\t1\t12\t.\t-\t.\tID=short;Parent=g\n"
    gff += "chr\tx\texon\t1\t2\t.\t-\t.\tParent=long\n"
    gff += "chr\tx\texon\t9\t10\t.\t-\t.\tParent=long\n"
    gff += "chr\tx\texon\t3\t3\t.\t-\t.\tParent=short\n"
    transcripts, audit = representative_transcripts(gz(tmp_path/"gff.gz", gff))
    assert len(transcripts) == 1 and transcripts[0]["id"] == "long"
    assert audit["unchosen_isoforms"] == 1
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE TABLE score(chrom,strand,pos,value)")
        db.executemany("INSERT INTO score VALUES('chr',?,?,?)", [("-", 0, 0), ("-", 9, 9), ("+", 9, 99), ("-", 5, 55)])
        r = project_transcript(transcripts[0], Reference(), db)
        assert r["sequence"] == "CGGU"
        assert r["measurements"] == {1: 9, 4: 0}
        t = dict(transcripts[0], strand="+", exons=[(10, 14)])
        with pytest.raises(ValueError, match="out of bounds"): project_transcript(t, Reference(), db)
        circular = project_transcript(t, Reference(), db, circular=True)
        assert circular["sequence"] == "UAAC"


def test_fractional_top_ties_do_not_depend_on_record_order():
    rows = [{"experimental_availability": v, "score": 1} for v in [0, 1, 9, 10]]
    assert ranking_stats(rows, "score", .25, 3)["top_fraction_gain"] == 0
    assert ranking_stats(list(reversed(rows)), "score", .25, 3)["top_fraction_gain"] == 0
    rows[3]["score"] = 2
    assert ranking_stats(rows, "score", .25, 3)["top_fraction_gain"] == 5


def test_genbank_reference_mismatch_is_rejected_before_mapping(tmp_path):
    pytest.importorskip("Bio")
    from Bio import SeqIO
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
    from Bio.SeqFeature import SeqFeature, SimpleLocation
    record = SeqRecord(Seq("ACGTAAGCCGTA"), id="chr", name="chr",
                       annotations={"molecule_type": "DNA"})
    record.features = [SeqFeature(SimpleLocation(0, 2, strand=-1), type="gene", qualifiers={"locus_tag": ["g"]})]
    path = tmp_path/"reference.gb"
    SeqIO.write(record, path, "genbank")
    class FullReference(Reference):
        def fetch(self, chrom, lo=0, hi=12): return super().fetch(chrom, lo, hi)
    transcripts, audit = genbank_transcripts(path, FullReference(), "chr")
    assert transcripts[0]["gene_id"] == "g" and transcripts[0]["strand"] == "-"
    assert audit["full_reference_sequence_verified"] == 1
    class WrongReference:
        def fetch(self, chrom): return "AAAAAAAAAAAA"
    with pytest.raises(ValueError, match="does not match"):
        genbank_transcripts(path, WrongReference(), "chr")


def test_pars_direction_and_seed_are_compared_to_correct_measurements():
    from rnavail.core.result import M
    b.CONFIG = {"min_pairs": 3, "coverage": 1., "min_window_bases": 2, "top_fraction": .34,
                "prediction": {"seed_length": 2}}
    r = validate_record({"id": "test", "gene_id": "test", "sequence": "AAAAAA",
        "measurements": {p: 4-p for p in range(1, 7)}})
    candidates = [{"start": p, "end": p+3, "pipeline_score": p/10, "score_coverage": .7,
        "pipeline_without_seed": p/10, "pipeline_without_opening_cost": p/10,
        "metrics": {M.P_UNPAIRED: p/10, M.SEED_P_UNPAIRED: p/10,
                    M.SEED_START: p, M.DG_OPEN_PER_NT: 1-p/10}} for p in range(1, 4)]
    prediction = {"candidates": candidates, "per_base": {"test": [p/10 for p in range(1, 7)]}}
    stats, rows = b.compare(r, {"higher_is": "paired", "observable_bases": "ACGU"}, prediction)
    assert stats["per_base:test"]["pearson"] == pytest.approx(1)
    assert stats["window:pipeline_score"]["spearman"] == pytest.approx(1)
    assert stats["seed:own_measurements"]["pearson"] == pytest.approx(1)
    assert rows[0]["experimental_availability"] == -1.5


def prediction_config():
    return {"temperature": 37., "window_size": 200, "max_bp_span": 150, "footprint": 20,
        "seed_length": 8, "step": 1, "tools": ["rnaplfold", "rnafold"],
        "robustness": False, "length_robustness": False, "global_max_length": 6000}


def test_tiny_native_prediction_equals_public_pipeline_and_reuses_cache(tmp_path, monkeypatch):
    from rnavail.adapters.registry import get
    if not get("rnaplfold").availability().available:
        pytest.skip("ViennaRNA unavailable")
    from rnavail.core.sequence import Sequence, Region
    from rnavail.core.model import ModelSettings, RecognitionSpec
    from rnavail.pipeline import run
    sequence = "GGGGGGAAAAAACCCCCCAAAAAAGGGGGGAAAAAACCCCCC"
    b.initialize({"prediction": prediction_config(), "retry_failed": False}, tmp_path)
    saved = b.predict(sequence)
    assert not saved["has_failures"]
    n = len(sequence)
    direct = run.evaluate(Sequence("check", sequence), [Region(1, 20)],
        settings=ModelSettings(window_size=n, max_bp_span=n, max_unpaired=20),
        seed_length=8, tools=["rnaplfold", "rnafold"], max_cost=None,
        recognition=RecognitionSpec(seed_lengths=(8,)))
    assert saved["candidates"][0]["pipeline_score"] == pytest.approx(direct.candidates[0].score.value)
    monkeypatch.setattr(run, "evaluate", lambda *args, **kwargs: pytest.fail("Refolded a cached sequence"))
    assert b.predict(sequence) == saved


def test_resume_checks_inputs_and_settings_without_refolding(tmp_path, monkeypatch):
    from rnavail.adapters.registry import get
    if not get("rnaplfold").availability().available: pytest.skip("ViennaRNA unavailable")
    dataset = {"id": "test", "study": "control", "assay": "synthetic", "conditions": {},
               "higher_is": "available", "observable_bases": "ACGU"}
    record = {"id": "one", "gene_id": "one", "sequence": "AAAAAA", "measurements": {p: p for p in range(1, 7)}}
    prepared = tmp_path/"prepared"
    info = write_dataset(dataset, [record], {}, {}, prepared)
    (prepared/"index.json").write_text(json.dumps({"schema_version": 1, "datasets": [info]}))
    args = ["--prepared-dir", str(prepared), "--output-dir", str(tmp_path/"results"),
            "--tools", "rnaplfold", "--min-pairs", "3", "--footprint", "4", "--seed-length", "2"]
    assert b.main(args) == 0
    monkeypatch.setattr(b, "predict", lambda *args: pytest.fail("Resumed a complete record by refolding"))
    assert b.main(args+["--resume", "--workers", "2"]) == 0
    with pytest.raises(SystemExit) as exc:
        b.main(args+["--resume", "--step", "2"])
    assert exc.value.code == 2
    with gzip.open(prepared/info["records"], "at") as stream: stream.write("\n")
    with pytest.raises(SystemExit) as exc: b.main(args+["--resume"])
    assert exc.value.code == 2
