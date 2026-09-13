# Extending `rnavail`: implementation proposal

This document records the staged extension derived from the literature review.
It preserves the tool's useful core question—how often a target interval is
unpaired in one RNA under a declared secondary-structure model—while making
that answer internally consistent and keeping recognition, experimental
context, and cellular effects as separate evidence layers.

The first release should improve correctness and provenance without claiming to predict binding. Partner-specific energetics, cellular evidence, and three-dimensional simulation should remain distinct optional layers. The related scientific rationale and references are in [the literature review](08-rna-accessibility-literature-review.md).

## Implementation status

The following core work is implemented in the current codebase:

| Area | Delivered behavior |
|---|---|
| Target event and conditions | `RecognitionSpec` and `ConditionSpec` are carried through scan/evaluate, written to reports, and validate temperature plus sodium consistency with the folding settings. Fixed/listed seed coordinates constrain eligibility only where a complementary seed mechanism is applicable. |
| Probing and identity | SHAPE/DMS input validates target identity, positions, bases, finite values, duplicates, source hash, condition, and conversion provenance. DMS needs an explicit conversion choice. Compatible local, global, and visualization paths receive the same track. |
| Protocol honesty | Every adapter records requested, applied, unsupported, and deliberately ignored settings plus `compatible_with_requested`. Probability results with material unsupported settings are excluded from compatible consensus while remaining raw diagnostics. |
| Coherent opening and numerical states | Candidate headline opening fields come from one `OpeningObservation`, not separate probability/energy medians. Bounds, censored zero probabilities, nonfinite numerical status, and sampling zero-hit limits remain distinguishable. |
| Evidence lineage and ranking | RNAplfold interfaces share one group; global ViennaRNA PF, `rnafold`, and sampling share `vienna-global-pf`. The score is named `heuristic_rank_score`, uses four default criteria, and records coverage. Non-complementary recognition classes exclude seed-derived ranking criteria. |
| Seed provenance | All permitted RNAplfold seed trials are retained; exact budget-skipped trials and sampling bounds are explicitly marked. |
| Biological evidence overlays | Versioned JSON tracks for probing, contacts, protein interaction, ribosome, modifications, variants, direct hybridization, and custom evidence validate the selected sequence hash and one-based coordinates. Overlaps are condition-labeled report annotations; they do not change the structural rank or imply occupancy. |
| G4 safety | G4-aware joint opening is refused where the backend cannot enforce that event; G4Hunter remains a signed sequence-propensity diagnostic. |

The original Phase 0–2 text below is retained as a design record and explains
why those changes were made. It should not be read as a description of the
pre-change code. The remaining proposals are **not implemented**: isoform and
haplotype-aware analysis beyond generic annotation tracks, partner-specific
interaction calculations, calibrated endpoint prediction, the YAML
configuration manifest, and kinetic/CGMD research modules. Their sections
define requirements for later work rather than current output.

## 1. Current architecture and the safe extension points

The implementation already has useful boundaries:

| Concern | Current location | Proposed role |
|---|---|---|
| Physical settings | `rnavail/core/model.py` | Separate local and global model settings; add condition and recognition specifications |
| Metric vocabulary | `rnavail/core/result.py` | Replace context-free floats with coherent, traceable observations |
| Adapter request | `rnavail/adapters/base.py` | Carry recognition, conditioning, and capability requirements to every adapter |
| Tool integrations | `rnavail/adapters/` | Declare supported settings, model family, algorithm, and event definition |
| Evaluation and scans | `rnavail/pipeline/run.py` | Apply one declared protocol consistently and preserve evidence layers |
| Aggregation and ranking | `rnavail/pipeline/score.py` | Select a primary coherent estimate; keep model disagreement separate from score |
| CLI | `rnavail/cli.py` | Add explicit configuration while keeping existing commands usable |
| Input parsing | `rnavail/io/fasta.py` | Validate sequence and probing identity rather than silently guessing |
| Reports | `rnavail/io/report.py`, `html_report.py`, `rundir.py` | Expose event, conditions, applied settings, unsupported fields, and evidence gaps |

Every existing joint interval estimate currently comes from the ViennaRNA model family: RNAplfold through two interfaces, constrained partition functions, or sampling from a ViennaRNA partition function. Other adapters provide useful structural or marginal diagnostics, but they do not constitute many independent measurements of joint accessibility. The data model should state this directly.

