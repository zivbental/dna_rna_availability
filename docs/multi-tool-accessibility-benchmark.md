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

1. **RNAstructure partition 6.6** — an exact global, pseudoknot-free thermodynamic ensemble implemented independently of ViennaRNA. Pin RNA alphabet/data-table hashes, `310.15 K`, coaxial stacking enabled, isolated pairs forbidden (omit `--isolated`), no maximum pair distance, and no SHAPE, constraints, or experimental bonuses. `ProbabilityPlot --text` reports `x_ij = -log10(p_ij)`, not `p_ij`; parse every pair as `p_ij = 10^(-x_ij)`, add that probability to both endpoints, then compute `q_i = 1 - Σ_j p_ij`.[1][2] Use an explicitly untruncated text range and prove on fixtures against RNAstructure's pair-probability API that all nonzero reported mass is retained; otherwise this adapter is ineligible.
2. **CONTRAfold 2.02** — an exact conditional log-linear structure ensemble trained on known structures rather than Turner free energies.[3] Invoke complete posterior output with threshold `0`, not the repository adapter's current `0.001`, parse every pair for both endpoints, and compute `q_i = 1 - Σ_j p_ij`. Any implementation that cannot demonstrate complete posterior mass is ineligible.
3. **LinearPartition-C** — beam-pruned, left-to-right partition inference with CONTRAfold-family parameters. The implementation emits base-pair probabilities, supports a fixed beam size, and is designed for practical linear-time scaling.[4][5] Pin commit `b450fb3e63189073b68d385589035f992080aa3a`, beam 100, and output cutoff 0.0.
4. **EternaFold 1.3.1** — a CONTRAfold-family model trained by multitask learning that included high-throughput probing and binding data.[6][7] Use `EternaFoldParams.v1`, no evidence input, and posterior threshold `0`; do not reuse the current positive-cutoff adapter. It can enter the confirmatory ranking only after complete-mass validation and exact-sequence/homology-overlap auditing.
5. **LinearCapR 1.0.4** — an exploratory scalable structural-context ensemble. Pin Turner 2004 tables, beam 100, and the implementation's fixed unpaired-run cap. Its primary score is fixed prospectively as `q_i = 1 - P(Stem_i)` and is accepted only when all six context probabilities sum to one within `1e-6` at every position; loop-context combinations will not be selected after seeing outcomes.
6. **MXfold2 0.1.2 pilot only** — a learned structure model with thermodynamic regularization and published source/model distributions.[8][9] Its documented float32 base-pair-probability instability prevents confirmatory use unless **every** prediction passes the matrix invariants below.[14] No clipping or renormalization is permitted. A double-precision patch is a different, separately versioned predictor with its own artifact and adapter hashes.

### Controls and deferred tools

- **LinearPartition-C** is an approximate-inference control within the CONTRAfold parameter family; **LinearPartition-V** is the corresponding Vienna-family control; and **LinearCapR** is a Turner-family context-marginal model. They are useful predictors but not independent biological-model votes. Report both predictor-level and model-family-level summaries.
- **CROSS** is a direct structural-propensity predictor, but its assay-specific models were trained on yeast PARS and mouse icSHAPE—the same assay/organism combinations represented here.[10][11] It may be shown only as a training-contaminated diagnostic unless an overlap-excluded evaluation can be established.
- **ShaKer** is a direct SHAPE-like predictor, but checkpoint, licensing, training-overlap, and runtime questions must be resolved before inclusion.[12][13]
- CapR, NUPACK, RNAsoft/SimFold, SPOT-RNA, UFold, RNA-FM, RiNALMo, and RNAsnap2 remain secondary candidates. They are excluded from the first headline ranking when their output is not a normalized ensemble probability, their endpoint differs from unpairedness, their licensing or deployment is not reproducible, or their compute/length limits prevent the shared cohort.
- SPOT-RNA2 is excluded from the primary sequence-only panel because inference performs homology/database searches.

### Frozen confirmatory membership

