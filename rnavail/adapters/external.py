"""Locating and running external command-line tools.

Search order for a binary:
  1. an explicit override in the ``RNAVAIL_TOOLS_BIN`` environment variable
  2. the project-local micromamba environment created by tools/install_tools.sh
  3. whatever is on ``PATH``

That order means a project-local install always wins over a stale system copy,
which keeps results reproducible between machines.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


class ToolError(RuntimeError):
    """An external tool exited non-zero or produced unusable output."""


def project_root() -> Path:
    """The rnavail checkout root, i.e. two levels above this file."""
    return Path(__file__).resolve().parents[2]


@lru_cache(maxsize=1)
def _search_paths() -> list[Path]:
    paths: list[Path] = []
    override = os.environ.get("RNAVAIL_TOOLS_BIN")
    if override:
        paths.extend(Path(p) for p in override.split(os.pathsep) if p)
    paths.append(project_root() / ".tools" / "env" / "bin")
    return [p for p in paths if p.is_dir()]


@lru_cache(maxsize=256)
def find_binary(name: str) -> str | None:
    """Absolute path to ``name``, or None if it cannot be found."""
    for directory in _search_paths():
        candidate = directory / name
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    return shutil.which(name)


@lru_cache(maxsize=1)
def rnastructure_datapath() -> str | None:
    """RNAstructure refuses to run without DATAPATH pointing at its tables."""
    explicit = os.environ.get("DATAPATH")
    if explicit and Path(explicit).is_dir():
        return explicit
    for directory in _search_paths() + [Path(shutil.which("partition") or "/nonexistent").parent]:
        candidate = directory.parent / "share" / "rnastructure" / "data_tables"
        if candidate.is_dir():
            return str(candidate)
    return None


def tool_environment() -> dict[str, str]:
    """A process environment with DATAPATH filled in when we can find it."""
    env = dict(os.environ)
    datapath = rnastructure_datapath()
    if datapath:
        env["DATAPATH"] = datapath
    return env


@dataclass
class CommandResult:
    args: list[str]
    returncode: int
    stdout: str
    stderr: str


def run_command(
    args: list[str],
    stdin: str | None = None,
    timeout: float = 600.0,
    cwd: str | Path | None = None,
    check: bool = True,
) -> CommandResult:
    """Run an external tool, raising :class:`ToolError` on failure."""
    try:
        proc = subprocess.run(
            args,
            input=stdin,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(cwd) if cwd else None,
            env=tool_environment(),
        )
    except subprocess.TimeoutExpired as exc:
        raise ToolError(
            f"{args[0]} timed out after {timeout:g}s"
        ) from exc
    except OSError as exc:
        raise ToolError(f"could not execute {args[0]}: {exc}") from exc

    result = CommandResult(args, proc.returncode, proc.stdout, proc.stderr)
    if check and proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip().splitlines()
        tail = " | ".join(detail[-3:]) if detail else "no output"
        raise ToolError(f"{Path(args[0]).name} exited {proc.returncode}: {tail}")
    return result


def probe_version(name: str, args: list[str] | None = None) -> str:
    """Best-effort version string for a binary; empty if it will not say."""
    binary = find_binary(name)
    if not binary:
        return ""
    for flags in ([args] if args else [["--version"], ["-V"], ["--help"]]):
        try:
            proc = subprocess.run(
                [binary, *flags], capture_output=True, text=True,
                timeout=20, env=tool_environment(),
            )
        except (OSError, subprocess.TimeoutExpired):
            continue
        text = (proc.stdout or proc.stderr).strip()
        if text:
            first = text.splitlines()[0].strip()
            if first:
                return first[:80]
    return ""
