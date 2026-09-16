# 9. Current implementation status and roadmap

This page replaces the original pre-implementation proposal. It describes what
the repository does **now**, which scientific promises it deliberately does
not make, and the evidence required before expanding its scope.

The original design problem was broader: combine target opening, partner
interaction, gate design and coarse-grained molecular dynamics. Implementation
work showed that combining those layers into one “availability” number would
hide incompatible assumptions. The current project therefore makes the
single-molecule target-opening layer rigorous and leaves later layers separate.

## 9.1 Scope of the current release

The implemented question is:

> Under a declared secondary-structure protocol, what is the probability that
> a selected interval of one target molecule is fully unpaired?

The answer carries its sequence identity, coordinates, model family,
algorithm, local/global scope, temperature, conditioning and numerical status.
Recognition and environmental fields record what the user intends, but a
field appearing in a report does not imply it was modeled.

The following are outside the current calculation:

- partner-target hybridization energy and specificity;
- equilibrium complex concentration;
- cleavage, repression, translation or fluorescence;
- multi-strand gate-state design;
- atomistic or coarse-grained three-dimensional dynamics;
- universal corrections for magnesium, pH, crowding or cellular occupancy.

## 9.2 What is delivered

### A coherent opening event

The headline `P_unpaired`, `ΔG_open`, per-nucleotide cost and selected seed are
stored together in one `OpeningObservation`. This prevents a report from
combining a local probability, a global energy and a seed from a third protocol
as though they described one physical event.

Bounds and failures remain distinguishable. A zero-hit sample is an upper
bound, an underflow is censored, a skipped calculation is missing, and a
backend exception is failed. None is silently converted to numeric zero.

### Explicit recognition and conditions

`RecognitionSpec` records binder class, partner description, chemistry, seed
placement, orientation and intended endpoint. `ConditionSpec` records
temperature, sodium, potassium, magnesium, pH, preparation, exposure time,
partner concentration, crowding and cellular context.

Temperature and sodium are checked against folding settings. Fields not
implemented by a secondary-structure adapter remain explicitly unsupported.
For complementary recognition, fixed/listed seed coordinates also constrain
which scan windows are eligible.

### Validated probing and evidence

SHAPE/DMS tracks validate coordinates, optional base identities, duplicates,
finite values, target hash, source hash, condition and conversion provenance.
Compatible local, global and visualization paths receive the same track. DMS
requires an explicit conversion rather than silently assuming that a SHAPE
mapping is valid.

Versioned JSON evidence tracks support probing, contacts, protein interaction,
ribosome, modification, variant, direct-hybridization and custom annotations.
Overlapping records are labeled as condition-matched, different-condition or
unverified. They annotate the structural result; they do not invent an
occupancy penalty or change the structural rank.

### Protocol honesty

Every adapter records which requested settings it applied, deliberately
ignored because they are irrelevant to its quantity, or could not support.
A probability from a materially incompatible protocol remains visible as a
raw diagnostic but cannot enter the compatible consensus.

Local and global pair-span controls are separate. The protocol signature
records both, for example `L150/W200/GLall`: local span 150, local window 200,
and unrestricted global folds.

### Evidence lineage and estimand separation

The two RNAplfold interfaces share one calculation group. Vienna exact,
RNAfold and ensemble sampling share the global ViennaRNA partition-function
family. RNAstructure Partition and ProbKnot share a software/parameter family.

The consensus also separates physical probabilities from learned posteriors,
sequence propensities and one-structure calls. Alternative quantities are
retained in the report rather than being averaged into a number they do not
mean.

### Auditable ranking

The result is named `heuristic_rank_score`. It uses at most four criteria:
seed joint accessibility, full-site opening cost per nucleotide, model-setting
spread and footprint-length spread. It reports every input desirability,
weight, missing metric and coverage.

For non-complementary recognition classes, the seed criterion is removed.
Full-site probability is not scored again because it is the thermodynamic
transform of the opening energy already represented in the score.

### G-quadruplex safety

G4Hunter is kept as a signed G-rich/C-rich sequence-propensity diagnostic.
Where a backend cannot enforce a joint “unpaired and not occupied by G4” event,
the G4-aware probability is refused rather than overstated. A motif warning is
not presented as a corrected occupancy probability.

## 9.3 Architecture of safe extensions

