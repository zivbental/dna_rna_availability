"""Condition-linked experimental evidence annotations.

This module deliberately models *observations*, rather than translating them
into structural or binding penalties.  A CLIP peak, a ribosome footprint, or
a motif is evidence with a stated coordinate system and interpretation; it is
not by itself proof that an RNA interval is occupied or unavailable.

All coordinates use :class:`~rnavail.core.sequence.Region`'s one-based,
inclusive convention.  The JSON reader in :mod:`rnavail.io.evidence` calls
``validate_against`` before returning a track, so an imported observation is
always tied to the normalized target sequence that was selected for a run.
"""

from __future__ import annotations

import math
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Literal, TypeAlias

from .sequence import Region, Sequence, SequenceError


EVIDENCE_SCHEMA_VERSION = "1.0"
"""The canonical schema version emitted by :meth:`EvidenceTrack.to_dict`."""

EvidenceType: TypeAlias = Literal[
    "probing",
    "duplex_contact",
    "protein_interaction",
    "ribosome",
    "modification",
    "variant",
    "direct_hybridization",
    "custom",
]

EVIDENCE_TYPES = frozenset({
    "probing",
    "duplex_contact",
    "protein_interaction",
    "ribosome",
    "modification",
    "variant",
    "direct_hybridization",
    "custom",
})

_SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")


class EvidenceError(ValueError):
    """Raised when an evidence track cannot be represented or verified."""


def _freeze_json(value: Any, *, path: str) -> Any:
    """Return an immutable, JSON-compatible representation of ``value``.

    ``json.loads`` accepts ``NaN`` and ``Infinity`` by default even though
    they are not valid interoperable JSON.  Rejecting non-finite numbers in
    provenance as well as the measured value avoids a track that cannot be
    faithfully written back out later.
    """
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise EvidenceError(f"{path} must not contain a non-finite number")
        return value
    if isinstance(value, Mapping):
        frozen: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise EvidenceError(f"{path} has a non-string key")
            frozen[key] = _freeze_json(item, path=f"{path}.{key}")
        return MappingProxyType(frozen)
    if isinstance(value, (list, tuple)):
        return tuple(
            _freeze_json(item, path=f"{path}[{index}]")
            for index, item in enumerate(value)
        )
    raise EvidenceError(
        f"{path} must contain JSON-compatible values, not {type(value).__name__}"
    )


