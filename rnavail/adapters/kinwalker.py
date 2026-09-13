"""Kinwalker: does the region survive being folded while it is transcribed.

Every other adapter here answers an equilibrium question — fold the finished
molecule and ask what fraction of the ensemble has this region open. None of
them ask whether that equilibrium is ever reached. RNA starts folding as soon
as its 5' end leaves the polymerase, nucleotides at a time, and a helix that
forms early can be kinetically trapped: stable enough that the molecule never
crosses the energy barrier back out of it, even though the finished
transcript's global energy landscape says a different, more open fold is
available. Equilibrium prediction cannot see this by construction, because it
integrates over all time.

Kinwalker (Geis et al. 2008) simulates exactly this: it grows the sequence
one nucleotide at a time and, at each step, folds only the additional
structure that is both locally optimal and reachable without crossing an
energy barrier deemed too high to cross during transcription. Its output is a
trajectory of the structures actually adopted, in order, each tagged with the
transcript length at which it formed. Growth is not strictly monotonic —
reaching a new, sufficiently better structure can rearrange bases that were
already paired — so "trap length" here is defined from the end backward: the
earliest transcript length after which the region stays in its final paired
state with no further reopening, not merely the first time it was ever seen
paired in passing.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..core.result import Availability, M, Tier, ToolResult
from ..core.sequence import Region
from .base import AccessibilityAdapter, AccessibilityRequest
from .external import find_binary, run_command
from .registry import register

#: kinwalker's default barrier heuristic scales far worse than quadratically:
#: measured in this environment at 100 nt (7.5 s), 120 nt (9 s), 130 nt
#: (10.4 s), 140 nt (17.7 s), 150 nt (> 30 s and climbing). It runs by
#: default on every ``evaluate``/``scan`` call, so without a ceiling a single
#: transcript-length target would make every default run impractically slow
#: or effectively hang. This keeps it usable for what it is genuinely suited
#: to — a short designed construct such as a toehold switch — and out of the
#: way of a whole-transcript scan, which should exclude it with
#: ``--tools`` or ``--max-cost`` instead of discovering the hang by waiting.
MAX_PRACTICAL_LENGTH = 140


@dataclass
class _Event:
    """One row of a kinwalker trajectory: the structure as of one transcript length."""

    structure: str
    length: int


@register
class KinwalkerAdapter(AccessibilityAdapter):
    name = "kinwalker"
    tier = Tier.STRUCTURE
    cost = 3
    orthogonal = True
    #: One simulated trajectory's structure at one instant, not an ensemble:
    #: excluded from the primary per-base probability statistic for the same
    #: reason as linearfold.
    estimand = "single_structure"
    description = (
        "Kinwalker co-transcriptional folding trajectory: whether the region "
        "gets kinetically trapped closed before the transcript is even "
        "finished, something no equilibrium calculation can see"
    )
    provides = (M.MEAN_BASE_UNPAIRED, M.PAIRED_FRACTION, M.CO_TX_TRAP_LENGTH)

    def availability(self) -> Availability:
        if not find_binary("kinwalker"):
            return Availability.no(
                "kinwalker binary not found", hint="run tools/install_tools.sh"
            )
        # kinwalker has no --version flag; it only ever prints its usage
        # message, which is not worth surfacing as a "version".
        return Availability.yes("kinwalker (Geis et al. 2008)")

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        sequence = request.sequence

        if settings.is_dna:
            result.warn(
                "kinwalker folds with RNA-only heuristics; its transcription "
                "kinetics are not meaningful for a DNA target"
            )

        max_length = int(request.options.get(
            "kinwalker_max_length", MAX_PRACTICAL_LENGTH
        ))
        if len(sequence) > max_length:
            raise RuntimeError(
                f"sequence is {len(sequence)} nt; kinwalker's runtime "
                f"explodes well before typical transcript lengths (measured "
                f"superlinear blowup past ~150 nt in this environment), so "
                f"this adapter refuses above {max_length} nt rather than "
                "hanging the whole run. It is built for a short designed "
                "construct, not a transcript scan; raise the ceiling with "
                "options={'kinwalker_max_length': N} if you accept the cost"
            )

        # kinwalker's own --nolonely flag is documented but rejected by the
        # binary in this build (a getopt table mismatch upstream, not
        # something this adapter can fix); --dangle is the one folding-model
        # knob it reliably accepts.
        args = [find_binary("kinwalker"), "--dangle", str(min(settings.dangles, 2))]
        proc = run_command(args, stdin=f"{sequence.seq}\n", timeout=1800)
        final_structure, events = _parse_trajectory(proc.stdout, len(sequence))
        if final_structure is None:
            raise RuntimeError("kinwalker produced no final structure")

        result.detail["final_structure"] = final_structure
        result.detail["n_trajectory_events"] = len(events)
        result.detail["note"] = (
            "one simulated folding path under a specific barrier heuristic, "
            "not an ensemble; treat the trap length as a plausibility check, "
            "not a rate"
        )

        for region in request.regions:
            metrics = result.region_metrics(region)
            window = _state_at(final_structure, events, region.end)
            local = window[region.start - 1 : region.end]
            open_fraction = local.count(".") / len(local)
            metrics.set(M.MEAN_BASE_UNPAIRED, open_fraction)
            metrics.set(M.PAIRED_FRACTION, 1.0 - open_fraction)
            metrics.detail["co_tx_final_substructure"] = local

            trap_length = _final_trap_length(events, region)
            if trap_length is not None:
                metrics.set(M.CO_TX_TRAP_LENGTH, trap_length)
                metrics.detail["co_tx_trapped_before_full_transcript"] = (
                    trap_length < len(sequence)
                )
            else:
                metrics.detail["co_tx_never_trapped"] = True
        return result


def _parse_trajectory(text: str, seq_length: int) -> tuple[str | None, list[_Event]]:
    """Extract the final co-transcriptional structure and the event list.

    Kinwalker's stdout is: the input sequence, the final structure and its
    energy, a ``TRAJECTORY`` marker, then one row per structural event as
    ``<dot-bracket> <energy> <t1> <t2> <rate> <length>``. Each event's
    dot-bracket string is exactly ``length`` characters long, describing the
    whole chain transcribed so far, and later events always extend rather
    than revert earlier ones.
    """
    lines = [ln for ln in text.splitlines() if ln.strip()]
    final_structure: str | None = None
    events: list[_Event] = []
    in_trajectory = False

    for line in lines:
        if line.strip() == "TRAJECTORY":
            in_trajectory = True
            continue
        if line.startswith("Kinwalker run time"):
            break
        fields = line.split()
        if not fields:
            continue
        candidate = fields[0]
        if not (candidate and set(candidate) <= set(".()")):
            continue                                   # the echoed input sequence

        if not in_trajectory:
            if len(candidate) == seq_length:
                final_structure = candidate
            continue

        if len(fields) < 2:
            continue
        try:
            length = int(fields[-1])
        except ValueError:
            continue
        events.append(_Event(structure=candidate, length=length))

    events.sort(key=lambda e: e.length)
    if final_structure is None and events:
        final_structure = events[-1].structure
    return final_structure, events


def _state_at(final_structure: str, events: list[_Event], up_to: int) -> str:
    """Reconstruct the padded structure string covering at least ``up_to`` nt.

    Structure only changes at recorded events and never un-forms what a prior
    event already paired, so the state at any length is the most recent event
    at or before that length, with newly-transcribed, not-yet-paired bases
    appended as dots.
    """
    if up_to <= len(final_structure):
        return final_structure
    asof = final_structure
    for event in events:
        if event.length <= up_to:
            asof = event.structure
    return asof + "." * (up_to - len(asof))


def _final_trap_length(events: list[_Event], region: Region) -> int | None:
    """Transcript length after which the region stays paired to the end.

    Kinwalker can rearrange already-formed structure at a later step, so the
    first appearance of a pair is not necessarily a lasting one. This instead
    walks the trajectory backward from its last event and reports the start
    of the final unbroken run of paired states — the length beyond which the
    region never reopens. None means the region ends the trajectory unpaired,
    regardless of what happened earlier.
    """
    relevant = [e for e in events if e.length >= region.start]
    if not relevant:
        return None

    def paired(event: _Event) -> bool:
        window = event.structure[region.start - 1: min(region.end, event.length)]
        return any(c != "." for c in window)

    if not paired(relevant[-1]):
        return None
    trap_length = relevant[-1].length
    for event in reversed(relevant[:-1]):
        if not paired(event):
            break
        trap_length = event.length
    return trap_length