| Concern | Current component | Extension rule |
|---|---|---|
| target identity and coordinates | `core/sequence.py` | preserve hashes and one-based inclusive intervals |
| physical and experimental declarations | `core/model.py` | distinguish declared, applied and unsupported fields |
| result vocabulary | `core/result.py` | add a new estimand rather than reuse a misleading field |
| tool integration | `adapters/` | declare capability, lineage, algorithm and protocol |
| orchestration | `pipeline/run.py` | keep screening, deep evaluation and optional sweeps separate |
| aggregation and rank | `pipeline/score.py` | pool only compatible like quantities |
| reports | `io/` and `viz/` | expose raw evidence and missingness, not just a headline |

An extension should fail visibly when it cannot answer the requested event.
It should not silently fall back to a related but different question.

## 9.4 Roadmap

### P4: optional partner-interaction analysis

This would be a separate command and output layer, not a hidden addition to
the structural rank. A defensible implementation must define target and
partner opening terms separately; state chemistry and orientation; preserve
the interaction model's initiation and loop terms; include concentrations
before claiming occupancy; and benchmark against direct hybridization data.

Candidate engines could include IntaRNA- or RNAup-like models, but choosing an
engine is secondary to defining the event and validation dataset.

### P5: empirical endpoint calibration

The current weights are hypotheses. Calibration requires a declared endpoint
such as fraction bound after a fixed incubation, repression, cleavage or
toehold output. Training and test splits must separate related transcripts and
overlapping windows to avoid leakage.

At minimum, compare a learned model against simple baselines such as
`ΔG_open`, seed accessibility and sequence composition. A model trained for
one assay and condition must not be relabeled as universal accessibility.

### P6: isoforms, haplotypes and cellular evidence

Generic evidence tracks already preserve annotations. A deeper implementation
would enumerate actual transcript isoforms and phased variants, score each
complete sequence, and combine results only under an explicit abundance model.
Protein and ribosome occupancy need matched experiments and should not receive
universal penalties.

### Research: kinetics and three-dimensional simulation

Kinwalker currently supplies one short-construct co-transcriptional diagnostic.
A broader kinetic module needs an explicit path ensemble, barriers, timescale
mapping and kinetic experimental validation.

Coarse-grained molecular dynamics may describe solvent exposure and tertiary
occlusion for a selected construct, but it requires validated starting
structures, force fields, ions, restraints, replicas and convergence analysis.
An exposure threshold would be model-specific, not a universal `f_available`.

## 9.5 Evidence required for any new scored feature

Before a feature changes the default rank, document:

1. the physical or experimental quantity it estimates;
2. its units, direction and numerical failure states;
3. which existing features carry the same information;
4. condition and chemistry compatibility;
5. independence or shared lineage with existing tools;
6. held-out evidence that it improves the declared decision;
7. behavior when the value is missing;
8. how the report explains the feature to a non-specialist.

Pseudoknot fraction, G4 propensity, per-base accessibility, entropy,
riboSNitch spread and biological annotations are currently diagnostic because
no universal mapping from those values to target success has been validated.
Their exclusion from the score is an accuracy feature, not an omission.

## 9.6 Reproducibility checklist

A publishable or design-critical run should preserve:

- full expressed target sequence and SHA-256;
- transcript/isoform and molecule type;
- exact one-based target intervals and physical binder footprint;
- recognition event and allowed seed placement;
- temperature, salt and all recorded condition fields;
- probing/evidence source, conversion and condition identity;
- protocol signature and tool versions;
- raw results, exclusions, bounds, failures and warnings;
- score components and coverage;
- package/source revision when available;
- experimental validation plan.

`--save-run` records most computational items in the run directory. It cannot
record biological facts that were never declared.

## 9.7 Test strategy

The test suite emphasizes scientific semantics: coordinate conversion,
sequence validation, `P`/`ΔG` transform consistency, RNAplfold parity,
local/global scope separation, conditioning and protocol exclusion,
de-duplication, estimand gating, sampling bounds, nonfinite states, G4 refusal,
pseudoknot diagnostics, recognition-aware seed placement and report round
trips.

Future biological validation should deliberately include exposed, buried,
model-disagreement, context-sensitive and variant-sensitive candidates rather
than testing only the top-ranked sites.

**Next:** [mathematical and chemical foundations](10-mathematical-and-chemical-foundations.md).
