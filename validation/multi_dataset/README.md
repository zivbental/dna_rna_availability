# Benchmarking RNA structural availability

This runner evaluates the **existing pipeline** on independent experimental
structure-probing datasets. It compares the current candidate ranking, the
same ranking with its seed term removed, the same ranking with its opening-cost
term removed, and mean per-base unpaired probabilities. It also reports the
20-base joint opening probability and best 8-base seed probability separately.
It does not change production weights or fit a new model.

## Run tomorrow

Use a checkout containing `validation/multi_dataset/` and the updated
`pyproject.toml` on your Linux device. A transfer ZIP contains these changes;
unpack it at the repository root of a checkout based on `2c72a16` or compatible
main. The ignored `work/` directory is regenerated there. macOS also works;
on Windows use WSL. From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[benchmark]'
.venv/bin/python validation/multi_dataset/prepare.py --list
```

Both default models use ViennaRNA's Python bindings; separate RNAfold and
RNAplfold executables are unnecessary. Start in a persistent `tmux` session,
or use the detached command below. Four workers are the default; increase
after checking RAM usage. Downloading, disk indexing and preparing experimental
records happen first, without folding.

```bash
mkdir -p validation/multi_dataset/work
nohup env BENCHMARK_WORKERS=4 bash validation/multi_dataset/run_overnight.sh \
  > validation/multi_dataset/work/overnight.log 2>&1 < /dev/null &
```

Monitor with:

```bash
tail -f validation/multi_dataset/work/overnight.log
```

The launcher prepares all seven datasets, then resumes or starts the default
benchmark. Keep these files on a local disk and allow tens of GB of free space:
mouse references, SQLite measurement indexes, canonical records and per-RNA
prediction caches are substantial. Runtime depends on transcript lengths,
hardware and the global folds; this is not guaranteed to finish in one night.

For separate preparation and execution, or to select a subset:

```bash
.venv/bin/python validation/multi_dataset/prepare.py
.venv/bin/python validation/multi_dataset/benchmark.py --dry-run
.venv/bin/python validation/multi_dataset/benchmark.py --workers 4 --resume
```

Repeat `--dataset ID` on either Python command to select datasets. Without it,
preparation selects all seven and benchmarking selects all prepared datasets.
`--dry-run` checks records, checksums, tool availability and counts without
performing any folding. To check a few actual RNAs first, use a separate output
directory:

```bash
.venv/bin/python validation/multi_dataset/benchmark.py \
  --dataset pars_yeast_invitro --limit 2 --workers 1 \
  --output-dir validation/multi_dataset/work/pilot
```

`--limit` selects the first records by deposited/annotation identifier, **not a
representative sample**. It is a technical smoke test, never evidence for a
scientific conclusion. The full command has no record-count limit.

## Defaults and cost

The default prediction protocol is 37°C, Turner parameters, RNAplfold window
200, local pairing span 150, footprint 20, best seed 8, and step 1. All footprint
windows are evaluated; no prediction-based shortlist is used. Each model folds
once per RNA for per-base and regional metrics. Prediction caches are shared
across conditions **only when the RNA sequence and complete prediction protocol
are identical**. PARS and RASP references need not supply identical RNAs.

RNAplfold runs on every eligible sequence. Global models such as RNAfold have
an explicit default `--global-max-length 6000`; longer RNAs still receive local
predictions and ranking comparisons, with global-model exclusions reported.
Global folding has roughly cubic time and quadratic memory costs, so worker
count also sets concurrent memory demand. Set `--global-max-length 0` for
unrestricted global folding, or use `--tools rnaplfold` for a local-only run.
There is no universal runtime or memory guarantee. `--max-length N` instead
excludes entire RNAs and reports that selection.

The default run uses the production score with the metrics supplied by the two
selected models. Its seed and opening-cost terms are available; robustness
terms are absent and handled by the pipeline's existing coverage rules.
**It does not validate uncomputed robustness terms.** Coverage is recorded for
every candidate and summarized per RNA. If you also want the expensive
production robustness sweeps, use a distinct result directory:

```bash
.venv/bin/python validation/multi_dataset/benchmark.py --workers 4 \
  --robustness --length-robustness \
  --output-dir validation/multi_dataset/work/results_with_robustness