The only confirmatory candidate IDs are `rnaplfold_vienna_2_7_2`, `rnafold_vienna_2_7_2`, `rnastructure_partition_6_6`, `contrafold_2_02`, `linearpartition_c_b100`, and `eternafold_1_3_1`. LinearCapR, MXfold2, LinearPartition-V, CROSS, ShaKer, the current pipeline, and all other controls remain secondary regardless of their observed performance and never affect the all-core intersection.

After adapter/invariant tests, the Phase-0 resource gate, the complete prediction pass, coverage calculation, and the EternaFold training-overlap audit—but **before evaluation code is allowed to read experimental values**—write and checksum `ranked-predictors.json`. A listed candidate enters that frozen ranked set only if its adapter and complete-mass tests pass, Phase 0 passes, every dataset meets the 90% predictor-coverage gates, and any learned-model audit passes. Failures and fixed reasons are retained as secondary results; no replacement predictor is added. Fewer than four ranked predictors or fewer than two represented model families precludes a robust-overall-winner claim.

Use these immutable sequence-length strata everywhere a stratum is required: `S1=1–250 nt`, `S2=251–500`, `S3=501–1000`, `S4=1001–2000`, `S5=2001–6000`, and `S6≥6001`. Assignment uses full normalized sequence length. Empty dataset/stratum cells are `not_applicable`; a nonempty sparse cell is reported as sparse but still must meet the 70% window-retention gate—there is no merging or post hoc boundary change.

## One common scientific estimand

Every core predictor must produce a full-length array:

```text
per_base_unpaired[i] ∈ [0, 1] or null with an explicit reason
```

For normalized base-pair posterior matrices, use `q_i = 1 - Σ_j p_ij`. Every parsed matrix must be finite, symmetric within absolute tolerance `1e-6`, have diagonal magnitude at most `1e-8`, contain no value below `-1e-8`, have every row sum at most `1 + 1e-6`, and yield `q_i ∈ [0,1]` without clipping or renormalization. A matrix that violates any invariant is a failed prediction, not repairable data. For structural-context models, use `q_i = 1 - P(Stem_i)` only when every context value is finite/nonnegative and the six contexts sum to one within `1e-6`. Any pair-output threshold must be exactly zero unless a validated omitted-mass bound below `1e-6` per nucleotide is recorded; silently dropping low-probability pairs biases unpairedness upward.

Golden tests must compare `q_i` with an independent short-sequence implementation or tool API where available, assert one-based coordinate conversion, and prove each pair contributes to both endpoints exactly once. Exact, beam-pruned, local-window, learned, and Turner-family results remain separately labeled.

For each existing eligible 20-nt window, the primary prediction is the arithmetic mean of `q_i` at the **exact experimentally measured assay-observable positions**. DMS remains A/C-only. icSHAPE, SHAPE, and PARS use all bases. Existing direction normalization, minimum four measured bases, and 80% observable-base coverage remain frozen. The full-window mean, seed probability, joint 20-nt opening probability, MFE binary state, solvent accessibility, and contact confidence are separate estimands and cannot substitute for this primary score.

## Predictor contract and cache

Introduce versioned `PredictorSpec`, immutable `PredictionPayload`, append-only `PredictionAttempt`, append-only `CacheAccessEvent`, and evaluation-specific `ModelOverlapAudit` records. The spec records predictor ID, model family, adapter/parser source digest, executable/container digest, exact version, source, license, complete environment lock or container digest, relevant shared-library/data-table hashes, model/parameter SHA-256, frozen options, alphabet, output semantics, length limit, timeout, thread count, determinism, and immutable training-corpus provenance. Its canonical sorted-key digest is the scientific implementation identity; a parser or coordinate-conversion change must produce a new identity. Dataset-specific overlap status is keyed by model-artifact hash plus eligibility fingerprint in `ModelOverlapAudit` and is never part of the prediction-cache identity.

Each invocation receives only normalized RNA sequence, sequence SHA-256, predictor configuration, and resource limits—never dataset identity or probing measurements. A successful immutable payload contains only deterministic scientific values, null reasons, exact applied profile, stable warning codes, and scientific provenance. Warning codes are allowlisted, deduplicated, and lexically sorted; applied-profile maps use sorted keys and content-addressed relative artifact IDs. Timestamps, hostnames, temporary/absolute paths, raw tool text, and nondeterministic ordering are forbidden in payloads and belong in attempts. Attempts separately record success/failure, command and stdout/stderr digests, elapsed time, CPU time, peak RSS, host/runtime identity, and retry lineage. Cache-access events separately record hit/miss and warm-read latency. Only successful payloads are cached; timeout, corruption, and tool failures remain retryable attempts and can never masquerade as zero or a permanent cached result.

