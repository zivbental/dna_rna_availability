"""JSON reader for condition-linked :mod:`rnavail.core.evidence` tracks.

The reader accepts either one track object or a versioned envelope containing
``{"tracks": [...]}``.  It does not interpret an evidence value or convert it
to an opening-energy penalty; it only verifies target identity and preserves
the supplied measurement context.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import replace
from pathlib import Path
from typing import Any

from ..core.evidence import (
    EVIDENCE_SCHEMA_VERSION,
    EvidenceError,
    EvidenceRecord,
    EvidenceTrack,
)
from ..core.sequence import Region, Sequence


def _reject_nonstandard_number(token: str) -> None:
    raise EvidenceError(f"JSON must not contain non-finite number {token!r}")


def _object(value: Any, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise EvidenceError(f"{context} must be a JSON object")
    return value


def _required(value: Mapping[str, Any], key: str, *, context: str) -> Any:
    if key not in value:
        raise EvidenceError(f"{context} is missing required field {key!r}")
    return value[key]


def _schema_version(
    payload: Mapping[str, Any], *, context: str, inherited: str | None = None,
) -> str:
    versions = [
        payload[key]
        for key in ("evidence_schema_version", "schema_version")
        if key in payload
    ]
    if len(versions) == 2 and versions[0] != versions[1]:
        raise EvidenceError(f"{context} gives conflicting schema versions")
    if versions:
        version = versions[0]
    elif inherited is not None:
        version = inherited
    else:
        raise EvidenceError(
            f"{context} is missing evidence_schema_version (currently "
            f"{EVIDENCE_SCHEMA_VERSION})"
        )
    if isinstance(version, int) and not isinstance(version, bool):
        version = f"{version}.0"
    if not isinstance(version, str):
        raise EvidenceError(f"{context} schema version must be a string")
    return version


def _region(payload: Mapping[str, Any], *, context: str) -> Region:
    interval = payload.get("interval")
    if interval is None:
        interval = {
            key: payload[key]
            for key in ("start", "end", "name", "parent")
            if key in payload
        }
    interval = _object(interval, context=f"{context} interval")
    start = _required(interval, "start", context=f"{context} interval")
    end = _required(interval, "end", context=f"{context} interval")
    if isinstance(start, bool) or not isinstance(start, int):
        raise EvidenceError(f"{context} interval start must be an integer")
    if isinstance(end, bool) or not isinstance(end, int):
        raise EvidenceError(f"{context} interval end must be an integer")
    name = interval.get("name", "")
    parent = interval.get("parent", "")
    if not isinstance(name, str) or not isinstance(parent, str):
        raise EvidenceError(f"{context} interval name and parent must be strings")
    try:
        return Region(start=start, end=end, name=name, parent=parent)
    except ValueError as exc:
        raise EvidenceError(f"{context} has invalid interval: {exc}") from None


def _metadata(
    payload: Mapping[str, Any], *, known: set[str], context: str,
) -> Mapping[str, Any]:
    explicit = payload.get("metadata", {})
    if not isinstance(explicit, Mapping):
        raise EvidenceError(f"{context} metadata must be a JSON object")
    merged = dict(explicit)
    for key, value in payload.items():
        if key in known:
            continue
        if key in merged:
            raise EvidenceError(
                f"{context} duplicates {key!r} in metadata and at top level"
            )
        # Type-specific information (for example an interacting arm, strand,
        # replicate, or allele frequency) remains available without forcing a
        # shared biological interpretation on every evidence type.
        merged[key] = value
    return merged


def _record(payload: Any, *, context: str) -> EvidenceRecord:
    data = _object(payload, context=context)
    known = {
        "interval", "start", "end", "name", "parent", "value", "unit",
        "uncertainty", "missing_reason", "interpretation", "provenance",
        "metadata",
    }
    provenance = data.get("provenance", {})
    if not isinstance(provenance, Mapping):
        raise EvidenceError(f"{context} provenance must be a JSON object")
    return EvidenceRecord(
        interval=_region(data, context=context),
        value=data.get("value"),
        unit=data.get("unit"),
        uncertainty=data.get("uncertainty", {}),
        missing_reason=data.get("missing_reason"),
        interpretation=data.get("interpretation", ""),
        provenance=provenance,
        metadata=_metadata(data, known=known, context=context),
    )


def _track(
    payload: Any, *, context: str, inherited_version: str | None = None,
) -> EvidenceTrack:
    data = _object(payload, context=context)
    records = _required(data, "records", context=context)
    if not isinstance(records, list):
        raise EvidenceError(f"{context} records must be a JSON array")
    known = {
        "evidence_schema_version", "schema_version", "track_id", "evidence_type",
        "source", "condition_id", "transcript_id", "sequence_hash", "records",
        "coordinate_system", "interpretation", "missingness", "provenance",
        "metadata",
    }
    provenance = data.get("provenance", {})
    missingness = data.get("missingness", {})
    if not isinstance(provenance, Mapping):
        raise EvidenceError(f"{context} provenance must be a JSON object")
    if not isinstance(missingness, Mapping):
        raise EvidenceError(f"{context} missingness must be a JSON object")
    return EvidenceTrack(
        schema_version=_schema_version(
            data, context=context, inherited=inherited_version
        ),
        track_id=data.get("track_id", ""),
        evidence_type=_required(data, "evidence_type", context=context),
        source=_required(data, "source", context=context),
        condition_id=_required(data, "condition_id", context=context),
        transcript_id=_required(data, "transcript_id", context=context),
        sequence_hash=_required(data, "sequence_hash", context=context),
        coordinate_system=data.get("coordinate_system", "one_based_inclusive"),
        interpretation=data.get("interpretation", ""),
        missingness=missingness,
        provenance=provenance,
        metadata=_metadata(data, known=known, context=context),
        records=tuple(
            _record(record, context=f"{context} record {index}")
            for index, record in enumerate(records, start=1)
        ),
    )


def _with_input_provenance(track: EvidenceTrack, source_hash: str) -> EvidenceTrack:
    """Bind imported tracks to the exact JSON bytes that produced them."""
    provenance = dict(track.provenance)
    # This field belongs to the import layer rather than the user document, so
    # it cannot be accidentally supplied with a stale or forged value.
    provenance["rnavail_input_sha256"] = source_hash
    return replace(track, provenance=provenance)


def read_evidence_tracks(path: str | Path, sequence: Sequence) -> tuple[EvidenceTrack, ...]:
    """Read and verify one or more versioned JSON evidence tracks.

    Parameters
    ----------
    path:
        JSON document containing either one track or an envelope of the form
        ``{"evidence_schema_version": "1.0", "tracks": [...]}``.
    sequence:
        The exact normalized target sequence selected for this analysis.  Each
        track's SHA-256 checksum and all record coordinates are checked before
        it is returned.

    Returns
    -------
    tuple[EvidenceTrack, ...]
        Immutable tracks in source order.  No evidence is converted into a
        structural score by this reader.
    """
    source = Path(path)
    try:
        source_bytes = source.read_bytes()
        source_text = source_bytes.decode("utf-8")
        payload = json.loads(
            source_text, parse_constant=_reject_nonstandard_number
        )
    except UnicodeDecodeError as exc:
        raise EvidenceError(f"{source}: evidence JSON must be UTF-8") from exc
    except json.JSONDecodeError as exc:
        raise EvidenceError(f"{source}: invalid JSON: {exc.msg}") from None
    except OSError:
        raise

    source_hash = hashlib.sha256(source_bytes).hexdigest()
    root = _object(payload, context=str(source))
    if "tracks" not in root:
        return (_with_input_provenance(
            _track(root, context="evidence track").validate_against(sequence),
            source_hash,
        ),)

    tracks = root["tracks"]
    if not isinstance(tracks, list):
        raise EvidenceError(f"{source} tracks must be a JSON array")
    if not tracks:
        raise EvidenceError(f"{source} tracks must contain at least one track")
    # A manifest may declare its shared version once, or each track may carry
    # its own version.  In the latter form `_track` requires every child to
    # state one; no unversioned track is silently accepted.
    inherited = (
        _schema_version(root, context="evidence manifest")
        if "evidence_schema_version" in root or "schema_version" in root
        else None
    )
    return tuple(
        _with_input_provenance(
            _track(
                track, context=f"evidence track {index}", inherited_version=inherited
            ).validate_against(sequence),
            source_hash,
        )
        for index, track in enumerate(tracks, start=1)
    )
