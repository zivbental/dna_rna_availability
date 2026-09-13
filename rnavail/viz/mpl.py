"""Shared matplotlib plumbing for the visual report.

Matplotlib is an optional dependency: everything else in rnavail runs without
it, so a missing install should degrade the report (no images) rather than
crash the run. Every caller goes through :func:`available` first.
"""

from __future__ import annotations

import base64
import io

_ERROR = ""
try:
    import matplotlib
    matplotlib.use("Agg")  # headless: no display exists in a CLI/CI context
    import matplotlib.pyplot as plt
    _AVAILABLE = True
except Exception as exc:                             # pragma: no cover
    plt = None                                       # type: ignore
    _AVAILABLE = False
    _ERROR = str(exc)


def available() -> bool:
    return _AVAILABLE


def unavailable_reason() -> str:
    return _ERROR


def require() -> None:
    if not _AVAILABLE:
        raise RuntimeError(
            f"matplotlib is not importable ({_ERROR}); install it with "
            "'pip install matplotlib' to enable --html visual reports"
        )


def figure_to_data_uri(fig, dpi: int = 130) -> str:
    """Render a figure to a base64 PNG data URI and close it.

    Closing here, rather than leaving it to the caller, is what keeps a report
    with dozens of candidates from accumulating open figures and leaking
    memory across a long-running process.
    """
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"
