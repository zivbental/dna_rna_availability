"""Shared ViennaRNA plumbing.

ViennaRNA's energy parameters are process-global state. Every fold_compound
built here therefore goes through :func:`make_fold_compound`, which loads the
requested parameter set immediately before construction. Doing it in one place
is what stops a DNA calculation from silently inheriting RNA parameters left
behind by a previous call.
"""

from __future__ import annotations

import math
from typing import Any, Iterable

from ..core.model import PARAM_LOADERS, ModelSettings, ProbingData
from ..core.result import Availability
from ..core.sequence import Region, Sequence

try:
    import RNA  # type: ignore
    _IMPORT_ERROR = ""
except Exception as exc:                            # pragma: no cover
    RNA = None                                      # type: ignore
    _IMPORT_ERROR = str(exc)

_LOADED_PARAM_SET: str | None = None

#: Re-exported so adapters can reach ViennaRNA calls that need no wrapper.
__all__ = ["RNA"]


def availability() -> Availability:
    """Whether the ViennaRNA Python bindings are importable."""
    if RNA is None:
        return Availability.no(
            f"ViennaRNA python bindings not importable ({_IMPORT_ERROR})",
            hint="pip install ViennaRNA",
        )
    return Availability.yes(f"ViennaRNA {RNA.__version__}")


def version() -> str:
    return f"ViennaRNA {RNA.__version__}" if RNA else ""


def load_parameters(settings: ModelSettings) -> None:
    """Install ``settings.param_set`` into ViennaRNA's global parameter tables."""
    global _LOADED_PARAM_SET
    if _LOADED_PARAM_SET == settings.param_set:
        return
    loader = getattr(RNA, PARAM_LOADERS[settings.param_set], None)
    if loader is None:
        raise RuntimeError(
            f"this ViennaRNA build has no loader for {settings.param_set!r}"
        )
    loader()
    _LOADED_PARAM_SET = settings.param_set


def make_md(settings: ModelSettings, local: bool = False,
            uniq_ml: bool = False) -> Any:
    """Build a ViennaRNA model-details object from our settings.

    ``uniq_ml`` switches on unique multiloop decomposition, which stochastic
    backtracking requires; without it ViennaRNA silently returns no samples.
    """
    md = RNA.md()
    if uniq_ml:
        md.uniq_ML = 1
    md.temperature = settings.temperature_c
    md.dangles = settings.dangles
    md.noLP = 1 if settings.no_lonely_pairs else 0
    md.noGU = 1 if settings.no_gu else 0
    md.noGUclosure = 1 if settings.no_gu_closure else 0
    md.gquad = 1 if settings.gquad else 0
    md.circ = 1 if settings.circular else 0
    if settings.salt_molar is not None:
        md.salt = settings.salt_molar
    md.max_bp_span = (
        settings.max_bp_span if local
        else settings.global_max_bp_span if settings.global_max_bp_span is not None
        else -1
    )
    md.window_size = settings.window_size if local else -1
    return md


def make_fold_compound(
    sequence: str,
    settings: ModelSettings,
    options: int | None = None,
    probing: ProbingData | None = None,
    uniq_ml: bool = False,
) -> Any:
    """Create a fold_compound with parameters, model details and constraints.

    ``probing`` attaches SHAPE/DMS-derived soft constraints using whichever
    of the three ViennaRNA conversion methods the data object requests.
    """
    load_parameters(settings)
    md = make_md(settings, local=options == RNA.OPTION_WINDOW, uniq_ml=uniq_ml)
    if options is None:
        fc = RNA.fold_compound(sequence, md)
    else:
        fc = RNA.fold_compound(sequence, md, options)
    if probing is not None:
        apply_probing(fc, probing, len(sequence))
    return fc


def apply_probing(fc: Any, probing: ProbingData, length: int) -> None:
    """Attach SHAPE/DMS reactivities as soft constraints."""
    if len(probing) != length:
        raise ValueError(
            f"probing data covers {len(probing)} positions but the sequence "
            f"is {length} nt long"
        )
    vector = probing.as_vienna_vector()
    if probing.chemistry.upper().startswith("DMS") and not probing.conversion_explicit:
        raise ValueError(
            "DMS data need an explicitly selected conversion; do not apply a "
            "SHAPE pseudoenergy model by default"
        )
    if probing.method == "deigan":
        fc.sc_add_SHAPE_deigan(vector, probing.slope, probing.intercept)
    elif probing.method == "zarringhalam":
        # ViennaRNA's Zarringhalam conversion wants a string describing how to
        # treat missing values; "O" leaves them unconstrained.
        fc.sc_add_SHAPE_zarringhalam(vector, probing.beta, -1.0, "O")
    elif probing.method == "eddy2":
        fc.sc_add_SHAPE_eddy_2(vector, [], [])
    else:
        raise ValueError(f"unknown probing method {probing.method!r}")


def ensemble_free_energy(fc: Any) -> float:
    """Run the partition function and return the ensemble free energy."""
    _, energy = fc.pf()
    return float(energy)


