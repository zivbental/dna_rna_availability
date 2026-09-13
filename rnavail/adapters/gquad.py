"""G-rich and C-rich sequence propensity, by the G4Hunter score.

Every other adapter in this pipeline reasons about *nested* secondary
structure: stems, hairpins, multiloops. A G-quadruplex is not that — four
runs of guanines can associate into a stack of G-tetrads held together by
Hoogsteen hydrogen bonds, a structure no nearest-neighbour stem model
represents at all. A site that every thermodynamic adapter here calls open
can still be folded shut by a quadruplex the whole rest of the pipeline is
blind to. Negative scores flag C-rich sequence, but are not evidence that an
RNA i-motif is occupied.

This adapter does not fold anything. It scores the raw sequence with
G4Hunter (Bedrat, Lacroix & Mergny 2016, NAR 44:1746): each base gets +1..+4
for sitting in a run of G's (scaled by run length, capped at 4) or the mirror
-1..-4 for a run of C's, and 0 otherwise. A window's score is the mean of its
per-base scores; |score| >= 1.2 is the published threshold above which a
sequence reliably forms a quadruplex in vitro. It is a sequence heuristic, not
a folding calculation — cheap, always available, and orthogonal to everything
else here for exactly that reason.
"""

from __future__ import annotations

from ..core.result import Availability, M, Tier, ToolResult
from .base import AccessibilityAdapter, AccessibilityRequest
from .registry import register

#: The published G4Hunter window. Regions shorter than this are scored as a
#: single window; longer regions are scanned at this width so a quadruplex
#: motif sitting anywhere inside a wide target is not diluted into the mean.
G4HUNTER_WINDOW = 25

#: Published absolute score threshold for sequence propensity. For RNA target
#: interpretation, only a positive peak is labeled G-quadruplex propensity.
G4HUNTER_THRESHOLD = 1.2

#: Longest homopolymer run length that keeps adding to the per-base score;
#: G4Hunter caps here rather than rewarding arbitrarily long runs.
RUN_CAP = 4


def g4hunter_track(seq: str) -> list[float]:
    """Per-base G4Hunter score, 0-based, one value per nucleotide.

    Guanine runs score positive, cytosine runs negative, everything else
    (including ambiguous IUPAC codes) scores zero. ``seq`` is expected in the
    RNA alphabet (U, not T); G4Hunter does not care which pyrimidine it is.
    """
    n = len(seq)
    track = [0.0] * n
    i = 0
    while i < n:
        base = seq[i]
        if base in "GC":
            j = i
            while j < n and seq[j] == base:
                j += 1
            run_len = min(j - i, RUN_CAP)
            score = float(run_len) if base == "G" else -float(run_len)
            for k in range(i, j):
                track[k] = score
            i = j
        else:
            i += 1
    return track


def _window_scores(track: list[float], width: int) -> list[float]:
    """Mean score of every ``width``-wide window, sliding by one base."""
    if width >= len(track):
        return [sum(track) / len(track)] if track else []
    running = sum(track[:width])
    scores = [running / width]
    for i in range(width, len(track)):
        running += track[i] - track[i - width]
        scores.append(running / width)
    return scores


@register
class GQuadAdapter(AccessibilityAdapter):
    name = "gquad-scan"
    tier = Tier.ACCESSIBILITY
    cost = 1
    orthogonal = True
    estimand = "sequence_propensity"
    model_family = "g4hunter"
    algorithm = "signed-sliding-window-score"
    probing_irrelevant = True
    ignored_setting_names = frozenset({
        "temperature_c", "param_set", "dangles", "no_lonely_pairs",
        "no_gu", "no_gu_closure", "gquad", "circular", "salt_molar",
        "max_bp_span", "global_max_bp_span", "window_size", "max_unpaired",
    })
    description = (
        "signed G4Hunter sequence propensity; positive G-rich windows flag "
        "possible G-quadruplex formation outside nested-pair models"
    )
    provides = (M.GQUAD_SCORE,)

    def availability(self) -> Availability:
        return Availability.yes("G4Hunter (Bedrat et al. 2016)")

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        seq = request.sequence.seq
        track = g4hunter_track(seq)
        result.detail["note"] = (
            "a sequence heuristic, not a folding calculation: flags where a "
            "quadruplex could form regardless of what the partition function "
            "says about that position"
        )

        for region in request.regions:
            metrics = result.region_metrics(region)
            local = track[region.start - 1 : region.end]
            width = min(G4HUNTER_WINDOW, len(local))
            windows = _window_scores(local, width)
            if not windows:
                continue
            peak = max(windows, key=abs)
            peak_offset = windows.index(peak)
            metrics.set(M.GQUAD_SCORE, peak)
            metrics.detail["gquad_peak_score"] = peak
            metrics.detail["gquad_peak_strand"] = (
                "G-rich" if peak > 0 else "C-rich" if peak < 0 else "none"
            )
            metrics.detail["gquad_peak_window"] = (
                region.start + peak_offset, region.start + peak_offset + width - 1,
            )
            metrics.detail["gquad_above_threshold"] = peak >= G4HUNTER_THRESHOLD
            metrics.detail["c_rich_below_negative_threshold"] = (
                peak <= -G4HUNTER_THRESHOLD
            )
        return result
