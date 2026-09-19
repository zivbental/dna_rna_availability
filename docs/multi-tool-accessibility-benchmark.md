# Multi-tool RNA accessibility benchmark

## Status and scope

This document defines the next RNA-availability benchmark for `sackler616` (Lab PC). It asks which **sequence-only** predictor is most associated with the seven existing DMS, icSHAPE, PARS, and SHAPE datasets. It does not assume that RNAplfold has universally failed: the current run is partial, and agreement varies by assay, dataset, condition, and metric.

The benchmark will compare models on identical experimental observations. It will not use any benchmark probing value as predictor input, tune a model or threshold against the test outcomes, pool incompatible assay scales, or reinterpret model unpairedness as a calibrated probability of chemical reactivity or binder access.

## Isolation from the active run

The current benchmark remains authoritative and read-only:

- checkout: `/home/zivbental/workspace/projects/rna/dna_rna_availability-multi-dataset`;
- branch/commit: `feat/multi-dataset-rna-benchmark` at `46b9d1d63060dcfe7fd8916e1cd9a785ec8b23ce`;
- active output: `validation/multi_dataset/work/results_parallel`;
- active manifest fingerprint: `5daa1d4acdf4bc6f6a174b790a2ba8d7b8ea1165e4fb85efdb2b8aa31b8254c3`;
- active tool settings: ViennaRNA 2.7.2, 37 °C, RNAplfold `W=200`, `L=150`, 20-nt footprint, 8-nt seed, step 1, and a 6,000-nt global-model limit.

The future worktree has been created at:

```text
/home/zivbental/workspace/projects/rna/dna_rna_availability-multi-tool-benchmark
```

on branch `ziv/multi-tool-accessibility-benchmark`, initially at the same commit. Heavy installation, runtime testing, cache import, and prediction must wait until the current 12-worker run finishes and the host passes the idle-resource gate below. The current output directory must never be reused or modified.

Before implementation, preserve the exact untracked active runner `validation/multi_dataset/benchmark_parallel.py`, whose active-manifest SHA-256 is `69cc4410e18383e65f642f6e830671f3cea0a8ef0bfb8ff2b1feba28e9da832f`, together with the final manifest, dirty status, prepared-input hashes, tool versions, and final record/cache counts.

## Candidate panel

### Existing baselines

- **RNAplfold 2.7.2:** local Vienna/Turner marginal unpairedness.
- **RNAfold 2.7.2:** global Vienna/Turner marginal unpairedness.
- **Current pipeline and ablations:** comparison baselines only. They are not independent tools because the score contains RNAplfold-derived components.

### New Phase-0 candidates

1. **RNAstructure partition 6.6** — an exact global, pseudoknot-free thermodynamic ensemble implemented independently of ViennaRNA. `partition` produces a partition save file and `ProbabilityPlot` exposes base-pair probabilities.[1][2] Compute `q_i = 1 - Σ_j p_ij`. Pin the isolated-pair policy and use no SHAPE, constraints, or experimental bonuses.
2. **CONTRAfold 2.02** — an exact conditional log-linear structure ensemble trained on known structures rather than Turner free energies.[3] Parse complete posterior pair probabilities and compute `q_i = 1 - Σ_j p_ij`.
3. **LinearPartition-C** — beam-pruned, left-to-right partition inference with CONTRAfold-family parameters. The implementation emits base-pair probabilities, supports a fixed beam size, and is designed for practical linear-time scaling.[4][5] Pin commit `b450fb3e63189073b68d385589035f992080aa3a`, beam 100, and output cutoff 0.0.
4. **EternaFold 1.3.1** — a CONTRAfold-family model trained by multitask learning that included high-throughput probing and binding data.[6][7] Use `EternaFoldParams.v1`, no evidence input, and complete posterior output. It can enter the confirmatory ranking only after exact-sequence and homology-overlap auditing.
5. **LinearCapR 1.0.4** — an exploratory scalable structural-context ensemble. Its primary score is fixed prospectively as `q_i = 1 - P(Stem_i)`; loop-context combinations will not be selected after seeing outcomes.
6. **MXfold2 0.1.2 pilot** — a learned structure model with thermodynamic regularization and published source/model distributions.[8][9] It is eligible only if a numerical pilot demonstrates that its base-pair output is a coherent probability matrix within a predeclared tolerance.

### Controls and deferred tools