Use independent per-predictor immutable cache entries:

```text
<output>/predictors/<predictor_id>/cache/<prefix>/<key>.json.gz
```

where `key` hashes the interface schema, sequence SHA-256, and complete canonical `PredictorSpec` digest, including adapter/parser source and runtime dependency closure. Use canonical sorted-key JSON, normalized option types, and deterministic gzip metadata. Validate against the expected spec—not self-reported provenance—and verify key, sequence, length, ranges, payload checksum, and provenance on every read. Write atomically under a per-key lock. Dataset and experimental values are intentionally absent so identical sequences share predictions across conditions.

A read-only importer is mandatory for every validated completed RNAplfold/RNAfold legacy entry. It records source-file and source-payload hashes, proves imported arrays and protocols match exactly, and never mutates or warm-writes the legacy output. Tests must assert that baseline executables are not invoked for imported keys; only entries proven absent or invalid after the completed import may be recomputed under a separately recorded attempt.

## Fair comparison and winner rule

All headline comparisons are computed separately within each of the seven datasets.

1. Build a predictor-independent eligibility index from the existing prepared records and hashes. The primary transcript denominator contains normalized ACGU-only records with at least one assay-eligible window; non-ACGU records and records with zero eligible windows are excluded **before** prediction and reported separately. Predictor length limits, timeouts, execution failures, missing output positions, and invalid probabilities are predictor failures, not removals from this denominator. A predictor covers a transcript only when its full-length payload is valid and every measured position used by that transcript's eligible windows is finite. A window is covered only when all of its measured positions are finite; one null makes that predictor/window unavailable.
2. A predictor qualifies provisionally for the core ranking only if it produces finite primary scores for at least 90% of eligible transcripts **and** 90% of eligible windows in every dataset. Qualification is computed before any outcome correlation is inspected.
3. Build one all-core shared cohort per dataset. It must retain at least 80% of predictor-independent eligible transcripts and windows, plus at least 70% of eligible windows in each predeclared sequence-length stratum. Every ranked predictor must then have identical transcript, window, measured-position, and experimental-value identities and counts. Persist an eligibility fingerprint and a shared-cohort fingerprint; any identity/count mismatch is an error. If the intersection misses a threshold, there is no headline all-core ranking—only explicitly secondary maximal-coverage and pairwise analyses. Do not remove a tool post hoc based on its correlation.
4. Report:
   - pooled window Pearson;
   - median within-transcript Spearman for transcripts with at least 20 shared windows;
   - pooled per-base Pearson and median within-transcript per-base Spearman for true marginal-probability tools;
   - eligible and retained transcript/window/base counts, length exclusions, null positions, failures, timeouts, and coverage;
   - cold/warm wall time, CPU time, peak RSS, nucleotides/second, cache size, and cache-hit rate.
