"""Whole-transcript accessibility: a per-base profile at one window length,
and the full (start position, window length) landscape.

Both come from exactly the same object — RNAplfold's own
``{end_position: [None, p_1, p_2, ...]}`` table, the probability that the
``L`` nucleotides ending at each position are simultaneously unpaired for
every ``L`` up to some maximum. The pipeline already computes this whole
table in a single pass to screen a transcript; asking about more of it costs
nothing further. This module answers two things that table already contains
and that nothing before it rendered:

- **the profile** — dG_open per nucleotide at one fixed window length, at
  every position, not just the positions a particular ``--step`` happened to
  tile. Still the correct joint-interval quantity throughout, never the
  per-base marginal that :mod:`rnavail.pipeline.run` warns against ranking on.
- **the landscape** — the same quantity swept over every window length at
  once, so "what length of binder does this site support, and where does it
  stop" is one image instead of a guess.

Neither function folds anything; both take the table the pipeline already
built and are handed it directly, unlike :mod:`rnavail.viz.generate`, which
folds its own local window purely for rendering because a heatmap needs the
full base-pair probability matrix that no accessibility adapter keeps
around. Here the object needed for rendering is the one already kept around.
"""

from __future__ import annotations

import numpy as np

from ..core import thermo
from .mpl import figure_to_data_uri, plt, require

#: Candidate highlight colour, matching viz.generate's CANDIDATE_COLOR.
HIGHLIGHT_COLOR = "#d9622b"


def _dg_per_nt(p: float | None, length: int, temperature_c: float) -> float:
    if p is None or p <= 0.0 or length <= 0:
        return float("nan")
    return thermo.dg_open_from_probability(p, temperature_c) / length


def render_accessibility_profile(
    table: dict[int, list[float | None]],
    sequence_length: int,
    window: int,
    temperature_c: float,
    highlights: tuple[tuple[int, int, str], ...] = (),
) -> str:
    """Line plot of dG_open/nt at one fixed window length, every position.

    This is a per-base-*resolution* track, not a per-base marginal: every
    point is still the joint probability that the whole ``window``-nt
    interval starting there is unpaired, just evaluated at every start
    position rather than only the ones a coarser ``--step`` tiled.

    ``highlights`` marks candidate spans as ``(start, end, label)``; the
    shortlisted candidates the report ranks, so the profile and the ranking
    can be read side by side rather than as two disconnected numbers.
    """
    require()
    starts = list(range(1, sequence_length - window + 2))
    values = []
    for start in starts:
        end = start + window - 1
        row = table.get(end)
        p = row[window] if row is not None and window < len(row) else None
        values.append(_dg_per_nt(p, window, temperature_c))

    width = max(6.0, min(16.0, sequence_length / 45))
    fig, ax = plt.subplots(figsize=(width, 3.2))
    ax.plot(starts, values, color="#20303f", lw=1.0)

    for start, end, label in highlights:
        ax.axvspan(start, end, color=HIGHLIGHT_COLOR, alpha=0.18, lw=0)

    ax.set_xlabel("Start position (nt)")
    ax.set_ylabel("dG_open / nt (kcal/mol/nt)")
    ax.set_title(
        f"Accessibility profile — every {window} nt window, step 1 nt",
        fontsize=10,
    )
    ax.set_xlim(1, sequence_length)
    finite = [v for v in values if v == v]                # drop NaN
    if finite:
        ax.set_ylim(0, max(finite) * 1.08)
    fig.tight_layout()
    return figure_to_data_uri(fig)


def render_accessibility_landscape(
    table: dict[int, list[float | None]],
    sequence_length: int,
    max_length: int,
    temperature_c: float,
) -> str:
    """Heatmap of dG_open/nt over every (start position, window length).

    A vertical streak means a site is cheap to open across many lengths — a
    broad, robust element, safe to target with a binder of almost any
    footprint. An isolated fleck means the opposite: accessible at one
    specific length only, the case the window-length robustness sweep exists
    to catch (see ``M.WINDOW_LENGTH_SPREAD``). Grey cells are combinations
    RNAplfold's table has no data for (too close to a sequence end for that
    length to fit).
    """
    require()
    grid = np.full((max_length, sequence_length), np.nan)
    for end, row in table.items():
        upper = min(max_length, len(row) - 1)
        for length in range(1, upper + 1):
            p = row[length]
            if p is None:
                continue
            start = end - length + 1
            if start < 1:
                continue
            grid[length - 1, start - 1] = _dg_per_nt(p, length, temperature_c)

    # Plain viridis, not reversed: low dG_open (cheap, available) is dark,
    # high dG_open (expensive, buried) is yellow — the same "dark is open,
    # bright is paired/costly" sense as viz.dotplot's base-pair heatmap,
    # where high pairing probability (bad) is also yellow.
    cmap = plt.get_cmap("viridis").with_extremes(bad="#e2e2e2")

    finite = grid[np.isfinite(grid)]
    vmax = float(np.percentile(finite, 95)) if finite.size else 1.0

    width = max(6.0, min(16.0, sequence_length / 45))
    fig, ax = plt.subplots(figsize=(width, 3.6))
    image = ax.imshow(
        grid, aspect="auto", origin="lower", cmap=cmap, vmin=0.0, vmax=vmax,
        extent=(0.5, sequence_length + 0.5, 0.5, max_length + 0.5),
        interpolation="nearest",
    )
    colorbar = fig.colorbar(image, ax=ax, fraction=0.03, pad=0.02)
    colorbar.set_label("dG_open / nt (kcal/mol/nt)")
    ax.set_xlabel("Start position (nt)")
    ax.set_ylabel("Window length (nt)")
    ax.set_title(
        "Accessibility landscape — darker is cheaper to open at that length",
        fontsize=10,
    )
    fig.tight_layout()
    return figure_to_data_uri(fig)
