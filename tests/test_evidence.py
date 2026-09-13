"""Tests for the standalone condition-linked evidence import contract."""

from __future__ import annotations

import json

import pytest

from rnavail.core.evidence import EvidenceError, EvidenceRecord, EvidenceTrack
from rnavail.core.model import ConditionSpec, ModelSettings
from rnavail.core.sequence import Region, Sequence
from rnavail.io.evidence import read_evidence_tracks
from rnavail.io.html_report import to_html
from rnavail.io.report import to_text
from rnavail.pipeline.run import evaluate


@pytest.fixture
def sequence() -> Sequence:
    return Sequence("NM_example.3", "AUGCAUGCAU")


def _track_payload(sequence: Sequence) -> dict[str, object]:
    return {
        "evidence_schema_version": "1.0",
        "track_id": "clip-1",
        "evidence_type": "protein_interaction",
        "source": "doi:10.example/clip",
        "condition_id": "HEK293_37C",
        "transcript_id": "NM_example.3",
        "sequence_hash": sequence.sha256,
        "coordinate_system": "one_based_inclusive",
        "interpretation": "Enrichment is not a direct occupancy measurement.",
        "missingness": {"unmeasured_positions": [9, 10]},
        "provenance": {"assay": "eCLIP", "replicates": ["r1", "r2"]},
        "records": [
            {
                "interval": {"start": 3, "end": 7},
                "value": 0.0,
                "unit": "normalized_enrichment",
                "uncertainty": {"sem": 0.25},
                "missing_reason": None,
                "interpretation": "A peak denotes assay enrichment, not proven vacancy.",
                "provenance": {"replicate_ids": ["r1", "r2"]},
                "strand": "+",
            },
            {
                "start": 8,
                "end": 8,
                "value": None,
                "missing_reason": "low coverage",
                "interpretation": "No signal was measured at this position.",
            },
        ],
    }


def test_reader_preserves_context_zero_and_missingness(tmp_path, sequence):
    payload = _track_payload(sequence)
    path = tmp_path / "clip.json"
    path.write_text(json.dumps(payload))

    (track,) = read_evidence_tracks(path, sequence)

    assert track.evidence_type == "protein_interaction"
    assert track.condition_id == "HEK293_37C"
    assert track.transcript_id == "NM_example.3"
    assert track.provenance["assay"] == "eCLIP"
    assert len(track.provenance["rnavail_input_sha256"]) == 64
    assert track.missingness["unmeasured_positions"] == (9, 10)
    assert track.records[0].value == 0.0
    assert track.records[1].value is None
    assert track.records[1].missing_reason == "low coverage"
    assert track.records[0].metadata["strand"] == "+"
    assert track.to_dict()["records"][0]["metadata"]["strand"] == "+"


def test_reader_accepts_versioned_manifest_and_inherits_version(tmp_path, sequence):
    first = _track_payload(sequence)
    first.pop("evidence_schema_version")
    second = _track_payload(sequence)
    second.pop("evidence_schema_version")
    second["track_id"] = "mod-1"
    second["evidence_type"] = "modification"
    path = tmp_path / "evidence.json"
    path.write_text(json.dumps({
        "evidence_schema_version": "1.0", "tracks": [first, second],
    }))

    tracks = read_evidence_tracks(path, sequence)

    assert [track.track_id for track in tracks] == ["clip-1", "mod-1"]
    assert all(track.schema_version == "1.0" for track in tracks)
    assert isinstance(tracks, tuple)


def test_reader_accepts_individually_versioned_tracks_without_manifest_version(
    tmp_path, sequence,
):
    first = _track_payload(sequence)
    second = _track_payload(sequence)
    second["track_id"] = "custom-1"
    second["evidence_type"] = "custom"
    path = tmp_path / "individual-versions.json"
    path.write_text(json.dumps({"tracks": [first, second]}))

    assert len(read_evidence_tracks(path, sequence)) == 2


@pytest.mark.parametrize(
    ("field", "value", "match"),
    [
        ("sequence_hash", "0" * 64, "sequence_hash does not match"),
        ("coordinate_system", "zero_based_half_open", "one_based_inclusive"),
    ],
)
def test_reader_rejects_identity_and_coordinate_convention_mismatches(
    tmp_path, sequence, field, value, match,
):
    payload = _track_payload(sequence)
    payload[field] = value
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(payload))

    with pytest.raises(EvidenceError, match=match):
        read_evidence_tracks(path, sequence)


