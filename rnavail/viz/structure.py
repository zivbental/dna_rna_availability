"""2D secondary-structure diagrams.

Coordinates come from ViennaRNA's own naview layout engine, the same one
behind RNAplot, so the drawing is not a bespoke approximation of how the
molecule folds — it is the standard RNA-visualisation layout, restyled here as
a matplotlib figure so it can sit inline in the HTML report.
"""

from __future__ import annotations

from dataclasses import dataclass

from .mpl import figure_to_data_uri, plt, require

try:
    import RNA
except Exception:                                    # pragma: no cover
    RNA = None                                       # type: ignore

#: Above this length, per-nucleotide letters and position ticks are dropped
#: because they would overlap into an unreadable smear.
MAX_LABELLED_LENGTH = 170


@dataclass(frozen=True)
class Highlight:
    """A 1-based inclusive nucleotide range to colour and label."""

    start: int
    end: int
    color: str
    label: str


def render_structure(
    sequence: str,
    structure: str,
    title: str,
    highlights: tuple[Highlight, ...] = (),
    default_color: str = "#b0b0b0",
) -> str:
    """Render one secondary structure with optional coloured regions."""
    require()
    if RNA is None:
        raise RuntimeError("ViennaRNA python bindings are required for structure plots")
    length = len(sequence)
    if len(structure) != length:
        raise ValueError(
            f"structure length {len(structure)} does not match sequence "
            f"length {length}"
        )

    coords = RNA.get_xy_coordinates(structure)
    xs = [coords.get(i).X for i in range(length)]
    ys = [coords.get(i).Y for i in range(length)]
    pair_table = RNA.ptable(structure)  # 1-based; pair_table[i] = partner or 0

    colors = [default_color] * length
    for region in highlights:
        for i in range(region.start - 1, min(region.end, length)):
            colors[i] = region.color

    size = max(4.0, min(11.0, 3.0 + length / 40))
    fig, ax = plt.subplots(figsize=(size, size))

    ax.plot(xs, ys, "-", color="#c9c9c9", lw=1.0, zorder=1)

    for i in range(1, length + 1):
        j = pair_table[i]
        if j > i:
            ax.plot(
                [xs[i - 1], xs[j - 1]], [ys[i - 1], ys[j - 1]],
                color="#7a9fc9", lw=1.1, alpha=0.85, zorder=2,
            )

    show_letters = length <= MAX_LABELLED_LENGTH
    marker_size = 220 if show_letters else max(12, 4000 / length)
    ax.scatter(
        xs, ys, s=marker_size, c=colors, edgecolors="white",
        linewidths=0.6 if show_letters else 0.2, zorder=3,
    )

    if show_letters:
        for i, (x, y, base) in enumerate(zip(xs, ys, sequence), start=1):
            ax.annotate(
                base, (x, y), ha="center", va="center", fontsize=7,
                zorder=4, color="#202020",
            )
            if i % 10 == 0 or i == 1:
                ax.annotate(
                    str(i), (x, y), xytext=(6, 6), textcoords="offset points",
                    fontsize=6.5, color="#777777", zorder=4,
                )
    else:
        for i in range(0, length, max(1, length // 20)):
            ax.annotate(
                str(i + 1), (xs[i], ys[i]), xytext=(4, 4),
                textcoords="offset points", fontsize=6, color="#888888",
            )

    if highlights:
        handles = [
            plt.Line2D([0], [0], marker="o", linestyle="", color=h.color,
                      markersize=8, label=h.label)
            for h in _unique_by_label(highlights)
        ]
        ax.legend(
            handles=handles, loc="upper center",
            bbox_to_anchor=(0.5, -0.02), ncol=min(3, len(handles)),
            frameon=False, fontsize=8,
        )

    ax.set_title(title, fontsize=10)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    return figure_to_data_uri(fig)


def _unique_by_label(highlights: tuple[Highlight, ...]) -> list[Highlight]:
    seen: dict[str, Highlight] = {}
    for h in highlights:
        seen.setdefault(h.label, h)
    return list(seen.values())
