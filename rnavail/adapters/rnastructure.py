"""RNAstructure: an independent thermodynamic implementation.

Everything else in the accessibility tier is ViennaRNA underneath, so its
tools agree with each other partly by construction. RNAstructure is a separate
codebase with its own parameter tables and its own recursions, which makes it
the most informative cross-check available: where RNAstructure and ViennaRNA
disagree about a site, that site is genuinely model-dependent and should not
be trusted on either tool's word alone.

Wraps ``partition`` + ``ProbabilityPlot``: base-pair probabilities, reduced
here to per-nucleotide unpaired probability and paired fraction.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from ..core.result import Availability, M, Tier, ToolResult
from .base import AccessibilityRequest, Adapter
from .external import find_binary, probe_version, rnastructure_datapath, run_command
from .registry import register


def _rnastructure_available(binaries: list[str]) -> Availability:
    missing = [b for b in binaries if not find_binary(b)]
    if missing:
        return Availability.no(
            f"RNAstructure binaries not found: {', '.join(missing)}",
            hint="run tools/install_tools.sh",
        )
    if not rnastructure_datapath():
        return Availability.no(
            "RNAstructure data tables not found",
            hint="set DATAPATH to the RNAstructure data_tables directory",
        )
    return Availability.yes(probe_version(binaries[0], ["--version"]))


@register
class RNAstructurePartitionAdapter(Adapter):
    name = "rnastructure-partition"
    tier = Tier.STRUCTURE
    cost = 3
    handles_accessibility = True
    orthogonal = True
    #: Shares RNAstructure's partition function and parameter tables with
    #: probknot, which builds its pairing on the same calculation.
    independence_group = "rnastructure"
    model_family = "rnastructure"
    algorithm = "partition-probability-plot"
    applied_setting_names = frozenset({"temperature_c", "global_max_bp_span"})
    ignored_setting_names = frozenset({
        "max_bp_span", "window_size", "max_unpaired",
    })
    description = (
        "RNAstructure partition function: independent base-pair probabilities "
        "as a cross-check on the ViennaRNA energy model"
    )
    provides = (M.MEAN_BASE_UNPAIRED, M.MIN_BASE_UNPAIRED, M.PAIRED_FRACTION)

    def availability(self) -> Availability:
        return _rnastructure_available(["partition", "ProbabilityPlot"])

    def compute_accessibility(self, request: AccessibilityRequest) -> ToolResult:
        result = self.new_result(request.settings)
        settings = request.settings.for_molecule(request.sequence.molecule)
        sequence = request.sequence
        if settings.is_dna:
            # RNAstructure does not select the ViennaRNA parameter-set name,
            # but the request does select its distinct DNA calculation mode.
            result.applied_protocol["unsupported"].pop("param_set", None)
            result.applied_protocol["applied"]["param_set"] = (
                "RNAstructure DNA mode (--DNA)"
            )
            result.applied_protocol["compatible_with_requested"] = not bool(
                result.applied_protocol["unsupported"]
            )

        with tempfile.TemporaryDirectory(prefix="rnavail-rnastructure-") as workdir:
            work = Path(workdir)
            fasta = work / "target.fa"
            fasta.write_text(f">{sequence.name}\n{sequence.seq}\n")
            pfs, table = work / "target.pfs", work / "target.prob"

            args = [find_binary("partition"), str(fasta), str(pfs),
                    "--temperature", str(settings.temperature_c + 273.15)]
            if settings.is_dna:
                args.append("--DNA")
            if settings.global_max_bp_span is not None:
                args += ["--maxdistance", str(settings.global_max_bp_span)]
            run_command(args, timeout=1800)
            run_command(
                [find_binary("ProbabilityPlot"), str(pfs), str(table), "-t"],
                timeout=600,
            )
            paired = _parse_probability_plot(table.read_text(), len(sequence))

        unpaired = [0.0] + [
            max(0.0, min(1.0, 1.0 - paired[i])) for i in range(1, len(sequence) + 1)
        ]
        for region in request.regions:
            metrics = result.region_metrics(region)
            values = [unpaired[i] for i in region.positions()]
            mean = sum(values) / len(values)
            metrics.set(M.MEAN_BASE_UNPAIRED, mean)
            metrics.set(M.MIN_BASE_UNPAIRED, min(values))
            metrics.set(M.PAIRED_FRACTION, 1.0 - mean)
        return result


def _parse_probability_plot(text: str, length: int) -> list[float]:
    """Sum pairing probabilities per nucleotide from a ProbabilityPlot table.

    The file stores -log10(probability) for each pair, and only pairs above
    the tool's reporting cutoff appear, so unlisted pairs contribute nothing.
    """
    paired = [0.0] * (length + 1)
    for line in text.splitlines():
        fields = line.split()
        if len(fields) != 3:
            continue
        try:
            i, j, neg_log10 = int(fields[0]), int(fields[1]), float(fields[2])
        except ValueError:
            continue                       # header lines and the length line
        if not (1 <= i <= length and 1 <= j <= length):
            continue
        probability = 10.0 ** (-neg_log10)
        paired[i] += probability
        paired[j] += probability
    return paired