The main evidence-to-feature mapping is:

| Literature finding | Implementation response |
|---|---|
| [Joint interval events and local-window probabilities](08-rna-accessibility-literature-review.md#11-five-quantities-that-should-remain-separate) have specific ensemble definitions | Store one coherent observation with event, interval, scope, model, temperature, `P`, and derived energy |
| [Nucleation and displacement](08-rna-accessibility-literature-review.md#12-joint-probability-is-essential-but-complete-pre-opening-is-not-universally-necessary) can bypass complete pre-opening | Add binder-specific seed placement, orientation, and footprint through `RecognitionSpec` |
| [Partner chemistry](08-rna-accessibility-literature-review.md#22-opening-energy-is-only-one-thermodynamic-contribution) changes the interaction model | Keep target opening separate; enforce capability checks for RNA/RNA, RNA/DNA, and modified partners |
| [Folding history and probe exposure](08-rna-accessibility-literature-review.md#23-identical-equilibrium-accessibility-can-conceal-different-kinetics) affect observed binding | Add preparation, concentration, order, and time to `ConditionSpec`; do not derive rates from equilibrium `P` |
| [Proteins, ribosomes, modifications, isoforms, and compartments](08-rna-accessibility-literature-review.md#5-cellular-accessibility-includes-occupancy-and-active-remodeling) can change the relevant population | Add condition-linked evidence tracks and exact transcript identity; keep unknown evidence unknown |
| [Probing assays measure chemistry-specific observables](08-rna-accessibility-literature-review.md#6-experimental-evidence-what-each-assay-can-support) | Add validated `ProbingTrack` provenance and require consistent conditioning across all calculations |
| [Tools share models and transformed metrics share information](08-rna-accessibility-literature-review.md#7-computational-uncertainty-and-score-interpretation) | Record evidence lineage, derive transforms from one primary estimate, and label the composite heuristic |
| [CGMD descriptors are conditional on representation and sampling](08-rna-accessibility-literature-review.md#8-three-dimensional-modeling-and-the-existing-cgmd-proposal) | Keep 3D analysis as a separately validated research module with restraint and convergence provenance |

## 2. Phase 0: correct the meaning of existing output

These changes should precede new features because later layers would otherwise build on inconsistent baseline values.

### 2.1 Apply probing data consistently or declare it unused

`RNAplfoldAdapter.compute_accessibility()` calls `local_unpaired_matrix()` without `request.probing`. The profile builder in `pipeline/run.py` follows the same path. As a result, `scan --shape` can shortlist from an unconditioned local ensemble and later combine those values with probing-conditioned `vienna-exact` results, without warning.

Implement the following:

1. Add `probing: ProbingData | None` to `adapters/_vienna.py:local_unpaired_matrix()` and apply the supported soft constraint to its window fold compound.
2. Thread the same `ProbingData` through `RNAplfoldAdapter`, `_build_profile()`, `_length_sweep()`, and any visualization that performs a new fold.
3. Require each adapter to report `conditioning=applied`, `unsupported`, `not_requested`, or `deliberately_omitted`, plus a reason.
4. Exclude observations with different conditioning IDs from arithmetic aggregation. They may be displayed side by side.
5. Validate that the supplied track belongs to the exact sequence and coordinate system before folding.

The command-line RNAplfold adapter already accepts a SHAPE file, but it does not pass all requested model settings. It should participate in consensus only when its applied protocol matches the Python adapter for every field that affects the calculation.

**Acceptance test.** For `GGGCGCGCGCAAAAGCGCGCGCCC`, positions 1–8, a strongly pairing-disfavoring synthetic reactivity vector should materially change both local and global compatible estimators. The screen, candidate profile, deep evaluation, and visualizations must share a conditioning ID. Any adapter unable to apply that track must say so in machine-readable output.

### 2.2 Define a valid G-quadruplex-free target event

With ViennaRNA 2.7.2 in this environment, forcing every target nucleotide “unpaired” through `fc.hc_add_up()` does not exclude its participation in a G-quadruplex. For `GGGAGGGAGGGAGGG` with G4 enabled, the MFE contains `+` G4 symbols while the constrained calculation reports `P_unpaired=1` and `ΔGopen=0` for the full sequence.

The initial safe implementation is:

- Refuse joint accessibility and seed scoring when G4 mode is enabled unless the backend can enforce the declared event “not Watson–Crick paired and not part of a modeled G4.”
- Continue reporting `gquad-scan` as sequence propensity, labeled as such, with the tested sequence interval and context.
- Keep motif propensity, a predicted G4 state, and experimental G4 evidence as different observation types.
- Add backend-specific capability tests before enabling G4-conditioned joint probabilities.

Also revise `adapters/gquad.py`: it currently stores the absolute value of the strongest signed G4Hunter window, inherits the generic `probability` estimand, and labels a negative C-rich RNA window as an i-motif. Preserve the signed score and peak interval, label it `sequence_propensity`, retain the empirical method and threshold domain, and do not infer an occupied RNA i-motif from C richness alone.

Do not recommend `vienna-exact` as G4-aware accessibility until that event test passes. The reproduced behavior is specific to the installed version and invocation, so the guard should be capability-tested rather than inferred from a version number alone.

### 2.3 Correct the MFE/ensemble-gap interpretation

The code defines the gap as `G_MFE − G_ensemble`. Under a consistent Boltzmann model,

```text
P(MFE state) = exp[−(G_MFE − G_ensemble)/(RT)].
```

A gap near zero therefore means high weight on the MFE state; it does not mean a diffuse ensemble. Reverse the current warning logic in `adapters/vienna_fold.py`, correct its explanatory text, and avoid treating MFE dominance as an accuracy guarantee.

**Acceptance test.** An all-A control with a zero gap and unit MFE probability must not receive a “diffuse ensemble” warning. A constructed multi-state sequence should have a larger nonnegative gap and lower calculated MFE-state probability.

### 2.4 Record applied settings instead of copying requested settings

`Adapter.new_result()` currently copies the requested `ModelSettings` into each result even when the backend ignores fields. This can imply false protocol parity. Add a capability declaration and a resolved protocol:

```python
@dataclass(frozen=True)
class AdapterCapabilities:
    supported_settings: frozenset[str]
    supported_conditioning: frozenset[str]
    event_definitions: frozenset[str]
    model_family: str
    algorithm: str

@dataclass(frozen=True)
class AppliedProtocol:
    requested: dict[str, object]
    applied: dict[str, object]
    unsupported: dict[str, str]
    ignored_by_design: dict[str, str]
```

An adapter should fail or produce a diagnostic-only result when an unsupported field is material to the requested estimate. The report should show requested, applied, and unsupported fields separately.

The current global ViennaRNA path also applies `max_bp_span=150`. Split the setting into `local_max_bp_span` and `global_max_bp_span: int | None`. A full-sequence calculation with a finite global span is valid, but should be called “global constrained partition function with span 150,” rather than unrestricted or physically exact.

**Acceptance test.** A synthetic long-distance stem must distinguish an unrestricted global model from a finite-span global model. Command-line and Python RNAplfold results may share an independence group only when their resolved protocols match.

### 2.5 Keep probability, energy, interval, and seed together

The consensus layer aggregates every metric independently. It can therefore report a median probability and median opening energy that do not satisfy their defining relation. In an existing saved report, region 457–476 has consensus `P=0.0245983` and `ΔG=3.4960 kcal/mol`; at 37 °C, the reported probability transforms to approximately `2.2836 kcal/mol`, not `3.4960`.

Replace independent aggregation for related fields with a coherent observation:

```python
@dataclass(frozen=True)
class OpeningObservation:
    interval: Region
    p_unpaired: float | None
    dg_open_kcal_mol: float | None
    temperature_c: float
    event: str
    model_family: str
    protocol_id: str
    conditioning_id: str
    method: str
    estimate_kind: Literal["point", "upper_bound", "lower_bound", "interval"]
    uncertainty: dict[str, float]
```

Choose one primary observation, then derive `ΔGopen` and `ΔGopen/nt` from its `P` and temperature, or store a backend energy as primary and derive `P`. Preserve other observations and disagreement without constructing a hybrid physical estimate.

Seed identity belongs in the same record. Do not median `seed_start` independently from seed probability. Evaluate a shared set of seed intervals across compatible tools, then compare like with like.

**Acceptance tests.** Every point estimate with `0 < P ≤ 1` must satisfy the thermodynamic transform to numerical tolerance. A seed coordinate must be an integer interval and must be the interval that produced the attached probability. Bounds and censored values must remain bounds rather than being transformed into ordinary point estimates.

### 2.6 Represent numerical floors, caps, and unavailable tools

`core/thermo.py` currently clamps probabilities below `1e-30` before converting them to energy and separately defines a `100 kcal/mol` cap. The nominal inverse transformation does not preserve those censored values, and `RegionMetrics.set()` drops nonfinite values. An underflow, an exact zero returned by a backend, and a missing result can therefore become a finite point estimate or disappear.

Add explicit `censor_reason`, lower/upper bound fields, and the backend's numerical status. Preserve `P=0` as a censored or bounded result unless the model supplies an exact mathematical zero; transform a probability interval by reversing its endpoints in energy space. Constrained and unconstrained partition functions must use compatible numerical scaling, with failures exposed rather than capped into plausible values.

`adapters/registry.py:select()` also filters unavailable adapters before an explicitly requested tool can produce a skipped result. Resolve and save the complete requested tool inventory first, including availability and unsupported-condition reasons, then run the eligible subset. This makes absence auditable in saved reports.

**Acceptance tests.** Round trips must distinguish a measured zero, probability underflow, an upper bound, a nonfinite backend failure, an unsupported event, and a missing measurement. An explicitly requested unavailable tool must appear in `meta.json` and the report with its reason and installation hint.

## 3. Phase 1: make the target event and experimental condition explicit

### 3.1 Add `RecognitionSpec`

The current free search for the best internal 10-nt seed is useful as an exploratory diagnostic, but it is not a universal binding mechanism. Add an optional specification:

```python
@dataclass(frozen=True)
class RecognitionSpec:
    footprint: Region
    binder_class: Literal[
        "generic_complementary_strand", "dna_probe", "rna_probe",
        "cas13", "protein", "small_molecule", "custom"
    ]
    partner_sequence: str | None = None
    partner_chemistry: str | None = None
    orientation: Literal["antiparallel", "parallel", "unspecified"] = "unspecified"
    seed_mode: Literal["any_internal", "five_prime", "three_prime", "fixed", "listed"] = "any_internal"
    seed_lengths: tuple[int, ...] = (10,)
    allowed_seeds: tuple[Region, ...] = ()
    endpoint: Literal["binding", "cleavage", "activation", "regulation", "unspecified"] = "unspecified"
```

For `protein` and `small_molecule`, interval unpairing should remain a structural descriptor and the report must state that greater unpairing is not assumed to be more favorable. For complementary strands, report full-footprint opening and every permitted seed. “Best seed” remains a multiple-comparison selection and should be confirmed using the primary estimator.

`--seed-length` should remain as a backward-compatible shortcut for `any_internal`. Reports should mark it `generic exploratory seed`, not a binder-specific nucleation model.

### 3.2 Add `ConditionSpec`

```python
@dataclass(frozen=True)
class ConditionSpec:
    condition_id: str
    temperature_c: float
    sodium_molar: float | None = None
    potassium_molar: float | None = None
    magnesium_total_molar: float | None = None
    magnesium_free_molar: float | None = None
    ph: float | None = None
    crowding_agent: str | None = None
    crowding_concentration: str | None = None
    preparation: str | None = None
    incubation_seconds: float | None = None
    partner_concentration_molar: float | None = None
    biological_context_id: str | None = None
```

Adapters resolve only the fields they actually support. Unsupported Mg²⁺, pH, and crowding values should appear as explicit evidence gaps. Do not convert them to an invented energy offset. A condition matrix can rerun supported variables and compare ranks, but it is a scenario analysis rather than a confidence interval.

### 3.3 Improve sequence identity and probing provenance

Extend `ProbingData` or replace it with a versioned `ProbingTrack` containing:

- assay chemistry and protocol, reagent, pH, temperature, biological preparation, and condition ID;
- exact sequence checksum, transcript/accession and version, one-based coordinate mapping, and target record ID;
- replicate IDs, normalization and conversion method, raw/mapped coverage, and missingness mask;
- base identities when present in the input, plus explicit treatment of insertions, deletions, and mature-RNA processing;
- the original input hash and parser/schema version.

Input validation should reject duplicate positions, nonfinite reactivities, positions outside the sequence, and base-identity mismatches. Measured zero and unmeasured must stay distinct. Multi-record FASTA input should require an explicit record selection or process every record; it should not silently take the first record.

Use assay-specific names. `--shape` may keep its current behavior for compatible SHAPE data, while a future `--probing-config track.yaml` selects chemistry and conversion explicitly. Do not apply a Deigan SHAPE conversion to an arbitrary DMS track by default.

## 4. Phase 2: restructure consensus and ranking

### 4.1 Select a primary estimate, then show sensitivity

For each target and condition:

1. Use RNAplfold as the fast local screening estimate, labeled as a window-averaged local ensemble.
2. Re-evaluate shortlisted regions with a global constrained partition function under the declared global span and identical conditioning.
3. Use sampling from the same ViennaRNA model as a numerical or state-inspection check, not another independent biological vote.
4. Show RNAstructure, learned-model, pseudoknot, G4, and kinetic-path outputs as their actual estimands.
5. Select the global constrained result as the default primary opening observation when it is supported and successfully computed. Otherwise fall back visibly and state why.

Local-global disagreement should be described as sensitivity to ensemble scope and windowing. It cannot by itself prove a long-range pairing partner or establish which result is physically correct.

When users request several materially different contexts, conditions, or structural models, a shortlist produced by one screen can discard candidates favored by every other protocol. Build a bounded union of top candidates from each declared screening protocol, plus explicitly requested controls, before the global confirmation and final rerank. Record each protocol's admission rank and cap so this remains computationally predictable.

### 4.2 Replace “independent tools” with evidence lineage

Add per-observation fields:

```text
model_family     algorithm       parameter_set        interface
event            sequence_scope conditioning_id      protocol_id
```

For example, RNAplfold Python and CLI share model family, algorithm, and parameter set; their agreement validates integration parity. Vienna constrained PF and Vienna sampling use different estimators but the same physical model family. Pair probabilities from a learned energy model and a single predicted structure must not enter the median of Boltzmann probabilities.

Reports may retain `n_tools` for operational transparency. Rename `n_independent` to a narrower, auditable concept such as `n_distinct_protocols` and avoid equating it with biological independence.

### 4.3 Make the ranking explicitly heuristic until calibrated

The default score currently includes full-region probability and its transformed opening energy per nucleotide, which duplicates one signal at fixed length and temperature. It also renormalizes around missing criteria, allowing equal scores with different evidence coverage.

For an uncalibrated release:

- rank primarily by the declared structural objective, such as seed `ΔGopen` followed by full-footprint `ΔGopen/nt`;
- expose robustness, protocol disagreement, alternative-structure flags, and evidence coverage as separate columns;
- optionally produce a Pareto shortlist rather than forcing every item into one scalar;
- retain the existing composite only as `heuristic_rank_score`, with its anchors, weights, saturation, and missing-feature behavior in the report;
- never call a value between zero and one a probability of binding or success.

For a calibrated release, define a binder and endpoint, then fit weights on measured examples. Split training and evaluation by transcript, structural family, and condition; overlapping sliding windows must not cross the split. Compare against simple baselines and report held-out ranking and probability calibration separately.

### 4.4 Quantify only the uncertainty that the calculation supports

Use distinct fields for:

- numerical or Monte Carlo uncertainty;
- model/protocol disagreement;
- condition sensitivity;
- sequence/isoform variation;
- missing biological evidence.

For structure samples, attach a binomial interval to every hit count, including zero and all-hit cases. The one-sided 95% upper bound after zero independent hits is `1 − 0.05^(1/N)`; `3/N` is only an approximation. If samples or trajectory frames are correlated, use an effective sample size or time-series analysis.

Apply uncertainty per seed placement before choosing the best seed. The current exact seed scan subsamples when placements exceed `SEED_SCAN_BUDGET`; ensure any declared scan includes both terminal placements and report every omitted interval. The sampling adapter should not report optimized empirical seed values of exactly zero or one without their intervals or the fact that several placements were searched. Confirm a selected seed with the primary estimator or an independent sample set.

Do not combine these categories into a conventional confidence interval unless a statistical model justifies that operation.

### 4.5 Make robustness sweeps isolate one change at a time

The current length sweep fixes the 5′ start, changes the 3′ end, and constructs a new ±100-nt context for each length. It also omits probing. This changes footprint and folded sequence together. Build one enclosing context large enough for every tested length, slice one compatible probing track onto that context, and vary only the footprint. Offer 5′-anchored, 3′-anchored, and centered policies when the recognition mechanism does not determine the anchor.

The context sweep currently tests several flanks and the full sequence, while other documentation describes a single ±100-nt frame. Emit the actual boundaries for every scenario. Describe mutation, context, parameter, and length sweeps separately because they perturb different assumptions. A shortlist-only robustness run cannot establish that the original screen retained all candidates favored by an alternative protocol; use the multi-protocol union when that question matters.

## 5. Phase 3: add biological evidence as condition-linked tracks

### 5.1 General evidence-track interface

Use annotations before numerical penalties:

```python
@dataclass(frozen=True)
class EvidenceTrack:
    evidence_type: Literal[
        "probing", "duplex_contact", "protein_interaction", "ribosome",
        "modification", "variant", "direct_hybridization", "custom"
    ]
    source: str
    condition_id: str
    transcript_id: str
    sequence_hash: str
    records: tuple["EvidenceRecord", ...]
    provenance: dict[str, object]

@dataclass(frozen=True)
class EvidenceRecord:
    interval: Region
    value: float | str | bool | None
    unit: str | None
    uncertainty: dict[str, float]
    missing_reason: str | None
    interpretation: str
```

Do not interpret lack of a CLIP peak as vacancy, a protein motif as occupancy, a ribosome-profile read as guaranteed steric blockage, or a G4 motif as a folded G4. Each report should show evidence type, measurement condition, coordinate mapping, and interpretation limit.

### Implemented JSON overlay

`--evidence FILE.json` accepts either one version-1 track or a manifest with
`{"evidence_schema_version": "1.0", "tracks": [...]}`. Each track carries a
required normalized-target SHA-256, transcript ID, condition ID, source, and
one or more one-based inclusive records. Obtain the normalized target hash
from a previous `report.json`; this prevents an annotation for a similarly
named but different transcript from being silently overlaid.

```json
{
  "evidence_schema_version": "1.0",
  "track_id": "eclip-rep1",
  "evidence_type": "protein_interaction",
  "source": "doi:...",
  "condition_id": "HEK293_buffer_A",
  "transcript_id": "NM_example.3",
  "sequence_hash": "<report sequence sha256>",
  "records": [{
    "interval": {"start": 205, "end": 224},
    "value": 3.2,
    "unit": "normalized_enrichment",
    "uncertainty": {"sem": 0.4},
    "interpretation": "Peak enrichment is not direct occupancy evidence.",
    "metadata": {"replicate_ids": ["r1", "r2"], "strand": "+"}
  }]
}
```

```bash
rnavail evaluate transcript.fa --region 205-224 --condition-id HEK293_buffer_A \
  --evidence eclip.json --json report.json
```

The parser rejects a wrong hash, a non-finite numeric value, unsupported
coordinate convention, or any record outside the selected sequence. A
different evidence condition is retained as `different_condition`, not folded
into a matched-condition interpretation. JSON reports retain full tracks at
the root and overlapping records under each candidate's
`biological_evidence`; text and HTML reports show a compact annotation view.

### 5.2 Isoforms, variants, and mature sequence

Add a manifest that maps target intervals to exact transcript versions. Report:

- which relevant isoforms contain the complete site;
- the site's coordinate in each sequence and whether flanking context changes;
- condition-matched isoform abundance when supplied;
- observed variants and allele frequency when supplied;
- separate folding results for each sequence rather than one mean sequence.

The existing exhaustive target-only SNV sweep should be renamed `hypothetical_local_mutation_sensitivity`. A biological variant mode should accept real alleles in the target and flanks, preserve haplotypes, and keep population frequency separate from structural effect.

### 5.3 Protein, ribosome, modification, and contact overlays

Initial integrations can accept BED-like interval tracks plus metadata. They should add flags and report sections without changing the structural score. Later, a target-specific calibrated model can learn whether a given evidence type helps predict a declared endpoint.

Modification records need identity and estimated stoichiometry when known. Alternative duplex records need both arms, direction, evidence method, and condition. Ribosome and protein records should preserve strand, replicate, cell state, normalization, and measurement uncertainty.

## 6. Optional partner-specific interaction layer

The repository intentionally removed RNA–RNA interaction adapters to retain a clean single-molecule scope. Reintroduce them only as an opt-in layer with a separate result type and command, for example:

```bash
rnavail interact target.fa --region 205-224 \
  --partner probe.fa --partner-chemistry rna \
  --seed-mode five_prime --seed-length 8
```

This proposed command does not exist yet. It would:

1. compute target and partner opening contributions;
2. calculate the partner-specific intermolecular term with IntaRNA/RNAup when the chemistry is supported;
3. retain the energy decomposition and predicted paired intervals;
4. accept partner concentration only for a separately defined occupancy model;
5. search competitors only when a reference transcriptome and abundance assumptions are explicitly supplied.

Do not use the current DNA-target folding parameters for a DNA probe binding RNA. RNA/DNA hybrid energetics need suitable hybrid parameters, including attention to the published correction to lower-salt parameter tables. LNA, PNA, phosphorothioate backbones, other modifications, and protein-assisted recognition remain unsupported unless a validated model is added.

The 2025 23-method interaction benchmark evaluates recovery of intermolecular base pairs in known complexes. It can inform tool selection, but it does not validate live-cell binding, rates, or functional output. Benchmark the chosen adapter against the actual intended endpoint.

## 7. Three-dimensional and kinetic analysis

### 7.1 Keep kinetic outputs honest

The current `kinwalker` field records one heuristic cotranscriptional path and the earliest prefix from which any target nucleotide remains paired. Rename the metric to describe that predicate precisely. Do not interpret it as a rate, dwell time, full-site closure, or proof that the target is locked.

A later kinetic layer should define transcription speed and pauses, binder arrival and concentration, seed pathway, and observation horizon. It should operate on selected constructs and be validated against time-resolved binding data. Equilibrium `P_unpaired` remains an input or comparison, not a rate constant.

### 7.2 Treat CGMD as a separately validated research module

The current Katzir-inspired document proposes Martini/GROMACS analysis. The cited Katzir study concerns ssDNA/peptide condensates, while the Martini 3 RNA paper demonstrates prestructured RNA and RNA–protein dynamics and uses elastic networks in complex systems. Neither validates a universal RNA-gate `f_available` threshold.

Before any CGMD result enters `rnavail`:

1. State the event the model must represent: static steric exposure, spontaneous melting, or strand invasion.
2. Verify that its force field, topology, elastic network, and restraints permit that event.
3. Preserve starting-structure provenance, mapping, force-field files and hashes, ion model, replica settings, equilibration, and sampling diagnostics.
4. Report target-specific distributions of geometric features, contact occupancy, and replica sensitivity.
5. Account for trajectory autocorrelation; frame count is not an independent sample count.
6. Validate candidate-level features against matched direct binding or function before incorporating them in a ranker.

Use SASA only as geometric exposure under a named atom/bead selection and probe radius. Whole-RNA radius of gyration is a global compactness diagnostic. A thresholded frame fraction should be named for its exact predicate, such as `fraction_frames_passing_geometry_rule`, rather than `P_available`.

If oxRNA is explored for strand displacement, keep it as a different model family with its own chemistry and validation range. Do not pool its trajectory-derived event with ViennaRNA equilibrium values.

## 8. CLI and configuration proposal

Keep the present simple commands working. Add one versioned YAML manifest for advanced runs:

```yaml
config_schema_version: 1
target:
  fasta: transcript.fa
  record: NM_example.3
  transcript_version: NM_example.3
recognition:
  binder_class: dna_probe
  footprint: 205-224
  partner_sequence: ATGCACTGACTGACTGACTG
  partner_chemistry: unmodified_dna
  seed_mode: three_prime
  seed_lengths: [6, 8, 10]
  endpoint: binding
condition:
  id: in_vitro_buffer_A
  temperature_c: 37
  sodium_molar: 0.10
  magnesium_total_molar: 0.001
  ph: 7.4
  incubation_seconds: 600
probing_tracks:
  - file: target.shape.tsv
    chemistry: 1M7_SHAPE
    condition_id: in_vitro_buffer_A
    conversion: deigan
```

Proposed invocation:

```bash
rnavail evaluate --config experiment.yaml --save-run
```

The resolver should show that ViennaRNA used temperature and supported monovalent settings while Mg²⁺ and pH remained unmodeled. Because partner chemistry is DNA, the single-molecule target-opening layer can run, while any RNA-only interaction engine must decline the hybrid-energy estimate.

## 9. Output schema and user-facing report

Add a schema version and preserve raw observations. A candidate JSON object should contain:

```json
{
  "region": {"start": 205, "end": 224},
  "recognition_spec_id": "...",
  "condition_id": "in_vitro_buffer_A",
  "primary_opening_observation_id": "...",
  "opening_observations": [],
  "seed_observations": [],
  "structural_diagnostics": [],
  "biological_evidence": [],
  "uncertainty": {},
  "unsupported_assumptions": [],
  "heuristic_rank_score": null,
  "evidence_coverage": {}
}
```

At the report root, use a separate field such as `"report_schema_version": "2.0"`; the configuration and output schemas evolve independently.

The text, TSV, and HTML reports should lead with:

1. target identity and the recognition event;
2. primary structural estimate with interval, model, scope, conditioning, and transform-consistent energy;
3. permitted seed results with coordinates;
4. disagreement and robustness by source;
5. experimental or biological evidence in matched and unmatched conditions;
6. unmodeled assumptions and unavailable tools;
7. heuristic rank, if requested, clearly separated from probabilities.

Record source sequence and probing hashes, configuration bytes, schema version, package and executable versions, parameter-file identifiers, and tool capability resolutions in `meta.json`. The workspace currently lacks Git metadata, so the run should explicitly record `source_revision: unavailable` rather than imply code provenance.

## 10. Delivery sequence

| Milestone | Status | Deliverable / exit criterion |
|---|---|---|
| P0a | implemented | Probing propagation and validation across compatible screen, profile, deep evaluation, and figures |
| P0b | implemented | G4 event guard and corrected MFE/ensemble-gap interpretation |
| P0c | implemented | Applied-protocol records and separate local/global span settings; material unsupported settings are explicit |
| P0d | implemented | Coherent opening/seed observations and numerical states; seed trial provenance distinguishes evaluated, censored, bounded, and skipped placements |
| P0e | implemented in report paths | Failed/skipped requested calculations remain visible with reasons |
| P1 | implemented | Recognition and condition specifications, including unsupported environmental assumptions and mechanism-aware seed ranking |
| P2 | implemented | Evidence lineage, conditioning/protocol gates, and heuristic-rank coverage |
| P3 | implemented, annotation-only | Validated probing and generic JSON evidence tracks preserve identity, coordinates, conditions, missingness, uncertainty, provenance, and overlap reports without inventing a score penalty |
| P4 | deferred | Optional interaction command with decomposed target/partner opening and chemistry capability checks |
| P5 | deferred | Empirical endpoint calibration with held-out transcripts and conditions |
| Research | deferred | Kinetic or CGMD module with represented event, sampling, and direct-experiment validation |

The delivered work preserves the present single-molecule scope. P4 and later
stages remain optional modules with their own estimands and validation.

## 11. Test plan

Add focused tests for scientific semantics rather than tests that mirror individual assignments:

- probing changes every compatible path and unsupported paths visibly decline it;
- target sequence hash and probing base identities match, while duplicates, nonfinite values, and invalid coordinates fail;
- multi-record FASTA behavior is explicit;
- local/global span controls expose a designed long-distance stem;
- G4 target-open constraints exclude modeled G4 occupancy or refuse the estimate;
- `P` and `ΔG` always remain transform-consistent;
- seed probability always identifies one evaluated integer interval and supported orientation;
- sampling returns intervals for zero, intermediate, and all hits;
- underflow, exact zero, censoring, backend failure, and missingness survive report round trips as distinct states;
- MFE-state probability and gap interpretations agree on simple controls;
- requested/applied/unsupported settings survive JSON and report round trips;
- explicitly requested unavailable adapters remain visible in the tool inventory;
- no probability, posterior, single-structure state, motif score, or experimental reactivity is pooled with another estimand by default;
- multi-protocol screening admits the bounded union before global reranking;
- length sensitivity uses one fixed enclosing context and identical probing while varying the footprint;
- saved reports remain readable after a schema migration and old reports identify their legacy semantics.

After these unit and integration controls, benchmark local screening against global confirmation on multiple sequence lengths and structures. For biological validation, pre-register the binder, endpoint, conditions, and train/test split, then include accessible, buried, model-disagreement, and context-sensitive candidates rather than testing only top-ranked sites.

## 12. Decisions to defer until evidence exists

Do not hard-code a universal seed length, Mg²⁺ correction, crowding penalty, protein-occupancy penalty, G4 penalty, cellular unfolding factor, CGMD exposure cutoff, or candidate-count threshold. Do not treat SHAPE reactivity as a probability of oligo access or map an interaction-energy score directly to cellular success.

Store enough structure and provenance to learn such relationships for a defined assay later. Until then, `rnavail` should report a coherent structural estimate, the evidence that changes its interpretation, and the assumptions it cannot model.