5. Compute ordinary paired 95% intervals with 2,000 deterministic replicates. Resample normalized-sequence SHA-256 clusters with replacement and recompute each complete metric. For the 200-nt sensitivity, assign each 20-nt window exactly once by its left central base `window_start + 9` to fixed one-based blocks `[1,200], [201,400], ...`; per-base observations use their own coordinate. Within every sampled transcript, resample its nonempty blocks with replacement, drawing the original number of nonempty blocks, and duplicate all assigned observations when a block is redrawn. Predictor-difference intervals use the same resampled units; never infer a difference from overlap of separate confidence intervals. Seed framing is `b"rna-accessibility-bootstrap-v1\0"` followed by each UTF-8 field preceded by its unsigned 64-bit big-endian byte length; fields are metric schema, dataset/study ID, metric ID, cohort fingerprint, and replicate count. Interpret the first eight SHA-256 digest bytes as an unsigned big-endian integer and use `numpy.random.PCG64DXSM` at the version pinned in the analysis environment. Ordinary intervals use linear-interpolated 2.5th/97.5th percentiles. Undefined correlations from zero variance remain null and their replicate counts are reported.
6. Rank tools independently for Pearson and Spearman within each dataset, using average ranks for exact ties. Report each paired condition contrast separately: yeast DMS in vitro/in vivo, mouse icSHAPE in vitro/in vivo, and *E. coli* SHAPE cell-free/in-cell. These paired conditions share sequence-only predictions and quantify environment/assay dependence rather than independent model evidence.
7. The primary overall endpoint is a **study-balanced Spearman score**. First average the condition-level median within-transcript Spearman values within each of four study groups (yeast DMS, mouse icSHAPE, *E. coli* SHAPE, and yeast PARS), giving paired conditions equal weight; then average the four study scores equally. Point estimates retain each condition's complete all-core cohort. In a paired-study bootstrap, form the union of normalized-sequence SHA-256 cluster IDs across its two conditions, sample that union with replacement, and apply each sampled identity and multiplicity to whichever condition(s) contain it; condition-only identities contribute only to their own condition and are never silently discarded. Yeast PARS resamples its own identities. Each replicate recomputes condition metrics before equal-weight study and four-study aggregation. Pearson receives an analogous secondary study-balanced summary. Raw assay values and observations are never pooled.
8. Freeze the `K` ranked predictor IDs before inspecting correlations and perform `20,000` synchronized hierarchical replicates for overall inference. Compute all `M=K(K-1)/2` pairwise study-balanced Spearman differences in every replicate and form two-sided Bonferroni family-wise-95% percentile intervals at quantiles `0.05/(2M)` and `1-0.05/(2M)`; report every adjusted interval. The observed top predictor is superior only if its adjusted lower bound is above zero against **every** other ranked predictor. At least 19,000 replicates must yield all required metrics or the overall inference fails. This simultaneous all-pairs procedure makes subsequent winner selection family-wise protected rather than testing only a selected runner-up.
9. A predictor is called the robust overall winner only if it passes the simultaneous all-competitor Spearman gate, remains first in all four leave-one-study-out analyses, the study-balanced Pearson point winner agrees, the fixed model-family and training-overlap-excluded sensitivities do not change the winner, and all coverage thresholds pass. Otherwise report per-dataset/per-study winners and state that no single robust overall winner was established.
10. The model-family sensitivity uses fixed memberships: `Vienna-Turner={RNAplfold,RNAfold}`, `CONTRAfold-parameter={CONTRAfold,LinearPartition-C}`, `RNAstructure={RNAstructure}`, and `EternaFold={EternaFold}`. In each condition and bootstrap replicate, compute the family condition score as the arithmetic mean of that condition's metric across the family's frozen ranked members; no best-member selection is allowed. Aggregate those family condition scores with the same condition-to-study and study-to-overall weighting as predictors. Rank family means with average ranks for exact ties and apply the same simultaneous all-pairs interval rule across represented families. The predictor winner's family must also be the statistically superior family; otherwise no robust overall predictor winner is claimed.
11. Nucleotide-identity sensitivity reports per-base Pearson and median within-transcript Spearman separately for A, C, G, and U wherever the assay observes that nucleotide. Transcript-centered sensitivity subtracts, separately within each transcript, the transcript mean experimental window value and mean predictor window value, then computes pooled Pearson on the centered pairs; within-transcript Spearman is unchanged and is not duplicated. These fixed formulas distinguish structural association from nucleotide composition and between-transcript scale effects.

EternaBench has already shown that learned statistical packages can outperform commonly used thermodynamic packages for some ensemble-oriented tasks, which motivates this comparison but does not predict the winner on these seven datasets.[7] LinearPartition's published speed and structure benchmarks likewise do not establish probing-reactivity performance here.[5]

## Training-overlap audit

Before confirmatory use of any learned model:

- hash normalized evaluation sequences against all available training manifests;
- identify near-global matches at ≥80% identity over ≥80% of the shorter sequence;
- identify local matches at ≥90% identity over ≥50 nt or ≥80% of the training sequence;
- report overlap by dataset and repeat metrics after excluding flagged transcripts;
- mark training provenance as unknown when corpora cannot be recovered.

