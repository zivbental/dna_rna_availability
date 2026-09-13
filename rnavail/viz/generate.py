"""Per-candidate visual bundle: a base-pair probability heatmap and a 2D
structure diagram, both for the candidate folded on its own.

This module intentionally knows nothing about the metrics adapters. It folds
its own local window purely for rendering, independent of whatever the
accessibility adapters computed, because a heatmap needs the full NxN
base-pair probability matrix and a structure needs a layout — objects nobody
wants sitting in a JSON report, and not something the metrics layer should be
made to carry around on their behalf.

The window folded is the candidate region plus flanking context, not the bare
site and not the whole transcript: a bare 20-30 nt site would remove exactly
the neighbouring sequence that might bury or expose it, and folding an entire
long transcript for every candidate would be needlessly slow. See
:data:`DEFAULT_FLANK`.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..adapters import _vienna as V
from ..core.model import ModelSettings, ProbingData
from ..core.sequence import Region, Sequence
from .dotplot import bpp_to_matrix, render_bpp_heatmap
from .mpl import available as mpl_available
from .structure import Highlight, render_structure

#: Context folded on each side of a candidate for its diagrams.
DEFAULT_FLANK = 60

CANDIDATE_COLOR = "#d9622b"


@dataclass
class CandidateVisuals:
    context: Region
    heatmap: str
    structure: str


def build_candidate_visuals(
    sequence: Sequence,
    region: Region,
    settings: ModelSettings,
    flank: int = DEFAULT_FLANK,
    probing: ProbingData | None = None,
) -> CandidateVisuals:
    """Fold and render the self-folding heatmap and structure for one candidate."""
    if not mpl_available():
        raise RuntimeError(
            "matplotlib is not installed; install it to enable visual reports"
        )

    settings = settings.for_molecule(sequence.molecule)
    context = region.with_flanks(flank, flank, len(sequence))
    context_seq = context.slice(sequence)
    local = region.to_local(context)

    context_probing = probing.sliced(context.start, context.end) if probing else None
    structure_str, bpp = _fold(context_seq, settings, probing=context_probing)
    heatmap = render_bpp_heatmap(
        bpp_to_matrix(bpp, len(context_seq)),
        title=f"{region.label} — folded on itself",
        highlight=(local.start, local.end),
    )
    structure = render_structure(
        context_seq, structure_str,
        title=f"{region.label} — folded on itself",
        highlights=(Highlight(local.start, local.end, CANDIDATE_COLOR, region.label),),
    )
    return CandidateVisuals(context=context, heatmap=heatmap, structure=structure)


def _fold(
    seq: str, settings: ModelSettings, probing: ProbingData | None = None,
) -> tuple[str, list[list[float]]]:
    fc = V.make_fold_compound(seq, settings, probing=probing)
    structure, mfe = fc.mfe()
    fc.exp_params_rescale(mfe)
    fc.pf()
    return structure, fc.bpp()
