"""Folding-model settings shared by every thermodynamic adapter.

Keeping these in one object matters more than it looks: accessibility numbers
are only comparable between candidates when every candidate was folded under
an identical protocol. Passing the same :class:`ModelSettings` to each adapter
is what makes the final ranking meaningful.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, field, replace
from typing import Any, Iterator, Literal

ParamSet = Literal[
    "turner2004",
    "turner1999",
    "andronescu2007",
    "langdon2018",
    "dna_mathews2004",
    "dna_mathews1999",
]

SeedMode = Literal["any", "five_prime", "three_prime", "fixed", "listed"]
SeedNucleationStatus = Literal["complementary", "exploratory", "not_applicable"]


# These are mechanisms for which a short complementary stretch is a useful
# structural proxy for initiation.  Keeping the list explicit is deliberate:
# a free best-seed search should not become an unstated affinity model for an
# arbitrary protein, ligand, or custom binder.
_COMPLEMENTARY_SEED_BINDER_CLASSES = frozenset({
    "generic_complementary_strand",
    "complementary_strand",
    "dna_probe",
    "rna_probe",
    "antisense",
    "antisense_oligo",
    "aso",
    "sirna",
    "mirna",
    "guide_rna",
    "crispr_guide",
    "cas13",
    "toehold_trigger",
    "primer",
})


@dataclass(frozen=True)
class RecognitionSpec:
    """The molecular recognition event used to interpret accessibility."""

    binder_class: str = "unspecified"
    partner_sequence: str | None = None
    partner_chemistry: str = "unspecified"
    seed_mode: SeedMode = "any"
    seed_lengths: tuple[int, ...] = (10,)
    seed_start: int | None = None
    listed_seed_starts: tuple[int, ...] = ()
    orientation: str = "unspecified"
    endpoint: str = "structural_opening"

    def __post_init__(self) -> None:
        if not self.seed_lengths or any(length < 1 for length in self.seed_lengths):
            raise ValueError("seed_lengths must contain positive integers")
        if self.seed_mode not in (
            "any", "five_prime", "three_prime", "fixed", "listed"
        ):
            raise ValueError(f"unknown seed_mode {self.seed_mode!r}")
        if self.seed_mode == "fixed" and self.seed_start is None:
            raise ValueError("fixed seed mode requires seed_start")
        if self.seed_mode == "listed" and not self.listed_seed_starts:
            raise ValueError("listed seed mode requires listed_seed_starts")
        if any(start < 1 for start in self.listed_seed_starts):
            raise ValueError("listed_seed_starts must be one-based and positive")

    def to_dict(self) -> dict[str, Any]:
        return {
            "binder_class": self.binder_class,
            "partner_sequence": self.partner_sequence,
            "partner_chemistry": self.partner_chemistry,
            "seed_mode": self.seed_mode,
            "seed_lengths": list(self.seed_lengths),
            "seed_start": self.seed_start,
            "listed_seed_starts": list(self.listed_seed_starts),
            "orientation": self.orientation,
            "endpoint": self.endpoint,
        }

    def identifier(self) -> str:
        digest = hashlib.sha256(
            json.dumps(self.to_dict(), sort_keys=True).encode()
        ).hexdigest()[:16]
        return f"recognition:{digest}"

    @property
    def normalized_binder_class(self) -> str:
        """A stable spelling for comparing declared binder mechanisms."""
        return self.binder_class.strip().lower().replace("-", "_").replace(" ", "_")

    @property
    def seed_nucleation_status(self) -> SeedNucleationStatus:
        """Whether a best unpaired seed has a declared mechanistic role.

        An unspecified class retains the historical generic seed scan as an
        exploratory complementary-strand proxy.  A named class must be in
        the explicit complementary set to make seed accessibility part of a
        rank; in particular, protein, small-molecule, and custom binders do
        not get an implied base-pair nucleation mechanism.
        """
        binder_class = self.normalized_binder_class
        if binder_class in _COMPLEMENTARY_SEED_BINDER_CLASSES:
            return "complementary"
        if binder_class in ("", "unspecified"):
            return "exploratory"
        return "not_applicable"

    @property
    def supports_seed_nucleation(self) -> bool:
        """Whether seed placement and seed accessibility may affect a rank."""
        return self.seed_nucleation_status != "not_applicable"

    def permitted_seed_starts(
        self, region: "Region", seed_length: int,
    ) -> list[int]:
        """Return allowed one-based seed starts that fit ``region``.

        Fixed and listed positions use the target sequence's coordinate
        system. A listed event can therefore name several global positions;
        each candidate receives only the placements inside its footprint.
        Callers that require an actual seed must reject an empty result rather
        than interpreting it as a completed seed scan.
        """
        if seed_length < 1 or seed_length > len(region):
            return []
        first = region.start
        last = region.end - seed_length + 1
        if self.seed_mode == "five_prime":
            return [first]
        if self.seed_mode == "three_prime":
            return [last]
        if self.seed_mode == "fixed":
            starts = [int(self.seed_start)]
        elif self.seed_mode == "listed":
            starts = sorted(set(self.listed_seed_starts))
        else:
            return list(range(first, last + 1))
        return [start for start in starts if first <= start <= last]

    @property
    def requires_declared_seed(self) -> bool:
        """Whether a candidate is valid only when it contains a listed seed.

        Fixed/listed coordinates describe a complementary nucleation event.
        They are not validity constraints for a binder that has no declared
        complementary seed mechanism.
        """
        return self.supports_seed_nucleation and self.seed_mode in (
            "fixed", "listed"
        )


@dataclass(frozen=True)
class ConditionSpec:
    """Experimental conditions that qualify an accessibility estimate."""

    condition_id: str = "unspecified"
    temperature_c: float = 37.0
    sodium_molar: float | None = None
    potassium_molar: float | None = None
    magnesium_total_molar: float | None = None
    magnesium_free_molar: float | None = None
    ph: float | None = None
    incubation_seconds: float | None = None
    preparation: str = "unspecified"
    partner_concentration_molar: float | None = None
    crowding_agent: str | None = None
    crowding_concentration: str | None = None
    organism: str | None = None
    cell_type: str | None = None
    compartment: str | None = None

    def __post_init__(self) -> None:
        concentrations = (
            self.sodium_molar, self.potassium_molar,
            self.magnesium_total_molar, self.magnesium_free_molar,
            self.partner_concentration_molar,
        )
        if any(
            value is not None and (not math.isfinite(value) or value < 0)
            for value in concentrations
        ):
            raise ValueError("condition concentrations must be finite and non-negative")
        if self.incubation_seconds is not None and (
            not math.isfinite(self.incubation_seconds) or self.incubation_seconds < 0
        ):
            raise ValueError("incubation_seconds must be finite and non-negative")
        if not math.isfinite(self.temperature_c):
            raise ValueError("condition temperature_c must be finite")
        if self.ph is not None and not math.isfinite(self.ph):
            raise ValueError("condition ph must be finite")

    def to_dict(self) -> dict[str, Any]:
        return {
            "condition_id": self.condition_id,
            "temperature_c": self.temperature_c,
            "sodium_molar": self.sodium_molar,
            "potassium_molar": self.potassium_molar,
            "magnesium_total_molar": self.magnesium_total_molar,
            "magnesium_free_molar": self.magnesium_free_molar,
            "ph": self.ph,
            "incubation_seconds": self.incubation_seconds,
            "preparation": self.preparation,
            "partner_concentration_molar": self.partner_concentration_molar,
            "crowding_agent": self.crowding_agent,
            "crowding_concentration": self.crowding_concentration,
            "organism": self.organism,
            "cell_type": self.cell_type,
            "compartment": self.compartment,
        }

    def unsupported_by_secondary_structure_model(self) -> dict[str, object]:
        unsupported: dict[str, object] = {}
        for name in (
            "magnesium_total_molar", "magnesium_free_molar", "ph",
            "incubation_seconds", "preparation", "partner_concentration_molar",
            "crowding_agent", "crowding_concentration", "organism", "cell_type",
            "compartment",
        ):
            value = getattr(self, name)
            if value is not None and value != "unspecified":
                unsupported[name] = value
        if self.potassium_molar is not None:
            unsupported["potassium_molar"] = self.potassium_molar
        return unsupported

#: Maps our parameter-set names onto the ViennaRNA loader functions.
PARAM_LOADERS: dict[str, str] = {
    "turner2004": "params_load_RNA_Turner2004",
    "turner1999": "params_load_RNA_Turner1999",
    "andronescu2007": "params_load_RNA_Andronescu2007",
    "langdon2018": "params_load_RNA_Langdon2018",
    "dna_mathews2004": "params_load_DNA_Mathews2004",
    "dna_mathews1999": "params_load_DNA_Mathews1999",
}


@dataclass(frozen=True)
class ModelSettings:
    """Everything that changes a folding free energy.

    Attributes
    ----------
    temperature_c:
        Folding temperature in degrees Celsius.
    param_set:
        Nearest-neighbour parameter set. Use a ``dna_*`` set for DNA targets.
    dangles:
        ViennaRNA dangling-end model (0, 1, 2 or 3). 2 is the ViennaRNA
        default and the usual choice for partition functions.
    no_lonely_pairs:
        Disallow helices of length one. Tends to make accessibility estimates
        less jittery at the cost of some accuracy on real lone pairs.
    no_gu / no_gu_closure:
        Forbid GU pairs entirely, or only as helix-closing pairs.
    salt_molar:
        Monovalent salt concentration in mol/L for ViennaRNA's salt
        correction. ``None`` leaves the default (1.021 M) untouched.
    max_bp_span:
        Longest allowed base pair in local/window calculations. This is the
        ``-L`` of RNAplfold and the ``W`` of Raccess.
    global_max_bp_span:
        Optional longest allowed base pair in whole-sequence calculations.
        ``None`` leaves global folds unrestricted instead of silently
        inheriting the local screening approximation.
    window_size:
        Local folding window, the ``-W`` of RNAplfold. Must be >= max_bp_span.
    max_unpaired:
        Longest unpaired stretch whose joint probability the local engine
        tabulates, the ``-u`` of RNAplfold.
    """

    temperature_c: float = 37.0
    param_set: ParamSet = "turner2004"
    dangles: int = 2
    no_lonely_pairs: bool = False
    no_gu: bool = False
    no_gu_closure: bool = False
    gquad: bool = False
    circular: bool = False
    salt_molar: float | None = None
    max_bp_span: int = 150
    global_max_bp_span: int | None = None
    window_size: int = 200
    max_unpaired: int = 30

    def __post_init__(self) -> None:
        if not math.isfinite(self.temperature_c):
            raise ValueError("temperature_c must be finite")
        if self.salt_molar is not None and (
            not math.isfinite(self.salt_molar) or self.salt_molar < 0
        ):
            raise ValueError("salt_molar must be finite and non-negative")
        if self.param_set not in PARAM_LOADERS:
            raise ValueError(
                f"unknown parameter set {self.param_set!r}; "
                f"choose from {sorted(PARAM_LOADERS)}"
            )
        if self.dangles not in (0, 1, 2, 3):
            raise ValueError(f"dangles must be 0, 1, 2 or 3, got {self.dangles}")
        if self.window_size < self.max_bp_span:
            raise ValueError(
                f"window_size ({self.window_size}) must be at least "
                f"max_bp_span ({self.max_bp_span}); RNAplfold cannot look for "
                "pairs further apart than the window it folds"
            )
        if self.global_max_bp_span is not None and self.global_max_bp_span < 1:
            raise ValueError("global_max_bp_span must be positive or None")
        if self.max_unpaired < 1:
            raise ValueError("max_unpaired must be at least 1")

    @property
    def is_dna(self) -> bool:
        return self.param_set.startswith("dna_")

    def for_molecule(self, molecule: str) -> "ModelSettings":
        """Return settings whose parameter set matches ``molecule``."""
        if molecule == "dna" and not self.is_dna:
            return replace(self, param_set="dna_mathews2004")
        if molecule == "rna" and self.is_dna:
            return replace(self, param_set="turner2004")
        return self

    def variants(self) -> Iterator["ModelSettings"]:
        """Yield a small ensemble of perturbed settings for robustness checks.

        The doc's rule "prefer sites robust across model/window settings"
        needs an actual perturbation set; this is it. Each variant changes one
        assumption that is genuinely uncertain rather than merely arbitrary.
        """
        yield self
        yield replace(self, temperature_c=self.temperature_c - 5.0)
        yield replace(self, temperature_c=self.temperature_c + 5.0)
        yield replace(self, dangles=0 if self.dangles else 2)
        yield replace(self, no_lonely_pairs=not self.no_lonely_pairs)
        wider = min(self.max_bp_span * 2, 400)
        yield replace(self, max_bp_span=wider, window_size=max(wider, self.window_size))
        narrower = max(40, self.max_bp_span // 2)
        yield replace(self, max_bp_span=narrower, window_size=max(narrower, 80))
        # gquad is deliberately not varied here: this sweep always runs
        # through rnaplfold, and ViennaRNA's local/window partition function
        # segfaults outright when gquad is combined with OPTION_WINDOW (see
        # the guard in adapters/_vienna.py). A whole-sequence engine such as
        # vienna-exact or rnafold is the safe way to test gquad sensitivity.

    def to_dict(self) -> dict[str, Any]:
        return {
            "temperature_c": self.temperature_c,
            "param_set": self.param_set,
            "dangles": self.dangles,
            "no_lonely_pairs": self.no_lonely_pairs,
            "no_gu": self.no_gu,
            "no_gu_closure": self.no_gu_closure,
            "gquad": self.gquad,
            "circular": self.circular,
            "salt_molar": self.salt_molar,
            "max_bp_span": self.max_bp_span,
            "global_max_bp_span": self.global_max_bp_span,
            "window_size": self.window_size,
            "max_unpaired": self.max_unpaired,
        }

    def signature(self) -> str:
        """Short stable string identifying this protocol, for report headers."""
        bits = [
            f"T{self.temperature_c:g}",
            self.param_set,
            f"d{self.dangles}",
            f"L{self.max_bp_span}",
            f"W{self.window_size}",
            (
                f"GL{self.global_max_bp_span}"
                if self.global_max_bp_span is not None else "GLall"
            ),
        ]
        if self.no_lonely_pairs:
            bits.append("noLP")
        if self.no_gu:
            bits.append("noGU")
        if self.gquad:
            bits.append("gquad")
        if self.circular:
            bits.append("circ")
        if self.salt_molar is not None:
            bits.append(f"salt{self.salt_molar:g}")
        return "/".join(bits)


@dataclass(frozen=True)
class ProbingData:
    """Experimental SHAPE/DMS reactivities for one sequence.

    ``reactivities`` is 1-based and parallel to the sequence; ``None`` marks
    positions with no data (primer sites, low coverage), which the soft
    constraint must leave unperturbed rather than treat as zero.
    """

    reactivities: tuple[float | None, ...]
    method: Literal["deigan", "zarringhalam", "eddy2"] = "deigan"
    source: str = ""
    slope: float = 1.8
    intercept: float = -0.6
    beta: float = 0.89
    chemistry: str = "SHAPE"
    condition_id: str = "unspecified"
    sequence_hash: str = ""
    source_hash: str = ""
    conversion_explicit: bool = False

    def __post_init__(self) -> None:
        for index, value in enumerate(self.reactivities, start=1):
            if value is not None and not math.isfinite(float(value)):
                raise ValueError(
                    f"probing reactivity at position {index} is not finite"
                )
        for name in ("slope", "intercept", "beta"):
            value = getattr(self, name)
            if not math.isfinite(float(value)):
                raise ValueError(
                    f"probing conversion parameter {name} is not finite"
                )

    def __len__(self) -> int:
        return len(self.reactivities)

    @property
    def coverage(self) -> float:
        """Fraction of positions carrying a measured value."""
        if not self.reactivities:
            return 0.0
        measured = sum(1 for r in self.reactivities if r is not None)
        return measured / len(self.reactivities)

    def as_vienna_vector(self) -> list[float]:
        """ViennaRNA wants a 1-based list with -999 marking missing data."""
        return [-999.0] + [
            -999.0 if r is None else float(r) for r in self.reactivities
        ]

    def conditioning_id(self) -> str:
        """Stable ID for the exact soft-constraint track and conversion."""
        payload = {
            "reactivities": self.reactivities,
            "method": self.method,
            "slope": self.slope,
            "intercept": self.intercept,
            "beta": self.beta,
            "chemistry": self.chemistry,
            "condition_id": self.condition_id,
            "sequence_hash": self.sequence_hash,
            "conversion_explicit": self.conversion_explicit,
        }
        digest = hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode()
        ).hexdigest()[:16]
        return f"probing:{self.method}:{digest}"

    def sliced(self, start: int, end: int) -> "ProbingData":
        """Restrict the data to a 1-based inclusive window."""
        return ProbingData(
            reactivities=self.reactivities[start - 1 : end],
            method=self.method,
            source=self.source,
            slope=self.slope,
            intercept=self.intercept,
            beta=self.beta,
            chemistry=self.chemistry,
            condition_id=self.condition_id,
            sequence_hash=self.sequence_hash,
            source_hash=self.source_hash,
            conversion_explicit=self.conversion_explicit,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "method": self.method,
            "chemistry": self.chemistry,
            "condition_id": self.condition_id,
            "source": self.source,
            "source_hash": self.source_hash,
            "sequence_hash": self.sequence_hash,
            "coverage": self.coverage,
            "positions": len(self.reactivities),
            "conversion": {
                "explicit": self.conversion_explicit,
                "slope": self.slope,
                "intercept": self.intercept,
                "beta": self.beta,
            },
        }
