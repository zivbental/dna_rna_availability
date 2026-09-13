"""Base-pair probability heatmaps.

The equilibrium base-pair probability matrix is the single richest object a
partition-function calculation produces, and a scalar accessibility number is
a lossy summary of it. Rendering the matrix directly shows *which* competing
structures exist, not just that something competes.
"""

from __future__ import annotations

import numpy as np

from .mpl import figure_to_data_uri, plt, require


def bpp_to_matrix(bpp: list[list[float]], length: int) -> "np.ndarray":
    """Convert ViennaRNA's 1-based, upper-triangular bpp() output to a dense,
    symmetric 0-based matrix suitable for imshow.
    """
    matrix = np.zeros((length, length))
    for i in range(1, length + 1):
        row = bpp[i]
        for j in range(i + 1, min(length, len(row) - 1) + 1):
            p = row[j]
            if p:
                matrix[i - 1, j - 1] = p
                matrix[j - 1, i - 1] = p
    return matrix


def render_bpp_heatmap(
    matrix: "np.ndarray",
    title: str,
    highlight: tuple[int, int] | None = None,
    junction: int | None = None,
) -> str:
    """Render a base-pair probability matrix as a viridis heatmap.

    ``highlight`` marks a 1-based inclusive nucleotide range (typically the
    evaluated candidate region) with light guide lines. ``junction`` marks a
    single 1-based position (the target/partner strand boundary in an ON-state
    dimer) with a dashed crosshair, the way a domain boundary is called out in
    a classic dot-plot.
    """
    require()
    length = matrix.shape[0]
    size = max(3.6, min(9.0, 3.0 + length / 60))
    fig, ax = plt.subplots(figsize=(size, size))

    image = ax.imshow(matrix, cmap="viridis", vmin=0.0, vmax=1.0, origin="upper")
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    colorbar.set_label("Base-pair probability")

    if highlight is not None:
        start, end = highlight
        for axis_line in (ax.axhline, ax.axvline):
            axis_line(start - 1.5, color="white", lw=0.8, alpha=0.6, ls=":")
            axis_line(end - 0.5, color="white", lw=0.8, alpha=0.6, ls=":")

    if junction is not None:
        ax.axhline(junction - 0.5, color="white", lw=1.1, ls="--", alpha=0.85)
        ax.axvline(junction - 0.5, color="white", lw=1.1, ls="--", alpha=0.85)

    ax.set_xlabel("Nucleotide position")
    ax.set_ylabel("Nucleotide position")
    ax.set_title(title, fontsize=10)
    fig.tight_layout()
    return figure_to_data_uri(fig)