- **LinearPartition-V** is an approximation/inference control for Vienna-family parameters, not an independent model.
- **CROSS** is a direct structural-propensity predictor, but its assay-specific models were trained on yeast PARS and mouse icSHAPE—the same assay/organism combinations represented here.[10][11] It may be shown only as a training-contaminated diagnostic unless an overlap-excluded evaluation can be established.
- **ShaKer** is a direct SHAPE-like predictor, but checkpoint, licensing, training-overlap, and runtime questions must be resolved before inclusion.[12][13]
- CapR, NUPACK, RNAsoft/SimFold, SPOT-RNA, UFold, RNA-FM, RiNALMo, and RNAsnap2 remain secondary candidates. They are excluded from the first headline ranking when their output is not a normalized ensemble probability, their endpoint differs from unpairedness, their licensing or deployment is not reproducible, or their compute/length limits prevent the shared cohort.
- SPOT-RNA2 is excluded from the primary sequence-only panel because inference performs homology/database searches.

## One common scientific estimand

Every core predictor must produce a full-length array:

```text
per_base_unpaired[i] ∈ [0, 1] or null with an explicit reason
```

For normalized base-pair posterior matrices, use `q_i = 1 - Σ_j p_ij`. For structural-context models, use `q_i = 1 - P(Stem_i)`. Any omitted probability threshold must be zero or its omitted mass must be accounted for; silently dropping low-probability pairs biases unpairedness upward.

For each existing eligible 20-nt window, the primary prediction is the arithmetic mean of `q_i` at the **exact experimentally measured assay-observable positions**. DMS remains A/C-only. icSHAPE, SHAPE, and PARS use all bases. Existing direction normalization, minimum four measured bases, and 80% observable-base coverage remain frozen. The full-window mean, seed probability, joint 20-nt opening probability, MFE binary state, solvent accessibility, and contact confidence are separate estimands and cannot substitute for this primary score.

## Predictor contract and cache

Introduce versioned `PredictorSpec` and `PredictorResult` records. The spec records predictor ID, model family, adapter, executable/container digest, exact version, source, license, model/parameter SHA-256, frozen options, alphabet, output semantics, length limit, timeout, thread count, determinism, training provenance, and overlap status.

Each invocation receives only normalized RNA sequence, sequence SHA-256, predictor configuration, and resource limits—never dataset identity or probing measurements. A result records status, full-length values, null reasons, exact command/profile, stdout/stderr digests, elapsed time, CPU time, peak RSS, warnings, and provenance.

Use independent per-predictor immutable cache entries:

```text
<output>/predictors/<predictor_id>/cache/<prefix>/<key>.json.gz
```

where `key` hashes the interface schema, sequence SHA-256, predictor ID, executable/container digest, model/parameter digest, version, and frozen options. Validate the key, sequence, length, value range, payload checksum, and provenance on every read. Write atomically under a per-key lock. Dataset and experimental values are intentionally absent so identical sequences share predictions across conditions.

A read-only importer may extract validated RNAplfold/RNAfold arrays from the completed legacy cache. It must preserve source provenance and must not mutate or warm-write the legacy output.

## Fair comparison and winner rule

All headline comparisons are computed separately within each of the seven datasets.

1. Build a tool-independent eligible-window table from the existing prepared records and hashes.
2. A predictor qualifies for the core ranking only if it produces finite primary scores for at least 90% of eligible transcripts **and** windows in every dataset.
3. Build one all-core shared cohort per dataset. Every ranked predictor must have identical transcript, window, measured-position, and experimental-value counts. Persist a cohort fingerprint; any denominator mismatch is an error.
4. Report:
   - pooled window Pearson;
   - median within-transcript Spearman for transcripts with at least 20 shared windows;
   - pooled per-base Pearson and median within-transcript per-base Spearman for true marginal-probability tools;
   - eligible and retained transcript/window/base counts, length exclusions, null positions, failures, timeouts, and coverage;
   - cold/warm wall time, CPU time, peak RSS, nucleotides/second, cache size, and cache-hit rate.
5. Compute paired 95% intervals with 2,000 deterministic transcript-level bootstrap replicates. Add a 200-nt within-transcript block-bootstrap sensitivity analysis because overlapping windows are not independent.
6. Rank tools independently for Pearson and Spearman within each dataset. Across datasets, report average rank, win count, and decisive-win count; never pool raw assay values or observations across technologies, organisms, or conditions.
7. A tool is called best only if the predeclared shared-cohort ranking supports it. If Pearson and Spearman winners differ, the paired winner-minus-runner-up interval includes zero, training-overlap exclusion changes the ordering, or coverage falls below threshold, report that no single robust winner was established.

EternaBench has already shown that learned statistical packages can outperform commonly used thermodynamic packages for some ensemble-oriented tasks, which motivates this comparison but does not predict the winner on these seven datasets.[7] LinearPartition's published speed and structure benchmarks likewise do not establish probing-reactivity performance here.[5]

