# Compare every deposited transcript with the paper

`compare_all_genes.py` runs the complete deposited-transcript comparison.
It uses the four GSE22393 gzip files already in `source/`; it does not download data.
The default considers every record in the deposited filtered transcript FASTA,
including noncoding RNAs. This means all available dataset transcripts, rather
than every gene in the yeast genome. Each selected transcript receives a report,
including those with missing annotations, sequence mismatches, insufficient
coverage, ambiguous bases, or failed tools.

From the repository root, when you are ready to run:

```bash
.venv/bin/python validation/controls_2010/compare_all_genes.py
```

The primary comparison is measured PARS versus predicted per-base pairing.
It reports Pearson and tie-aware Spearman correlations for each gene/model,
pooled Pearson, and median per-gene correlations. Undefined correlations remain
null, not zero. No significance tests or independent-observation assumptions are
made. Positive per-base correlations indicate agreement in structural tendency.

The default models are RNAplfold (local, W=200/L=150) and RNAfold (unrestricted
global). Predictions reuse the repository's folding helpers/adapters and preserve
applied protocol and version information. RNAplfold computes its table once per
transcript, using it for per-base probabilities and every covered 20-nt window
with the best 8-nt seed among all 13 placements. There is no prediction-selected
shortlist. Mean PARS/full-site and mean PARS/seed correlations are separate
exploratory diagnostics: PARS is not a measurement of simultaneous opening or
binding. A separate seed diagnostic compares each chosen seed's P with its own
mean measured PARS. Best-seed P refers to one chosen segment, not a union event.

Defaults: 37 °C, Turner 2004/dangles=2 for ViennaRNA; at least 20 matched bases
for a per-gene correlation; at least 80% measured coverage per window/seed;
window step 1; no transcript-length ceiling. Local and global models are reported
separately, not averaged. Full-transcript partition functions can take substantial
time and memory on long RNAs. The script runs sequentially and checkpoints each
transcript, so it can resume without repeating completed genes. On Linux,
`--workers 4` processes independent transcripts in four isolated processes,
sharing immutable input arrays. Worker count does not change prediction settings
and can be changed when resuming. Execution worker count is recorded in the
initial run manifest; the default remains one worker.

For all four models used in the earlier per-base benchmark, plus RNAplfold:

```bash
.venv/bin/python validation/controls_2010/compare_all_genes.py \
  --tools rnaplfold,rnafold,rnastructure-partition,contrafold,eternafold \
  --output-dir validation/controls_2010/all_models_comparison
```

Other configurations:

```bash
# Resume the exact same configuration, data, code and tool versions.
.venv/bin/python validation/controls_2010/compare_all_genes.py --resume

# Local-only comparison; optional compressed per-base/per-window detail files.
.venv/bin/python validation/controls_2010/compare_all_genes.py \
  --tools rnaplfold --details \
  --output-dir validation/controls_2010/local_comparison

# Match the prior demos' whole-transcript local window/span (more expensive).
.venv/bin/python validation/controls_2010/compare_all_genes.py \
  --local-scope full --output-dir validation/controls_2010/full_scope_comparison

# Optional small selection when you choose to test the script later.
.venv/bin/python validation/controls_2010/compare_all_genes.py \
  --gene YLR110C --gene YDL184C \
  --output-dir validation/controls_2010/two_gene_comparison
```

`--max-length` explicitly skips long transcripts; it is absent by default.
`--retry-failed --resume` recomputes checkpoints containing failed models.
Unavailable tools are reported rather than silently omitted. Resume requires the
same settings, source hashes, code hash and reported tool versions. Existing
output directories are refused unless resuming, so earlier results are preserved.

Inputs are checked against the matching genome using one-based inclusive
coordinates and reverse complementation for negative-strand transcripts. Processed
PARS scores are mapped directly without applying an extra cleavage-site shift.
Missing WIG entries stay absent. By default, measurements overlapping an opposite
strand annotated transcript are excluded because the WIG has no strand labels.
`--keep-antisense-overlaps` retains them, with ambiguity counts recorded.
Raw cleavage-depth uncertainty and the paper's average-coverage selection cannot
be reconstructed from the WIG alone. Exact genome reconstruction is required:
if the contiguous interval differs, the supplied exon and UTR blocks must reproduce
the deposited mature/processed RNA exactly. Removed genomic segments receive no
RNA positions. The script never infers exon boundaries by alignment, and records
whether a contiguous or annotated-block projection was used.

Outputs:

- `REPORT.md`: aggregate interpretation and comparison statistics.
- `per_gene.tsv`: one row per gene/model, with status, coverage, correlations and individual report path.
- `summary.json`: statistics, selected/deposited counts and gene status counts.
- `manifest.json`: settings, source SHA256 hashes and prediction-tool versions.
- `genes/<ID hash>/REPORT.md` and `result.json`: individual report and atomic checkpoint.
- With `--details`, compressed per-base prediction tables and local-window/seed tables.

The run uses unconditioned predictions. It does not feed PARS back into folding,
produce a calibrated availability classifier, or compute oligo binding. It compares
the paper's deposited signals rather than digitizing traditional footprinting gels.

Dataset: [GSE22393](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE22393).