```

Those sweeps evaluate many settings and constrained local folds for every
window; they can be much slower. Their actual contexts and protocols are
recorded. Neither run uses probing measurements as folding constraints.

## Experimental inputs

| Dataset ID | Experiment | Reference | Higher score means |
|---|---|---|---|
| `pars_yeast_invitro` | PARS, yeast, in vitro | Deposited GSE22393 RNAs and genome | More paired |
| `dms_yeast_invitro` | DMS-seq, BY4741, in vitro | RASP matched yeast genome/annotation | More available |
| `dms_yeast_invivo` | DMS-seq, BY4741, in vivo | RASP matched yeast genome/annotation | More available |
| `icshape_mouse_invitro` | icSHAPE, mouse ES cells, in vitro | RASP mm10 genome/annotation | More available |
| `icshape_mouse_invivo` | icSHAPE, mouse ES cells, in vivo | RASP mm10 genome/annotation | More available |
| `shape_ecoli_cellfree` | SHAPE-MaP, MG1655, cell free | RASP E. coli genome, version-matched GenBank gene locations | More available |
| `shape_ecoli_incell` | SHAPE-MaP, MG1655, in cells | RASP E. coli genome, version-matched GenBank gene locations | More available |

PARS reuses the four deposited files already included in
`validation/controls_2010/source/`. RNAs must reconstruct exactly from the
deposited contiguous intervals or exon/UTR blocks; ambiguous antisense
measurements are excluded as in the existing comparison.

The other studies use [RASP v2's download service](https://rasp2.zhanglab.net/download/).
The catalog pins study DOI, species, condition and processed track path.
Preparation requires RASP `tracktype=raw`, which means original/non-imputed
data; it does **not** mean unnormalized sequencing counts. Publisher/RASP
processing metadata, downloaded content hashes and timestamps are retained.
No imputed structural scores are used and no extra score normalization is
invented. Updates to remote files require a fresh work directory to retain
both versions.

For genomic tracks, exon intervals are concatenated in RNA orientation, with
reverse complements on the negative strand. One longest exon-annotated
transcript per gene is selected independently of the probing scores; ties use
transcript ID. This avoids counting every annotated isoform as a separate
validation example. For E. coli, RASP's supplied annotation was found to
contain coordinates beyond its `U00096.2` reference length. The runner instead
downloads the deposited [version-specific GenBank record](https://getentry.ddbj.nig.ac.jp/getentry/na/U00096.2?filetype=gb),
checks its full DNA sequence against RASP's reference, and uses its exact gene
locations, including any joined locations. It never repairs a version mismatch
by wrapping out-of-bounds coordinates around the chromosome.
Missing annotations, rejected mappings, isoform selection and lost PARS
antisense measurements have preparation audit files.

**Genomic scores cannot identify which isoform generated a measurement.** The
RASP annotation reconstruction is a reproducible proxy for RNA boundaries,
not a reconstruction of all author-defined full transcripts. In particular,
bacterial annotation units do not reconstruct every polycistronic RNA used in
the original study. Consequently these are study-track validation examples,
not exact re-runs of each paper's complete analysis. In vitro and in-cell
measurements are kept separate, and the fixed folding protocol does not claim
to reproduce each experiment's temperature, salts, protein occupancy or active
cellular processes.

Study sources: [Kertesz 2010](https://doi.org/10.1038/nature09322),
[Rouskin 2014](https://doi.org/10.1038/nature12894),
[Spitale 2015](https://doi.org/10.1038/nature14263), and
[Mustoe 2018](https://doi.org/10.1016/j.cell.2018.02.034).

## What is measured

All experimental comparisons orient scores so that higher means more
structurally available. Thus PARS scores are negated and positive correlation
is the expected direction. DMS comparisons use A/C only; SHAPE uses A/C/G/U.
Measured zeros and negative background-corrected SHAPE values are retained.
Absent entries remain missing. BED intervals are expanded as constant-valued
half-open intervals, with strand preserved; overlapping duplicate measurements
cause an error rather than being overwritten.

Per-base comparisons pair each observed base with its predicted unpaired
probability. A window requires at least four measured assay-observable bases
and 80% coverage **of the assay-observable bases**, including observable bases
whose measurements are missing. Its experimental proxy is the mean oriented
reactivity over those measured positions. Predicted means over all bases and
over just those same measured positions are both reported; the latter is the
fairer comparison for DMS. Best-seed probability is also checked against the
measurements inside its own selected seed, separately from the footprint.

Outputs include Pearson, Spearman and the experimental gain in the top 10%
of ranked windows over all valid windows within the same RNA. Scaled gain is
divided by the within-RNA standard deviation of experimental window means;
it is undefined for constant measurements. Ties at the cutoff are included
fractionally, avoiding dependence on sequence position. At least 20 pairs are
required for a defined correlation or gain by default.

`window:*` uses every valid observation for each feature.
`matched_window:*` compares the three score variants and available per-base
means on **the identical intersection of valid windows**, so missing score
terms cannot silently change their comparison cohorts. The intersection can
exclude windows with censored/unavailable opening costs; both sets of results
are retained. The prediction cache preserves opening observations and censor
reasons. Underflowing opening probabilities are not replaced with invented
experimental labels.

**Probing reactivity is a proxy for per-base structural availability. It does
not measure simultaneous 20-base opening, binding kinetics or target efficacy.**
A result can show whether a feature helps rank experimentally reactive regions;
it cannot directly validate its claimed joint-opening probability. Overlapping
windows and shared energy parameters mean many observations are dependent.
No independence-based p-values are reported. Prefer per-RNA Spearman medians
and matched ranking comparisons over pooled Pearson, which can reflect
between-RNA score scales. RNAfold and RNAplfold share ViennaRNA/Turner physics;
they are complementary calculations, not independent experimental confirmations.

## Reports, interruption and resume

Default outputs are in `validation/multi_dataset/work/results/`:

- `REPORT.md`: separate tables for each study condition, plus failures and exclusions.
- `summary.json`: machine-readable dataset summaries and full source metadata.
- `per_record.tsv`: every RNA/feature, with status, correlations and checkpoint path.
- `records/<hash>/REPORT.md` and `result.json`: one report and checkpoint per RNA.
- `prediction_cache/*.json.gz`: per-base predictions, window metrics, score
  components, opening observations, warnings and applied model protocols.
- `manifest.json`: checksums of inputs, code and parameter files, model versions,
  protocol and analysis settings.

Add `--details` from the beginning to retain per-RNA `windows.tsv.gz` tables.
This increases disk use and is part of the run fingerprint.

Completed predictions and records are written atomically. Re-run the same
launcher or Python command with `--resume` after an interruption. Worker count
can change; data, code, model versions and analysis parameters must match. A
mismatch fails before folding. `--resume --retry-failed` retries failed records
and failed sequence caches; successful records and sequence caches are reused.
For a failed sequence, the selected models are recomputed together so its
updated pipeline score has a consistent derivation. Exit status 1 means at least
one failed/partially failed RNA; an exclusion is reported separately. Other
fatal input/download errors propagate as errors. A lost stdout pipe does not
turn a finished folding prediction into a failed record.

When stopping a native fold, terminate its worker processes as well as its
parent; stopping only the parent can leave native workers running. In `tmux`,
Ctrl-C interrupts the process group, but a native operation may take time to
return. Unfinished work is recomputed on resume, and POSIX cache locks are
released on process termination. Do not run two benchmark parents against the
same result directory at once, or two preparation commands against the same
work directory. A stopped run's summary can be incomplete; resuming rebuilds
it from all record checkpoints.

## Additional datasets

The benchmark accepts canonical JSONL with one RNA per line and **one-based
RNA positions**:

```json
{"id":"construct_1","gene_id":"gene_1","sequence":"ACGUACGU","measurements":{"1":0.0,"2":0.2,"5":0.9}}
```

Missing positions are omitted; sequences are normalized to uppercase RNA.
An optional `sequence_sha256` is checked against SHA-256 of that normalized
RNA string. This differs from the production `Sequence.sha256`, which also
includes molecule type. Other record metadata is retained in checkpoints.
Supply one metadata JSON per assay and experimental condition:

```json
{"id":"my_shape_condition","study":"Study name","assay":"SHAPE-MaP","higher_is":"available","observable_bases":"ACGU","conditions":{"environment":"invitro","temperature_c":25}}
```

```bash
.venv/bin/python validation/multi_dataset/prepare.py \
  --import-jsonl path/to/records.jsonl --metadata path/to/metadata.json
```

Source quality filtering, numerical missing-value sentinels and exact RNA
coordinates must be resolved before canonical import. Keep distinct conditions
in separate datasets. This interface allows later addition of RMDB or other
experiments without changing the predictor; it does not automatically parse
RDAT files or claim independence from any model's training data. If fitting
weights later, split by gene/sequence family and hold out entire studies;
check training-set overlap for learned folding models.

## Validation performed during preparation of this code

Focused tests check DMS coverage, zero/missing/negative measurements, constant
BED intervals, strand and exon projection, circular-origin projection,
fractional ranking ties, PARS score direction, seed-coordinate matching,
checkpoint identity and changed-input rejection. A tiny native fold verifies
that the benchmark score equals the public pipeline's score and that the
sequence cache avoids refolding. Technical preparation was also checked on
the full deposited PARS input, one yeast DMS track and the cell-free E. coli
track, plus a three-RNA parallel smoke run; no full
multi-dataset folding benchmark was run.
