# 4. The tools

Twelve adapters collectively assess one molecule. Some provide direct joint
opening estimates; others provide per-base, single-structure, kinetic, or
sequence-propensity diagnostics needed to interpret them. They report into the
shared metric vocabulary ([3.3](03-architecture.md#33-the-metric-vocabulary)).

`rnavail tools` prints what is installed here, what is missing, and how to
get it.

**How to read this page.** A tool, engine, or library is the scientific
software doing a calculation. An adapter is the `rnavail` connector that
supplies inputs, reads outputs, records capabilities, and translates the result
into shared fields. The table is not a ballot: some engines calculate joint
accessibility; others deliberately provide warnings or different evidence.

---

## 4.1 Why twelve and not one

If they all agreed, one would do. They do not, and the disagreement is the
point.

Secondary-structure prediction has real, known error rates. The adapters
therefore expose distinct algorithms, parameterisations, and diagnostics, but
they are not all independent evidence. In particular, the RNAplfold bindings
and CLI are an integration-parity pair, and the global ViennaRNA adapters
share one partition-function model family. The report keeps that lineage so
agreement can be read as a model check where appropriate and disagreement as
model sensitivity rather than as a vote count.

Three of the twelve exist specifically to see things the others *cannot
represent at all* — pseudoknots, quadruplexes, and kinetic traps. Their
disagreement is not noise; it is the only signal available for a whole class
of structure.

---

## 4.2 At a glance

| Adapter | Tier | Cost | Estimand | Independence group | Core contribution |
|---|---|---|---|---|---|
| `rnaplfold` | accessibility | 1 | probability | `vienna-rnaplfold` | the workhorse: local windowed accessibility, the only thing that scales to a transcript |
| `rnaplfold-cli` | accessibility | 2 | probability | `vienna-rnaplfold` | the stock binary, as a check that we drive the bindings correctly |
| `vienna-exact` | accessibility | 3 | probability | `vienna-global-pf` | constrained global partition function for joint opening under the selected ViennaRNA model |
| `gquad-scan` | accessibility | 1 | sequence propensity | own | signed G-rich/C-rich composition diagnostic; positive G-rich peaks flag possible G-quadruplex formation |
| `rnafold` | structure | 2 | probability | `vienna-global-pf` | global ViennaRNA partition function: MFE, ensemble energy, positional entropy |
| `contrafold` | structure | 2 | **posterior** | own | a *learned* model rather than a thermodynamic one |
| `eternafold` | structure | 2 | **posterior** | own | CONTRAfold's model class, retrained on ~1M chemical-mapping measurements — a second, differently-trained learned model |
| `linearfold` | structure | 1 | **single structure** | own | linear-time whole-transcript fold, catches long-range burial |
| `ensemble-sample` | structure | 3 | Monte Carlo probability | `vienna-global-pf` | Monte Carlo/state-population check of the global ViennaRNA ensemble; diagnostic when an exact PF value is present |
| `rnastructure-partition` | structure | 3 | probability | `rnastructure` | an independent codebase and parameter set |
| `probknot` | structure | 3 | **single structure** | `rnastructure` | **pseudoknot-capable** — the one adapter not restricted to nested structure |
| `kinwalker` | structure | 3 | **single structure** | own | **co-transcriptional folding** — does the site get trapped shut while being made |

*Tier* orders execution (accessibility before structure). *Cost* is a rough
runtime class, filterable with `--max-cost`. *Estimand* and *independence
group* control how the consensus combines them
([5.1](05-consensus-and-scoring.md#51-four-gates-before-any-averaging)).

### Plain-language role and advantage of every adapter

| Adapter | What it does | Main advantage | How its result is used |
|---|---|---|---|
| `rnaplfold` | asks whether short intervals are open inside moving local neighborhoods | scores an entire transcript in one pass | screening, seeds, profile and length landscape |
| `rnaplfold-cli` | runs the same method through the official executable | detects integration/parsing errors | parity check; grouped with `rnaplfold`, never a second vote |
| `vienna-exact` | compares the whole-RNA ensemble with and without an interval forced open | direct joint-event energy under the global ViennaRNA model | preferred coherent headline observation when compatible |
| `gquad-scan` | searches the sequence for G-rich quadruplex propensity | sees a non-standard motif ordinary pair matrices omit | warning only; not a corrected probability |
| `rnafold` | computes whole-RNA MFE and ensemble descriptors | gives global structural context and uncertainty | per-base/global diagnostics in the shared Vienna family |
| `ensemble-sample` | draws structures from the global Boltzmann ensemble | reveals exposed/partial/buried populations | numerical and state check; bounds rare events honestly |
| `rnastructure-partition` | computes probabilities with a separate implementation and parameters | strongest independent thermodynamic cross-check | compatible per-base consensus and disagreement detection |
| `contrafold` | predicts pairing with a learned statistical model | tests a different model class | posterior diagnostic, never converted into physical `ΔG` |
| `eternafold` | runs the CONTRAfold model class with measurement-trained parameters | tests training informed by large chemical-mapping data | separate learned posterior diagnostic |
| `linearfold` | predicts one whole-transcript structure with a linear-time beam search | fast long-range burial check | single-structure warning, not an ensemble probability |
| `probknot` | predicts one structure while allowing crossing pairs | detects pseudoknots missed by nested models | warning that other accessibility estimates may be optimistic |
| `kinwalker` | follows one folding path as the RNA chain grows | detects possible co-transcriptional traps | short-construct kinetic warning; refuses long inputs |

“Used in the report” does not always mean “used in the rank.” The score uses
four defined structural criteria; specialist tools often change the warning
you act on rather than the arithmetic. See [5.4](05-consensus-and-scoring.md#54-what-is-scored-and-what-is-only-reported).

---

## 4.3 The accessibility tier

These compute the quantity the whole tool is organised around.

### `rnaplfold` — local sliding-window accessibility

**Algorithm.** RNAplfold slides a window of `--window-size` (default 200 nt)
along the molecule, computes a partition function within each window, and
tabulates the probability that every stretch of up to `-u` nucleotides ending
at each position is unpaired. Pairs longer than the *local*
`--max-bp-span` (default 150 nt) are never considered. This is separate from
`--global-max-bp-span`, which applies only to whole-sequence folds.

**Why it is the default screen.** One pass gives every position and every
stretch length at once. That is what makes transcript-scale screening
possible, and why `--step 1` costs nothing extra (measured: 70 windows and
698 windows both take 0.30 s on a 717 nt transcript).

**Scope caveat.** It cannot see a pair longer than `--max-bp-span`, and
independent windows do not let a base compete against the whole molecule's
ensemble. Those choices can make local and whole-sequence estimates differ;
the direction is sequence- and boundary-dependent. Read
`window_exact_gap` in [5.3](05-consensus-and-scoring.md#53-the-windowed-vs-exact-gap)
as a reported disagreement, not as a universal correction.

**Provides.** `p_unpaired`, `dg_open`, `dg_open_per_nt`, the four seed
metrics, `mean_base_unpaired`, `min_base_unpaired`.

### `rnaplfold-cli` — the same algorithm, the stock binary

**Purpose.** A check that we drive the ViennaRNA bindings correctly, not a
second opinion. The test suite asserts it agrees with `rnaplfold` to
**0.01 kcal/mol**.

**This is exactly why it shares an independence group.** Two interfaces to
one algorithm are one measurement checked twice, not two votes — and the
consensus is built to know the difference.

Both local adapters retain every permitted seed placement in regional
`seed_trials` detail and select the highest-probability available placement.
This makes a fixed, terminal, listed, or exploratory seed choice auditable
without treating a selected maximum as an unrecorded universal property.

### `vienna-exact` — global constrained partition function

**Algorithm.** Computes `dG_open` the way the definition says, by running the
partition function twice on the **whole molecule**:

```
dG_open(i,j) = G_ensemble[i..j forced unpaired] − G_ensemble[unconstrained]
P_unpaired    = exp(−dG_open / RT)
```

There is no local-window approximation or lookup table, and it works for an
interval of any length. By default the global fold has no base-pair-span cap;
set `--global-max-bp-span` only when that is an intentional global modelling
choice. This is the Raccess definition evaluated under the selected
ViennaRNA energy model, not an experimentally exact accessibility measurement.

**Cost.** One extra partition function per region — right for tens or
hundreds of shortlisted regions, wrong for a transcriptome scan. Its seed
scan is budgeted (`SEED_SCAN_BUDGET = 40`): beyond that it strides rather
than testing every placement, and says so in a warning. The report still
lists every permitted coordinate: evaluated trials carry their estimate and
budget-skipped trials are explicitly `not_evaluated`.

**How to read it.** It removes the local-window approximation while retaining
ViennaRNA's secondary-structure model and its assumptions. A disagreement
with `rnaplfold` is therefore useful evidence about scope and model
sensitivity, not proof that either number is experimentally correct. It shares
`vienna-global-pf` with `rnafold` and `ensemble-sample`, so those calculations
do not provide independent biological votes.

**G4 exception.** With `--gquad`, `vienna-exact` refuses a joint-unpaired
calculation. ViennaRNA's forced-unpaired hard constraint does not exclude a
target nucleotide from a modeled G-quadruplex, so returning `P_unpaired`
would give the wrong event. The adapter reports this as a failed calculation
instead of treating G4 bases as open.

### `gquad-scan` — quadruplex propensity, no folding at all

**Algorithm.** G4Hunter (Bedrat, Lacroix & Mergny 2016, *NAR* 44:1746). Each
base scores +1…+4 for sitting in a run of Gs (scaled by run length, capped at
4), the mirror −1…−4 for a run of Cs, and 0 otherwise; a window's score is
the mean of its per-base scores. The adapter keeps that score **signed**. A
positive peak at or above `+1.2` is flagged as possible G-quadruplex
propensity. A peak at or below `−1.2` is reported as C-rich composition; it
does not claim that an RNA i-motif is occupied.

**Why it is here.** A G-quadruplex is four runs of guanine stacked into
G-tetrads held together by *Hoogsteen* hydrogen bonds — not Watson–Crick
pairing. A positive G-rich propensity can therefore identify a closure mode
outside the nested-pair calculations. The signed C-rich result is retained so
the sequence composition is not hidden, but it is not a structural call.

**Honest about what it is.** A cheap sequence heuristic, not a folding
calculation. It flags *where* a quadruplex could form, regardless of what the
partition function says about that position. Validated here against the human
telomeric repeat, which scores 2.04.

**Always available** — pure Python, no external binary.

---

## 4.4 The structure tier

These fold the whole molecule and describe it, providing cross-checks and
kinds of structure the accessibility tier cannot see.

### `rnafold` — the global partition function

The standard whole-molecule ViennaRNA calculation: minimum free energy
structure, ensemble free energy, the gap between them, mean base-pair
distance, per-base pairing probabilities and positional entropy. The general
structural picture the per-base diagnostics come from.

### `ensemble-sample` — Boltzmann sampling, the Sfold strategy

**Algorithm.** Stochastic backtracking draws structures from the Boltzmann
distribution. The fraction of samples in which the target interval is
*completely* unpaired is an unbiased Monte Carlo estimate of `P_unpaired` —
sampling the same global ViennaRNA partition-function model used by
`vienna-exact` and `rnafold`. It is a numerical and state-inspection check,
not an independent biological replicate. Its `monte_carlo_probability`
estimand stays visible but does not average into an exact
`probability`-estimand value from that same ensemble; it is the compatible
fallback only when sampling is the sole requested estimate.

**What it does that they cannot.** It reports *how* a region is buried,
classifying sampled structures into **exposed / partly exposed / buried**
populations rather than collapsing to one mean.

**Its honest weakness, reported rather than hidden.** Rare events. When a
region is open one sample in a million, no feasible number of draws will
estimate it. Whenever zero samples land in the exposed state the adapter
reports the exact one-sided 95% binomial upper bound
`1 − 0.05^(1/N)` instead of a point estimate, warns, and points you at the
global constrained calculation.

That refusal is retained as a raw upper-bound diagnostic rather than being
turned into a zero probability. When an exact global PF result is present, the
sampling row does not change that primary value. If sampling is the sole
compatible estimate, a zero-hit bound can still leave candidates with
different primary evidence coverage; `_diagnose_run()` flags that general
dropout case
([2.11](02-pipeline.md#211-step-11-diagnose-the-run-as-a-whole)).

**Reproducible by default** (fixed RNG seed); `--sampling-seed` draws a fresh
Monte Carlo ensemble from the same model.

### `rnastructure-partition` — an independent codebase

Everything else in the thermodynamic tier is ViennaRNA underneath, so those
tools agree with each other partly by construction. RNAstructure is a
**separate implementation with its own parameter tables and its own
recursions**, which makes it the most informative cross-check available: where
it and ViennaRNA disagree about a site, that site is genuinely
model-dependent. Asserted in the test suite to agree on per-base pairing to
**< 0.15**.

### `contrafold` — a learned model, deliberately not thermodynamic

**Algorithm.** CONTRAfold scores structures with a discriminatively trained
conditional log-linear model instead of measured nearest-neighbour free
energies. It is the only genuinely different *model class* in the pipeline.

**Its value is disagreement.** A site both the thermodynamic tools and
CONTRAfold call accessible is more credible than one where they split.

**What it deliberately does not do.** Its posteriors are *not* free energies,
and the adapter refuses to convert them into a `dG_open` — that would dress a
machine-learning confidence up as thermodynamic work. It is marked
`estimand="posterior"` so the consensus never averages it in with genuine
probabilities.

### `eternafold` — the same model class, retrained on measurement

**Algorithm.** Literally the same CONTRAfold inference engine as the
adapter above, run under a different trained parameter set: EternaFold
(Wayment-Steele et al. 2022) fits the identical model class by multitask
learning across roughly a million Eterna crowdsourced SHAPE/DMS
measurements, rather than CONTRAfold's original CRW-alignment training data.

**Why it is not a duplicate of `contrafold`.** Same recursion, different
training data — the thing that makes two tools count as independent evidence
here is not the code path but what shaped the parameters. It is registered
under its own `independence_group`, so a site where `contrafold` and
`eternafold` disagree is flagged the same way a disagreement between two
unrelated tools is, not silently averaged away as "the same tool twice."
Their published benchmark's largest gains over stock CONTRAfold were
specifically on ensemble/accessibility tasks rather than MFE structure — the
quantity this pipeline ranks candidates on.

**What it deliberately does not do.** Same caveat as `contrafold`: posteriors
are a trained model's confidence, not a Boltzmann probability, so no
`dG_open` is derived from them, and `estimand="posterior"` keeps it out of
the primary per-base statistic.

### `linearfold` — linear time, for long-range burial

**Algorithm.** Beam-search folding in linear time over the full transcript.
It is a fast whole-sequence structural check for distant pairing; unlike the
global partition-function tools, it returns one approximate structure rather
than an ensemble.

**The honest tradeoff.** Beam search returns *one structure*, not an
ensemble, so pairing is binary and quantised to multiples of 1/length. Marked
`estimand="single_structure"`. A fast triage filter and long-range sanity
check; never a basis for final ranking.

### `probknot` — pseudoknots, the shared blind spot

**The problem it addresses.** Every other engine here is restricted to
**nested** secondary structure: no base pair may cross another. That is a
deliberate and almost always correct simplification — and it is exactly wrong
for a site locked by a crossing interaction. A pseudoknotted site reads as
open to all ten other tools, and to nothing else.

```
nested (every engine can represent this)     pseudoknot (only probknot)
   ((((....))))                                 ((((....[[[[))))....]]]]
   pairs nest inside one another                pairs cross
```

**Algorithm.** ProbKnot builds a structure from RNAstructure's own partition
function by iteratively pairing each base with its most probable partner,
*without* forbidding crossings. The adapter then detects genuine crossings —
pairs `(i,j)` and `(k,l)` where exactly one of `k,l` falls strictly inside
`(i,j)` — and reports `pseudoknot_paired_fraction`, the fraction of the
region locked into one.

**How to read it.** One MFE-style prediction, not an ensemble probability. Its
*disagreement* with the nested tools is the finding — when it pairs much more
of a site than the consensus, every other accessibility number for that site
may be optimistic, and a note says so.

### `kinwalker` — does the site survive being made?

**The problem it addresses.** Every other metric in this repository is an
*equilibrium* quantity. None of them ask whether equilibrium is ever reached.
RNA begins folding as soon as its 5′ end leaves the polymerase, while the 3′
end does not yet exist — and a helix that nucleates early can be
**kinetically trapped**: stable enough that the molecule never crosses the
barrier back out, even though the finished transcript's energy landscape says
a more open fold is available. Equilibrium prediction cannot see this by
construction, because it integrates over all time.

**Algorithm.** Kinwalker (Geis et al. 2008) grows the sequence one nucleotide
at a time and, at each step, folds only structure that is both locally
optimal and reachable without crossing too high an energy barrier. Output is
a trajectory of adopted structures, each tagged with the transcript length at
which it formed.

**`co_tx_trap_length`.** Growth is *not* strictly monotonic — reaching a
better structure can rearrange already-paired bases — so the trap length is
defined from the end backward: the earliest transcript length after which the
region stays in its final paired state with no further reopening, not merely
the first time it was seen paired in passing.

Validated on a real published toehold switch: the 95 nt construct's site
locks shut at transcript length 27 nt, which is exactly how a toehold switch
is designed to behave.

**Its ceiling.** Runtime explodes well before transcript lengths — measured
here at 100 nt → 7.5 s, 140 nt → 17.7 s, 150 nt → over 30 s. It refuses above
**140 nt** rather than hang a default run. It is built for a short designed
construct, not a transcript scan.

---

## 4.5 Feeding in experimental data

`--shape FILE` accepts SHAPE/DMS reactivities as `position<TAB>reactivity`
and supplies them as soft constraints to adapters that support the selected
conversion. The Python ViennaRNA adapters support `deigan`, `zarringhalam`,
and `eddy2`; the `rnaplfold-cli` adapter supports Deigan and Zarringhalam
only. Unsupported adapters stay visible as diagnostic results and are not
mixed into a probing-conditioned consensus.

For SHAPE data, omitting `--shape-method` selects Deigan's conversion. For
DMS data, a conversion must be chosen explicitly with `--shape-method`;
the program will not silently apply a SHAPE pseudoenergy mapping to DMS
reactivities. The report records the chemistry, conversion, source hash,
sequence identity, condition identifier, and coverage of the track.

This is the single best correction available to a pure thermodynamic
prediction: real measurement of which nucleotides are flexible in your actual
sample.

**Missing values stay missing.** A position with no measurement is passed
through as ViennaRNA's `-999`, not as zero. An absent measurement is not
evidence that a base is unpaired, and treating it as such would quietly
fabricate structure.

---

## 4.6 DNA targets

`--molecule dna` switches to the Mathews DNA parameter sets throughout
(`dna_mathews2004` by default). The stored alphabet stays RNA-form — the
parameter tables expect U-form input — so this changes the physics, not the
letters.

Note that `contrafold` was trained on RNA and warns that its scores are not
meaningful for a DNA target; `kinwalker` warns likewise about its
transcription kinetics.

---

**Next:** [5. Consensus and scoring](05-consensus-and-scoring.md) — how twelve
readings become one ranked number.