def test_reader_rejects_coordinate_outside_selected_sequence(tmp_path, sequence):
    payload = _track_payload(sequence)
    payload["records"][0]["interval"]["end"] = 11
    path = tmp_path / "out-of-range.json"
    path.write_text(json.dumps(payload))

    with pytest.raises(EvidenceError, match="invalid target coordinates"):
        read_evidence_tracks(path, sequence)


@pytest.mark.parametrize("uncertainty", [{"sem": float("nan")}, {"sem": True}])
def test_reader_rejects_nonfinite_or_nonnumeric_uncertainty(
    tmp_path, sequence, uncertainty,
):
    payload = _track_payload(sequence)
    payload["records"][0]["uncertainty"] = uncertainty
    path = tmp_path / "uncertainty.json"
    path.write_text(json.dumps(payload, allow_nan=True))

    with pytest.raises(EvidenceError, match="uncertainty.*finite number|non-finite"):
        read_evidence_tracks(path, sequence)


def test_track_and_records_are_deeply_immutable(sequence):
    record = EvidenceRecord(
        interval=Region(1, 2), interpretation="Measured signal.",
        uncertainty={"sd": 0.1}, provenance={"run": [1]},
    )
    track = EvidenceTrack(
        evidence_type="custom", source="lab notebook", condition_id="buffer-A",
        transcript_id="NM_example.3", sequence_hash=sequence.sha256,
        records=(record,), provenance={"nested": {"version": 1}},
    ).validate_against(sequence)

    with pytest.raises(TypeError):
        record.provenance["new"] = "value"
    with pytest.raises(TypeError):
        track.provenance["new"] = "value"
    with pytest.raises((AttributeError, TypeError)):
        track.records += (record,)


def test_pipeline_preserves_overlapping_evidence_without_scoring_it(sequence):
    track = EvidenceTrack(
        evidence_type="protein_interaction", source="eCLIP study",
        condition_id="buffer-A", transcript_id=sequence.name,
        sequence_hash=sequence.sha256,
        records=(EvidenceRecord(
            interval=Region(3, 7), value=4.2, unit="enrichment",
            interpretation="Enrichment does not establish occupancy.",
        ),),
    )
    region = Region(4, 6)
    baseline = evaluate(
        sequence, [region], settings=ModelSettings(), tools=[],
        condition=ConditionSpec(condition_id="buffer-A"),
    )
    report = evaluate(
        sequence, [region], settings=ModelSettings(), tools=[],
        condition=ConditionSpec(condition_id="buffer-A"),
        evidence_tracks=[track],
    )

    candidate = report.candidates[0]
    assert candidate.score.value == baseline.candidates[0].score.value
    assert report.detail["evidence_tracks"] == {
        "count": 1, "condition_statuses": ["matched"], "scoring": "annotation_only",
    }
    assert candidate.biological_evidence[0]["condition_status"] == "matched"
    assert candidate.biological_evidence[0]["record"]["value"] == 4.2
    payload = report.to_dict()
    assert payload["evidence_tracks"][0]["evidence_type"] == "protein_interaction"
    assert payload["candidates"][0]["biological_evidence"] == candidate.biological_evidence
    assert any("not score penalties" in note for note in candidate.notes)
    assert "evidence tracks: 1; annotation only" in to_text(report)
    assert "condition-linked evidence (1 record(s), annotation only)" in to_html(
        report, {}, top=1,
    )


def test_pipeline_marks_different_condition_evidence_as_unmatched(sequence):
    track = EvidenceTrack(
        evidence_type="ribosome", source="Ribo-seq", condition_id="condition-B",
        transcript_id=sequence.name, sequence_hash=sequence.sha256,
        records=(EvidenceRecord(interval=Region(1, 2)),),
    )
    report = evaluate(
        sequence, [Region(1, 2)], tools=[],
        condition=ConditionSpec(condition_id="condition-A"),
        evidence_tracks=[track],
    )

    assert report.candidates[0].biological_evidence[0]["condition_status"] == \
        "different_condition"
    assert any("different condition" in warning for warning in report.warnings)


def test_cli_imports_evidence_manifest_and_writes_annotations(tmp_path, sequence):
    from rnavail.cli import main

    evidence = tmp_path / "evidence.json"
    report = tmp_path / "report.json"
    evidence.write_text(json.dumps(_track_payload(sequence)))
    assert main([
        "evaluate", sequence.seq, "--region", "3-7", "--tools", "gquad-scan",
        "--condition-id", "HEK293_37C", "--evidence", str(evidence),
        "--json", str(report), "-q",
    ]) == 0

    payload = json.loads(report.read_text())
    assert payload["evidence_tracks"][0]["track_id"] == "clip-1"
    assert payload["candidates"][0]["biological_evidence"][0][
        "evidence_type"
    ] == "protein_interaction"