Exact overlap is normalized-sequence SHA-256 equality. For nonexact overlap, pin NCBI BLAST+ and Parasail versions in `overlap-audit-spec.json`; generate candidates with unmasked nucleotide BLAST using word size 4 and no target-count truncation, then confirm each candidate with Parasail Smith–Waterman traceback using match `+2`, mismatch `-1`, gap-open `3`, and gap-extension `1`. Identity is exact matches divided by alignment columns including gaps; coverage is aligned non-gap residues divided by the shorter full sequence length. Apply the thresholds above to the confirmed alignment, store coordinates/CIGAR, and test boundary cases and injected positives before accepting the audit. A capped candidate list or an unversioned web service is not allowed.

Exact or near-global overlap flags the affected transcripts for exclusion from the confirmatory sensitivity analysis. Local matches are reported and receive a separate exclusion sensitivity. A learned model is disqualified from a held-out overall-winner claim if training provenance is unknown, if exact/near-global overlap exceeds 10% of eligible transcripts or 20% of eligible windows in any dataset, or if excluding any flagged class changes the winner. It may still be shown as a labeled in-training/exploratory comparator. Sequence-only execution is necessary but not sufficient to establish independence from training data.

## Test-first delivery phases

1. **Preservation:** after the active run completes, snapshot its exact code, untracked runner hash, manifest, prepared hashes, tools, runtime environment, and final record/cache counts into a checksummed preservation manifest.
2. **Eligibility freeze:** materialize a canonical sorted eligibility artifact keyed by `(dataset_id, normalized_sequence_sha256, stable_record_id, one_based_window_start, measured_position_vector)` with experimental-value and prepared-source hashes. The artifact records all excluded non-ACGU/zero-window records, direction and nucleotide mask, and length strata. Freeze its checksum before installing or executing a candidate.
3. **Contract tests:** RED-GREEN-REFACTOR tests for specs/payloads/attempts/events, spec and cache identities, array/matrix validation, retryable failures, null handling, corruption rejection, deterministic serialization, atomic writes, concurrent readers/writers, and measurement-blind invocation.
4. **Adapter tests:** golden parsers and real executable smoke tests for every pinned candidate, including complete probability mass, RNAstructure `10^(-x)` conversion, both-endpoint accumulation, one-based coordinates, matrix/context invariants, ambiguous input, length limits, timeout, and version/parameter/dependency capture.
5. **Legacy importer:** import every valid completed RNAplfold/RNAfold entry, verify arrays/protocols and source hashes exactly, prove baseline executables are not called for imported keys, and leave the source output byte-for-byte unchanged.
6. **Eligibility and cohort tests:** cover PARS sign reversal, DMS masking, missing versus zero, non-ACGU records, zero-window records, predictor length/failure accounting, one-based coordinates, 90/80/70% thresholds, shared identity/count equality, and eligibility/cohort fingerprints.
7. **Metric tests:** use hand-calculated Pearson, Spearman, average tie ranks, paired condition contrasts, union-cluster resampling with condition-only identities, study-balanced aggregation, all-pairs Bonferroni intervals, model-family means, exact typed seeds, percentile extraction, zero-variance/null behavior, and unique midpoint assignment at 200-nt block boundaries.
8. **Phase 0 runtime:** before any tool outcome metric is computed, freeze `phase0-selection.json` from the eligibility artifact. For each of the three organisms and each fixed stratum `S1…S6`, choose one unused eligible normalized sequence: nearest to the arithmetic stratum midpoint for `S1…S5`, and longest for open-ended `S6`, with SHA-256 breaking ties. If a cell is empty, choose the unused same-organism sequence with minimum distance to that stratum's nearest boundary, again breaking ties by SHA-256; if any organism has fewer than six unique eligible sequences, fail Phase 0 rather than duplicate. This yields exactly 18 pinned sequence hashes and records which cells used fallback. For each candidate, collect three application-cache-cold invocations in a hash-seeded balanced order and one warm payload-read measurement with one process and one tool thread. Cold means a fresh dedicated payload-cache root; operating-system page caches are not flushed.
9. **Pilot science:** add 25 deterministic eligible transcripts per dataset, allocating `5,4,4,4,4,4` to `S1…S6` and selecting lowest normalized-sequence SHA-256 values not already in Phase 0. Redistribute any cell deficit one record at a time cyclically to the next stratum with unused records; record the allocation, and fail if 25 unique records do not exist. Complete provenance, overlap audit, coordinate inspection, coverage/cohort gates, and all metrics before full scale.
10. **Full run:** execute independently resumable predictor shards over unique sequence hashes, freeze the predictor manifest, and compute only missing successful payload keys while appending retry attempts.
11. **Release verification:** rebuild all metrics from immutable caches in a fresh output and require identical eligibility/cohort fingerprints, metric JSON, and report checksums across worker counts and reversed input order.

