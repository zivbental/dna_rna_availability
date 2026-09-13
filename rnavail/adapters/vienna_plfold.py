"""RNAplfold: local unpaired probabilities over a sliding window.

The workhorse of the first screening stage. RNAplfold folds inside a bounded
window and tabulates the probability that every stretch of up to ``-u``
consecutive nucleotides is unpaired, in O(n*L^2) time. That is what makes
scanning an entire transcript feasible.

Two backends are provided and give the same numbers: the Python bindings
(default, no subprocess overhead) and the RNAplfold command line, which is
useful as an integration-parity check that our binding usage is right.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

from ..core.model import ModelSettings
from ..core.result import Availability, M, Tier, ToolResult
from ..core.sequence import Region
from ..core import thermo
from . import _vienna as V
from .base import AccessibilityAdapter, AccessibilityRequest
from .external import ToolError, find_binary, probe_version, run_command
from .registry import register


@register
class RNAplfoldAdapter(AccessibilityAdapter):
    name = "rnaplfold"
    tier = Tier.ACCESSIBILITY
    cost = 1
    description = (
        "Local sliding-window unpaired probabilities (RNAplfold); the default "
        "engine for transcriptome-scale candidate screening"
    )
    #: Shared with rnaplfold-cli: same algorithm, run through the Python
    #: bindings here and the standalone binary there. The consensus counts
    #: this pair as one measurement, not two — see rnaplfold-cli's docstring.
    independence_group = "vienna-rnaplfold"
    probing_methods = frozenset({"deigan", "zarringhalam", "eddy2"})
    model_family = "vienna-turner"
    algorithm = "RNAplfold-window-pf"
    applied_setting_names = frozenset({
        "temperature_c", "param_set", "dangles", "no_lonely_pairs",
        "no_gu", "no_gu_closure", "salt_molar", "max_bp_span",
        "window_size", "max_unpaired", "circular",
    })
    ignored_setting_names = frozenset({"global_max_bp_span"})
    provides = (
        M.P_UNPAIRED, M.DG_OPEN, M.DG_OPEN_PER_NT,
        M.SEED_P_UNPAIRED, M.SEED_DG_OPEN, M.SEED_START, M.SEED_LENGTH,
        M.MEAN_BASE_UNPAIRED, M.MIN_BASE_UNPAIRED,
    )

    def availability(self) -> Availability:
        return V.availability()

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        temperature = settings.temperature_c

        longest = max((len(r) for r in request.regions), default=1)
        max_unpaired = max(longest, request.seed_length, settings.max_unpaired)
        if max_unpaired > settings.window_size:
            result.warn(
                f"longest region ({longest} nt) exceeds the folding window "
                f"({settings.window_size} nt); widen --window for this target"
            )
            max_unpaired = min(max_unpaired, settings.window_size)

        table = V.local_unpaired_matrix(
            request.sequence.seq, settings, max_unpaired, probing=request.probing
        )
        result.detail["max_unpaired"] = max_unpaired
        result.applied_protocol.setdefault("applied", {})["max_unpaired"] = max_unpaired

        # Per-base unpaired probabilities fall out of the u=1 column.
        singles = {
            j: row[1]
            for j, row in table.items()
            if len(row) > 1 and row[1] is not None
        }

        for region in request.regions:
            metrics = result.region_metrics(region)
            joint = V.region_probability_from_table(table, region)
            if joint is None:
                result.warn(
                    f"region {region.label} ({len(region)} nt) is longer than "
                    f"the tabulated maximum unpaired stretch ({max_unpaired} nt)"
                )
            else:
                metrics.set(M.P_UNPAIRED, joint)
                dg_open = thermo.dg_open_from_probability(joint, temperature)
                metrics.set(M.DG_OPEN, dg_open)
                metrics.set(
                    M.DG_OPEN_PER_NT,
                    thermo.dg_open_per_nucleotide(dg_open, len(region)),
                )

            per_base = [singles[j] for j in region.positions() if j in singles]
            if per_base:
                # Reported for diagnosis only. The mean of per-base
                # probabilities is systematically far more optimistic than the
                # joint probability and must never be used in its place.
                metrics.set(M.MEAN_BASE_UNPAIRED, sum(per_base) / len(per_base))
                metrics.set(M.MIN_BASE_UNPAIRED, min(per_base))

            allowed_starts = request.seed_starts(region)
            seed = V.best_seed(
                table, region, request.seed_length,
                starts=allowed_starts,
            )
            seed_trials = _seed_trials(
                table, region, request.seed_length,
                allowed_starts, temperature,
            )
            metrics.detail["seed_trials"] = seed_trials
            if seed is not None:
                seed_start, seed_p = seed
                metrics.set(M.SEED_START, seed_start)
                metrics.set(M.SEED_LENGTH, request.seed_length)
                metrics.set(M.SEED_P_UNPAIRED, seed_p)
                metrics.set(
                    M.SEED_DG_OPEN,
                    thermo.dg_open_from_probability(seed_p, temperature),
                )
                metrics.detail["seed_selection_note"] = (
                    "best permitted placement selected from the listed trials"
                )
        return result


@register
class RNAplfoldCLIAdapter(AccessibilityAdapter):
    """The stock RNAplfold binary: a check that we drive the bindings

    correctly, not a second, statistically independent estimate of
    accessibility — it is the same windowed local-partition-function
    algorithm as ``rnaplfold``, expected (and tested) to agree with it to
    0.01 kcal/mol. ``independence_group`` tells the consensus layer to treat
    the pair as one vote, so neither this adapter's agreement with
    ``rnaplfold`` nor its disagreement with an unrelated tool like
    ``vienna-exact`` gets double-counted in a median.
    """

    name = "rnaplfold-cli"
    tier = Tier.ACCESSIBILITY
    cost = 2
    description = "RNAplfold command-line binary (cross-check of the bindings)"
    independence_group = "vienna-rnaplfold"
    probing_methods = frozenset({"deigan", "zarringhalam"})
    model_family = "vienna-turner"
    algorithm = "RNAplfold-window-pf"
    applied_setting_names = frozenset({
        "temperature_c", "dangles", "no_lonely_pairs", "no_gu",
        "no_gu_closure", "max_bp_span", "window_size", "max_unpaired",
    })
    ignored_setting_names = frozenset({"global_max_bp_span"})
    provides = (
        M.P_UNPAIRED, M.DG_OPEN, M.DG_OPEN_PER_NT,
        M.SEED_P_UNPAIRED, M.SEED_DG_OPEN, M.SEED_START, M.SEED_LENGTH,
    )

    def availability(self) -> Availability:
        if not find_binary("RNAplfold"):
            return Availability.no(
                "RNAplfold binary not found",
                hint="run tools/install_tools.sh",
            )
        return Availability.yes(probe_version("RNAplfold", ["--version"]))

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        binary = find_binary("RNAplfold")

        if settings.gquad:
            raise ValueError(
                "RNAplfold does not support G-quadruplex-aware local "
                "accessibility; disable --gquad for this adapter"
            )
        if (
            request.probing is not None
            and request.probing.chemistry.upper().startswith("DMS")
            and not request.probing.conversion_explicit
        ):
            raise ValueError(
                "DMS data need an explicitly selected conversion; do not apply "
                "a SHAPE pseudoenergy model by default"
            )

        longest = max((len(r) for r in request.regions), default=1)
        max_unpaired = min(max(longest, request.seed_length), settings.window_size)

        args = [
            binary,
            "-W", str(settings.window_size),
            "-L", str(settings.max_bp_span),
            "-u", str(max_unpaired),
            "-T", str(settings.temperature_c),
            "-d", str(settings.dangles),
        ]
        if settings.no_lonely_pairs:
            args.append("--noLP")
        if settings.no_gu:
            args.append("--noGU")
        if settings.no_gu_closure:
            args.append("--noClosingGU")

        # RNAplfold writes <name>_lunp and <name>_dp.ps into the working
        # directory, so give it a scratch directory of its own rather than
        # scattering files across the project.
        with tempfile.TemporaryDirectory(prefix="rnavail-plfold-") as workdir:
            name = "target"
            if request.probing is not None:
                shape_file = Path(workdir) / "reactivities.shape"
                shape_file.write_text(_write_shape(request))
                args += ["--shape", str(shape_file),
                         "--shapeMethod", _shape_method_flag(request)]
                result.detail["probing_method"] = request.probing.method
            fasta = f">{name}\n{request.sequence.seq}\n"
            run_command(args, stdin=fasta, cwd=workdir)
            lunp = Path(workdir) / f"{name}_lunp"
            if not lunp.is_file():
                raise ToolError(f"RNAplfold produced no {name}_lunp file")
            table = _parse_lunp(lunp.read_text())

        result.detail["max_unpaired"] = max_unpaired
        result.applied_protocol.setdefault("applied", {})["max_unpaired"] = max_unpaired
        for region in request.regions:
            metrics = result.region_metrics(region)
            row = table.get(region.end)
            if row and len(region) < len(row):
                joint = row[len(region)]
                if joint is not None:
                    metrics.set(M.P_UNPAIRED, joint)
                    dg_open = thermo.dg_open_from_probability(
                        joint, settings.temperature_c
                    )
                    metrics.set(M.DG_OPEN, dg_open)
                    metrics.set(
                        M.DG_OPEN_PER_NT,
                        thermo.dg_open_per_nucleotide(dg_open, len(region)),
                    )

            allowed_starts = request.seed_starts(region)
            seed = V.best_seed(
                table, region, request.seed_length,
                starts=allowed_starts,
            )
            seed_trials = _seed_trials(
                table, region, request.seed_length,
                allowed_starts, settings.temperature_c,
            )
            metrics.detail["seed_trials"] = seed_trials
            if seed is not None:
                seed_start, seed_p = seed
                metrics.set(M.SEED_START, seed_start)
                metrics.set(M.SEED_LENGTH, request.seed_length)
                metrics.set(M.SEED_P_UNPAIRED, seed_p)
                metrics.set(
                    M.SEED_DG_OPEN,
                    thermo.dg_open_from_probability(seed_p, settings.temperature_c),
                )
                metrics.detail["seed_selection_note"] = (
                    "best permitted placement selected from the listed trials"
                )
        return result


def _seed_trials(
    table: dict[int, list[float | None]],
    region: Region,
    seed_length: int,
    starts: list[int],
    temperature_c: float,
) -> list[dict[str, object]]:
    """Describe every permitted seed placement in a local-probability table.

    The selected seed metric is useful for ranking, but it hides all other
    permitted nucleation placements.  Keep those raw trials next to the
    region so downstream reports can distinguish a genuinely broad exposed
    site from one chosen because of a single favorable offset.  A zero in an
    RNAplfold table may be an output floor, so it is explicitly censored
    rather than converted to an infinite point-energy estimate.
    """
    trials: list[dict[str, object]] = []
    for start in starts:
        seed = Region(start, start + seed_length - 1)
        probability = V.region_probability_from_table(table, seed)
        trial: dict[str, object] = {
            "start": start,
            "end": seed.end,
            "p_unpaired": probability,
            "dg_open_kcal_mol": None,
            "estimate_kind": "unavailable",
        }
        if probability is None:
            trial["reason"] = (
                "RNAplfold did not tabulate this permitted seed placement"
            )
        elif probability == 0.0:
            trial["estimate_kind"] = "censored"
            trial["censor_reason"] = (
                "RNAplfold reported zero probability; this can represent "
                "a numerical floor or underflow"
            )
        else:
            trial["dg_open_kcal_mol"] = thermo.dg_open_from_probability(
                probability, temperature_c
            )
            trial["estimate_kind"] = "point"
        trials.append(trial)
    return trials


def _parse_lunp(text: str) -> dict[int, list[float | None]]:
    """Parse RNAplfold's ``_lunp`` table into ``{end_position: [None, p1, ...]}``."""
    table: dict[int, list[float | None]] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        try:
            end = int(fields[0])
        except ValueError:
            continue
        row: list[float | None] = [None]
        for field in fields[1:]:
            if field == "NA":
                row.append(None)
            else:
                try:
                    row.append(float(field))
                except ValueError:
                    row.append(None)
        table[end] = row
    return table


def _write_shape(request: AccessibilityRequest) -> str:
    """Render probing data in ViennaRNA's two-column SHAPE file format."""
    lines = []
    sequence = request.sequence.seq
    for index, value in enumerate(request.probing.reactivities, start=1):
        lines.append(f"{index}\t{sequence[index - 1]}\t"
                     f"{-999.0 if value is None else value}")
    return "\n".join(lines) + "\n"


def _shape_method_flag(request: AccessibilityRequest) -> str:
    """Translate our probing method name into RNAplfold's --shapeMethod code."""
    probing = request.probing
    if probing.method == "deigan":
        return f"Dm{probing.slope}b{probing.intercept}"
    if probing.method == "zarringhalam":
        return f"Zb{probing.beta}"
    raise ValueError(
        "the RNAplfold command-line adapter cannot apply Eddy probing "
        "constraints; use the Python rnaplfold adapter"
    )