def constrained_free_energy(
    sequence: str,
    settings: ModelSettings,
    unpaired: Iterable[int],
    probing: ProbingData | None = None,
) -> float:
    """Ensemble free energy with the given 1-based positions forced unpaired.

    Positions are bounds-checked before they reach ViennaRNA. This is not
    defensive padding: ``hc_add_up`` performs no validation of its own and
    writes past the end of the constraint array for an out-of-range index,
    taking the whole process down with SIGSEGV rather than raising. A bad
    region has to become a Python exception here, so the adapter layer can
    turn it into a failed result like any other error.
    """
    positions = list(unpaired)
    if settings.gquad:
        raise ValueError(
            "joint unpaired probability is undefined with gquad=True: "
            "ViennaRNA's unpaired hard constraint does not exclude target "
            "nucleotides from modeled G-quadruplexes"
        )
    length = len(sequence)
    out_of_range = [p for p in positions if not 1 <= p <= length]
    if out_of_range:
        raise ValueError(
            f"positions {out_of_range[:5]} are outside the sequence "
            f"(1..{length}); ViennaRNA would segfault on these"
        )

    fc = make_fold_compound(sequence, settings, probing=probing)
    for position in positions:
        fc.hc_add_up(position)
    return ensemble_free_energy(fc)


def unpaired_probabilities(fc: Any) -> list[float]:
    """Per-nucleotide unpaired probability, 1-based (index 0 is padding).

    Requires that ``fc.pf()`` has already been called so the base-pair
    probability matrix exists.
    """
    bpp = fc.bpp()
    length = fc.length
    paired = [0.0] * (length + 1)
    for i in range(1, length + 1):
        for j in range(i + 1, length + 1):
            p = bpp[i][j]
            if p:
                paired[i] += p
                paired[j] += p
    return [0.0] + [max(0.0, min(1.0, 1.0 - paired[i])) for i in range(1, length + 1)]


def positional_entropy(fc: Any) -> list[float]:
    """Per-nucleotide Shannon entropy of the pairing distribution, 1-based."""
    return list(fc.positional_entropy())


def local_unpaired_matrix(
    sequence: str,
    settings: ModelSettings,
    max_unpaired: int,
    probing: ProbingData | None = None,
) -> dict[int, list[float | None]]:
    """RNAplfold's unpaired-probability table via the sliding-window engine.

    Returns ``{j: [None, p1, p2, ...]}`` where ``p_u`` is the probability that
    the u nucleotides ending at position j are all unpaired, matching
    RNAplfold's own ``-u`` output convention.
    """
    if settings.gquad:
        # ViennaRNA's local/window partition function does not implement
        # G-quadruplex folding and segfaults the whole process rather than
        # raising when the two are combined (reproduced against 2.7.2). Turn
        # that into a normal Python exception before it ever reaches the C
        # library, so a --gquad run degrades this one adapter instead of
        # crashing the interpreter.
        raise ValueError(
            "RNAplfold's local/window engine cannot combine with gquad=True "
            "(ViennaRNA crashes rather than erroring on this combination); "
            "use rnafold only for global G4-aware structural descriptors; "
            "joint G4-aware accessibility is deliberately unavailable"
        )
    fc = make_fold_compound(
        sequence, settings, options=RNA.OPTION_WINDOW, probing=probing
    )
    table: dict[int, list[float | None]] = {}

    def callback(values: Any, length: int, index: int, maxlen: int,
                 what: int, data: Any) -> None:
        if what & RNA.PROBS_WINDOW_UP:
            table[index] = list(values)

    fc.probs_window(max_unpaired, RNA.PROBS_WINDOW_UP, callback, None)
    return table


def region_probability_from_table(
    table: dict[int, list[float | None]], region: Region
) -> float | None:
    """Read P(all of ``region`` unpaired) out of a local unpaired table."""
    length = len(region)
    row = table.get(region.end)
    if row is None or length >= len(row):
        return None
    value = row[length]
    if value is None or not math.isfinite(value):
        return None
    return max(0.0, min(1.0, float(value)))


def best_seed(
    table_or_fn: Any,
    region: Region,
    seed_length: int,
    starts: Iterable[int] | None = None,
) -> tuple[int, float] | None:
    """Find the most accessible seed of ``seed_length`` inside ``region``.

    ``table_or_fn`` is either a local unpaired table or a callable taking a
    :class:`Region` and returning its joint unpaired probability. Returns
    ``(seed_start, probability)`` for the best placement, or None if the seed
    does not fit or nothing could be scored.
    """
    if seed_length > len(region):
        return None
    best: tuple[int, float] | None = None
    allowed = (
        list(starts) if starts is not None
        else list(range(region.start, region.end - seed_length + 2))
    )
    for start in allowed:
        seed = Region(start, start + seed_length - 1)
        if callable(table_or_fn):
            probability = table_or_fn(seed)
        else:
            probability = region_probability_from_table(table_or_fn, seed)
        if probability is None:
            continue
        if best is None or probability > best[1]:
            best = (start, probability)
    return best