## Resource and feasibility gates

No heavy work starts while the current benchmark is active. Sample the host once per minute for five consecutive minutes; every sample must show zero current-benchmark or predictor workers, one-minute load average below `2.0`, and at least `10 GiB` available RAM, while used swap changes by no more than `0.1 GiB` over the gate. Save the gate samples in the run manifest.

Phase 0 uses one predictor process and one tool thread with `OMP_NUM_THREADS=MKL_NUM_THREADS=OPENBLAS_NUM_THREADS=1`. Record hostname, CPU model, logical/physical CPU counts, RAM/swap, kernel/WSL versions, locale, environment lock/container digest, executable and `ldd` fingerprints, command, working directory, and all thread variables. For each panel point, the cold wall-time estimate is the maximum of its three application-cache-cold attempts; form a monotone piecewise-linear upper envelope in log-length/log-time space, sum its predicted time over every unique eligible sequence, multiply by `1.25`, and divide only by the memory-safe planned worker count. Nearest-rank p95 RSS over the three attempts (therefore their maximum) sets `workers = min(logical_cpus - 4, floor((available_RAM - 4 GiB) / p95_RSS))`, never below one. A predictor/length stratum is quarantined before outcome correlations are inspected if an invocation exceeds `8 GiB` RSS or two hours, or if the projected full run exceeds seven wall-clock days. Memory-heavy global predictors run in separate waves unless Phase 0 proves co-scheduling safe.

The eventual output root will be separate from the active run, for example:

```text
/home/zivbental/workspace/experiments/rna-accessibility-multitool-v1
```

## Acceptance criteria

- The active checkout, process tree, prepared data, and `results_parallel` remain unmodified.
- Every adapter records exact binary/model/config/dependency/adapter hashes and passes unit, golden-parser, complete-mass, coordinate, matrix/context-invariant, and real-executable tests.
- Successful scientific payloads are immutable and byte-deterministic; failures are retryable append-only attempts; warm cache reads create events rather than mutate payloads.
- Cold and warm scientific outputs are identical; only separate attempt/cache-event telemetry differs.
- Existing experimental preparation is reused read-only, its hashes are verified, and a canonical eligibility artifact is frozen before tool execution.
- Every valid completed RNAplfold/RNAfold entry is imported exactly, source hashes are retained, and imported keys never invoke baseline executables.
- Ranked predictor IDs are selected only from the six named confirmatory candidates by pre-outcome gates and frozen before evaluation values are read; exploratory tools never alter the primary cohort.
- Headline tools each meet 90% transcript/window coverage; the all-core shared cohort meets 80% transcript/window and 70% per-length-stratum retention; all ranked tools have identical shared identities and denominators per dataset.
- Every dataset reports Pearson, Spearman, paired uncertainty intervals, coverage, failures, and resources; matrix failures are never clipped or renormalized.
- Cross-study summaries use the frozen study-balanced rule, paired condition contrasts, and model-family sensitivity; raw assay values are never pooled.
- Learned-model overlap and overlap-excluded sensitivity results are reported.
- Interrupt/resume, failed-attempt retry, concurrent cache access, and worker/input-order invariance are verified.
- A robust-winner claim passes simultaneous family-wise-adjusted superiority against every frozen competitor, leave-one-study-out, Pearson-agreement, fixed model-family, training-overlap, and coverage gates; otherwise the report explicitly states that no single robust overall winner was established.
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
[14] https://github.com/mxfold/mxfold2/issues/27 — MXfold2 issue 27: BPP numerical behavior