def _thaw_json(value: Any) -> Any:
    """Convert frozen metadata back to standard JSON serializable objects."""
    if isinstance(value, Mapping):
        return {key: _thaw_json(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw_json(item) for item in value]
    return value


def _freeze_mapping(value: Mapping[str, Any], *, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise EvidenceError(f"{path} must be a JSON object")
    frozen = _freeze_json(value, path=path)
    assert isinstance(frozen, Mapping)
    return frozen


def _normalise_schema_version(value: str) -> str:
    if not isinstance(value, str):
        raise EvidenceError("evidence schema_version must be a string")
    version = value.strip()
    if version == "1":
        version = EVIDENCE_SCHEMA_VERSION
    if version != EVIDENCE_SCHEMA_VERSION:
        raise EvidenceError(
            f"unsupported evidence schema version {value!r}; supported version is "
            f"{EVIDENCE_SCHEMA_VERSION}"
        )
    return version


def _normalise_text(value: str, *, field_name: str) -> str:
    if not isinstance(value, str):
        raise EvidenceError(f"{field_name} must be a string")
    return value


@dataclass(frozen=True)
class EvidenceRecord:
    """One interval-level observation in an :class:`EvidenceTrack`.

    ``value`` is intentionally generic: an experimental signal can be a
    finite scalar, a categorical label, a boolean call, or absent.  An absent
    measurement remains distinguishable from a measured numeric zero through
    ``value`` and ``missing_reason``.  ``metadata`` preserves event-specific
    fields such as a second contact arm, strand, replicate identifier, or
    allele without assigning them a universal biological meaning.
    """

    interval: Region
    interpretation: str = ""
    value: float | str | bool | None = None
    unit: str | None = None
    uncertainty: Mapping[str, float] = field(default_factory=dict)
    missing_reason: str | None = None
    provenance: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.interval, Region):
            raise EvidenceError("record interval must be a Region")
        object.__setattr__(
            self,
            "interpretation",
            _normalise_text(self.interpretation, field_name="record interpretation"),
        )
        if self.unit is not None:
            object.__setattr__(
                self, "unit", _normalise_text(self.unit, field_name="record unit")
            )
        if self.missing_reason is not None:
            object.__setattr__(
                self,
                "missing_reason",
                _normalise_text(
                    self.missing_reason, field_name="record missing_reason"
                ),
            )

        value = self.value
        if isinstance(value, bool) or value is None or isinstance(value, str):
            pass
        elif isinstance(value, (int, float)):
            value = float(value)
            if not math.isfinite(value):
                raise EvidenceError("record value must be finite")
            object.__setattr__(self, "value", value)
        else:
            raise EvidenceError(
                "record value must be a finite number, string, boolean, or null"
            )

        if not isinstance(self.uncertainty, Mapping):
            raise EvidenceError("record uncertainty must be a JSON object")
        uncertainty: dict[str, float] = {}
        for name, raw_value in self.uncertainty.items():
            if not isinstance(name, str):
                raise EvidenceError("record uncertainty has a non-string key")
            if isinstance(raw_value, bool) or not isinstance(raw_value, (int, float)):
                raise EvidenceError(
                    f"record uncertainty {name!r} must be a finite number"
                )
            number = float(raw_value)
            if not math.isfinite(number):
                raise EvidenceError(
                    f"record uncertainty {name!r} must be a finite number"
                )
            uncertainty[name] = number
        object.__setattr__(self, "uncertainty", MappingProxyType(uncertainty))
        object.__setattr__(
            self, "provenance", _freeze_mapping(self.provenance, path="record provenance")
        )
        object.__setattr__(
            self, "metadata", _freeze_mapping(self.metadata, path="record metadata")
        )

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-ready representation without inferred semantics."""
        return {
            "interval": {
                "start": self.interval.start,
                "end": self.interval.end,
                "name": self.interval.name,
                "parent": self.interval.parent,
            },
            "value": self.value,
            "unit": self.unit,
            "uncertainty": dict(self.uncertainty),
            "missing_reason": self.missing_reason,
            "interpretation": self.interpretation,
            "provenance": _thaw_json(self.provenance),
            "metadata": _thaw_json(self.metadata),
        }


@dataclass(frozen=True)
class EvidenceTrack:
    """A versioned, condition-linked collection of experimental annotations.

    A track is only associated with a target sequence after
    :meth:`validate_against` succeeds.  This keeps the sequence checksum and
    coordinate validation explicit instead of assuming a similarly named
    transcript is identical.
    """

    evidence_type: EvidenceType
    source: str
    condition_id: str
    transcript_id: str
    sequence_hash: str
    records: tuple[EvidenceRecord, ...]
    provenance: Mapping[str, Any] = field(default_factory=dict)
    schema_version: str = EVIDENCE_SCHEMA_VERSION
    coordinate_system: str = "one_based_inclusive"
    interpretation: str = ""
    missingness: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)
    track_id: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.evidence_type, str) or self.evidence_type not in EVIDENCE_TYPES:
            raise EvidenceError(
                f"unknown evidence_type {self.evidence_type!r}; expected one of "
                + ", ".join(sorted(EVIDENCE_TYPES))
            )
        for name in ("source", "condition_id", "transcript_id", "track_id"):
            object.__setattr__(
                self, name, _normalise_text(getattr(self, name), field_name=name)
            )
        object.__setattr__(
            self,
            "interpretation",
            _normalise_text(self.interpretation, field_name="track interpretation"),
        )
        if self.coordinate_system != "one_based_inclusive":
            raise EvidenceError(
                "evidence coordinates must use one_based_inclusive convention"
            )
        if not isinstance(self.sequence_hash, str) or not _SHA256.fullmatch(
            self.sequence_hash
        ):
            raise EvidenceError("sequence_hash must be a 64-character SHA-256 hex digest")
        object.__setattr__(self, "sequence_hash", self.sequence_hash.lower())
        object.__setattr__(
            self, "schema_version", _normalise_schema_version(self.schema_version)
        )

        try:
            records = tuple(self.records)
        except TypeError as exc:
            raise EvidenceError("evidence track records must be iterable") from exc
        if not records:
            raise EvidenceError("evidence track must contain at least one record")
        if any(not isinstance(record, EvidenceRecord) for record in records):
            raise EvidenceError("evidence track records must be EvidenceRecord objects")
        object.__setattr__(self, "records", records)
        object.__setattr__(
            self, "provenance", _freeze_mapping(self.provenance, path="track provenance")
        )
        object.__setattr__(
            self, "missingness", _freeze_mapping(self.missingness, path="track missingness")
        )
        object.__setattr__(
            self, "metadata", _freeze_mapping(self.metadata, path="track metadata")
        )

    def validate_against(self, sequence: Sequence) -> "EvidenceTrack":
        """Verify target identity and every one-based inclusive interval.

        The transcript identifier is deliberately preserved but not matched to
        ``Sequence.name``: FASTA headers are often local aliases.  The exact
        normalized-sequence checksum is the unambiguous identity check.
        """
        if not isinstance(sequence, Sequence):
            raise EvidenceError("evidence validation requires a Sequence")
        if self.sequence_hash != sequence.sha256:
            raise EvidenceError(
                "evidence track sequence_hash does not match the target sequence"
            )
        for index, record in enumerate(self.records, start=1):
            try:
                record.interval.slice(sequence)
            except SequenceError as exc:
                raise EvidenceError(
                    f"evidence record {index} has invalid target coordinates: {exc}"
                ) from None
        return self

    def to_dict(self) -> dict[str, Any]:
        """Return the canonical, JSON-ready version-1 representation."""
        return {
            "evidence_schema_version": self.schema_version,
            "track_id": self.track_id,
            "evidence_type": self.evidence_type,
            "source": self.source,
            "condition_id": self.condition_id,
            "transcript_id": self.transcript_id,
            "sequence_hash": self.sequence_hash,
            "coordinate_system": self.coordinate_system,
            "interpretation": self.interpretation,
            "missingness": _thaw_json(self.missingness),
            "provenance": _thaw_json(self.provenance),
            "metadata": _thaw_json(self.metadata),
            "records": [record.to_dict() for record in self.records],
        }
