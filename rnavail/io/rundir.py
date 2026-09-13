"""Timestamped run directories.

Every ``evaluate``/``scan`` invocation can be asked to leave a permanent,
self-describing record of itself under ``runs/<timestamp>/`` instead of (or
alongside) an explicit ``--json``/``--tsv`` path. That is what makes it
possible to come back later and compare "what did last Tuesday's scan of this
transcript say" against today's without having remembered to redirect output
somewhere sensible at the time.

Two runs starting in the same second get disambiguated with a numeric suffix
rather than one silently clobbering the other, and ``runs/latest`` is kept
pointing at the most recent one as a convenience symlink.
"""

from __future__ import annotations

import json
import os
import platform
import sys
import time
from pathlib import Path
from typing import Any


def format_duration(seconds: float | int | None) -> str | None:
    """Render a measured wall-clock duration compactly for run artifacts."""
    if seconds is None:
        return None
    total = float(seconds)
    if total < 60:
        return f"{total:.3f} s"
    minutes, remaining = divmod(total, 60)
    if minutes < 60:
        return f"{int(minutes)} min {remaining:.1f} s"
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)} h {int(minutes)} min {remaining:.1f} s"


def timestamp(now: float | None = None) -> str:
    """A filesystem-safe, sortable timestamp, to the second, in local time."""
    return time.strftime("%Y%m%d-%H%M%S", time.localtime(now))


def make_run_dir(base: str | Path = "runs", tag: str | None = None) -> Path:
    """Create ``<base>/<timestamp>[-tag]/`` and return it.

    Collisions (two runs launched in the same second) get ``-2``, ``-3``, ...
    appended rather than overwriting the earlier run.
    """
    base = Path(base)
    base.mkdir(parents=True, exist_ok=True)
    stem = timestamp()
    if tag:
        stem = f"{stem}-{_slug(tag)}"

    candidate = base / stem
    suffix = 2
    while True:
        try:
            candidate.mkdir(parents=True, exist_ok=False)
            break
        except FileExistsError:
            candidate = base / f"{stem}-{suffix}"
            suffix += 1

    _update_latest_link(base, candidate)
    return candidate


def _slug(text: str) -> str:
    cleaned = "".join(c if c.isalnum() or c in "-_." else "-" for c in text)
    return cleaned.strip("-")[:40] or "run"


def _update_latest_link(base: Path, target: Path) -> None:
    """Best-effort ``runs/latest`` symlink to the most recent run.

    Purely a convenience; a filesystem that cannot make symlinks (or a stray
    non-symlink file already named ``latest``) should not break the run
    itself, so failure here is swallowed.
    """
    link = base / "latest"
    try:
        if link.is_symlink():
            link.unlink()
        elif link.exists():
            return  # something else owns this name; leave it alone
        link.symlink_to(target.name)
    except OSError:
        pass


def write_meta(run_dir: Path, fields: dict[str, Any]) -> Path:
    """Record what produced this run: command, inputs, protocol, outcome."""
    meta = {
        "command": sys.argv,
        "invoked_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "cwd": os.getcwd(),
        **fields,
    }
    meta.setdefault("duration_human", format_duration(meta.get("duration_s")))
    path = run_dir / "meta.json"
    path.write_text(json.dumps(meta, indent=2, default=str))
    return path