## Training-overlap audit

Before confirmatory use of any learned model:

- hash normalized evaluation sequences against all available training manifests;
- identify near-global matches at ≥80% identity over ≥80% of the shorter sequence;
- identify local matches at ≥90% identity over ≥50 nt or ≥80% of the training sequence;
- report overlap by dataset and repeat metrics after excluding flagged transcripts;
- mark training provenance as unknown when corpora cannot be recovered.

Unknown or material overlap excludes a learned model from a held-out winner claim. Sequence-only execution is necessary but not sufficient to establish independence from training data.

## Test-first delivery phases

1. **Preservation:** after the active run completes, snapshot its exact code, untracked runner hash, manifest, prepared hashes, tools, and final counts.
2. **Contract tests:** RED-GREEN-REFACTOR tests for specs/results, cache keys, array validation, null handling, corruption rejection, atomic writes, and measurement-blind invocation.
3. **Adapter tests:** golden parsers and real executable smoke tests for every pinned candidate, including complete probability mass, one-based coordinates, ambiguous input, length limits, timeout, and version/parameter capture.
4. **Legacy importer:** verify sampled imported RNAplfold/RNAfold arrays exactly match source entries and leave the source output unchanged.
5. **Eligibility and cohort tests:** cover PARS sign reversal, DMS masking, missing versus zero, coverage, one-based coordinates, shared-cohort equality, whole-transcript failures, and cohort fingerprints.
6. **Metric tests:** hand-calculated Pearson, Spearman, ranks/ties/wins, paired transcript bootstrap, and block bootstrap.
7. **Phase 0 runtime:** on an idle host, run a deterministic length-stratified 18-sequence panel. For each candidate, collect three cold runs in balanced order and one warm-cache run with one process and one tool thread.
8. **Pilot science:** run the Phase-0 panel plus 25 deterministic length-stratified eligible transcripts per dataset. Complete provenance, overlap audit, coordinate inspection, and all metrics before full scale.
9. **Full run:** execute independently resumable predictor shards over unique sequence hashes, freeze the predictor manifest, and compute only missing keys.
10. **Release verification:** rebuild all metrics from immutable caches in a fresh output and require identical cohort fingerprints, metric JSON, and report checksums.

## Resource and feasibility gates

No heavy work starts while the current benchmark is active. The idle gate requires no benchmark workers, load average below 2 for five minutes, at least 10 GiB available RAM, and stable swap use.

Phase 0 uses one predictor process and one thread. A predictor/length stratum is quarantined before outcome correlations are inspected if one invocation exceeds 8 GiB RSS or two hours, or if the safe projected full run exceeds seven days. Production concurrency is computed per predictor from measured p95 RSS while reserving at least 4 GiB RAM and four logical CPUs. Memory-heavy global predictors run in separate waves unless Phase 0 proves co-scheduling safe.

The eventual output root will be separate from the active run, for example:

```text
/home/zivbental/workspace/experiments/rna-accessibility-multitool-v1
```

## Acceptance criteria

- The active checkout, process tree, prepared data, and `results_parallel` remain unmodified.
- Every adapter records exact binary/model/config hashes and passes unit, parser, and real-executable tests.
- Cold and warm scientific outputs are identical apart from timing/cache metadata.
- Existing experimental preparation is reused read-only and its hashes are verified.
- Headline tools meet the 90% coverage threshold and have identical shared-cohort denominators per dataset.
- Every dataset reports Pearson, Spearman, uncertainty intervals, coverage, failures, and resources.
- Cross-dataset summaries use ranks and wins, never pooled assay-scale correlations.
- Learned-model overlap and overlap-excluded sensitivity results are reported.
- Interrupt/resume and worker/input-order invariance are verified.
- Final claims remain limited to association with assay-specific structural-reactivity proxies.

## Sources

[1] https://rna.urmc.rochester.edu/Text/partition.html
[2] https://rna.urmc.rochester.edu/Text/ProbabilityPlot.html
[3] https://ncbi.nlm.nih.gov/pubmed/16873527
[4] https://github.com/LinearFold/LinearPartition
[5] https://doi.org/10.1093/bioinformatics/btaa460
[6] https://github.com/WaymentSteeleLab/EternaFold
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC9839360
[8] https://github.com/mxfold/mxfold2
[9] https://doi.org/10.1038/s41467-021-21194-4
[10] https://doi.org/10.1093/nar/gkw1094
[11] https://tools.tartaglialab.com/static/algorithms/cross/tutorial.html
[12] https://github.com/BackofenLab/ShaKer
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC6612843
