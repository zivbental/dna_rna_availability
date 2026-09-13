# 7. Limitations

What this tool cannot tell you, why, and what would be needed to change that.

This page is deliberately long. A prediction tool that only documents its
strengths is harder to use well than one that is explicit about where its
numbers stop meaning anything.

---

## 7.1 The one-line version

`rnavail` estimates, well and from several independent directions, **one
term** of a much larger physical picture: how open a region is within its own
molecule's equilibrium secondary structure, in dilute solution, under a
chosen temperature and monovalent-salt folding protocol.

Everything below is the rest of the picture.

---

## 7.2 Scope boundaries — deliberate, not gaps

### It does not predict whether anything binds

This is the big one. `rnavail` answers a **single-molecule** question. Given
one sequence, how open is this region within *its own* folded structure. It
does **not** predict whether a specific other RNA will bind there.

RNA–RNA interaction prediction is a separate and still largely unsolved
problem. Adapters for it — IntaRNA, RNAup, RNAduplex/RNAcofold, OligoWalk —
were built in this repository, worked, and were **removed** once the scope was
fixed to the single-molecule question. The binaries remain installed if that
layer is ever wanted back.

**The practical consequence:** an open site is *necessary, not sufficient*. A
top-ranked candidate is a shortlist entry — "physically reachable" — not a
validated design. Whether your oligo binds it, and binds it in preference to
somewhere else, is a question this tool does not attempt.

### No multi-strand / gate-state design

Equilibrium complex concentrations, ensemble defect, crosstalk across a
multi-strand gate — the design tier described in the source document — is not
implemented. That needs NUPACK, which was tried and removed because it could
not be exercised without a separate paid licence in this environment.

### No 3D, no molecular dynamics

There is no tertiary-structure or coarse-grained MD layer. A Martini 3 RNA +
GROMACS stage was prototyped and removed: it needs a 3D starting structure
(no offline predictor is bundled), the Martini 3 RNA force-field files,
GROMACS itself, and realistically GPU/HPC access. None of that is available
here.

This matters more than it sounds, because of the next item.

---

## 7.3 Physics that is simply absent

Every one of these is a real effect on real molecules that **no tool in this
repository models**.

### Magnesium

Mg²⁺ is what stabilises tertiary structure and pseudoknots. It is very
plausibly the single biggest reason a site predicted open at equilibrium is
closed in a real reaction.

ViennaRNA's salt correction is **monovalent only** (`--salt` sets Na⁺/K⁺);
RNAstructure has no divalent term either. The condition fields can record
total or free Mg²⁺, but no adapter converts those values into a folding
parameter. Empirical calibration against data collected under the same
condition remains necessary.

### pH

Protonated A⁺·C pairs, i-motifs, and pH-dependent riboswitches all exist.
Nearest-neighbour parameter tables assume one pH and never say which.

### Molecular crowding

The cytoplasm is roughly 300 g/L of macromolecule. Crowding favours compact
folded states, which generally means **less** availability than a
dilute-solution calculation predicts. Every parameter set here was fitted in
dilute solution.

### Concentration and competition

Availability at 1 nM and at 1 µM are different numbers once self-dimerisation
and competing partners are in play. Nothing here models concentration:
a competitor binding 2 kcal/mol worse at a thousandfold higher concentration
still wins, and this tool has no way to say so.

### Tertiary contacts

Kissing loops, tetraloop–receptor motifs and Mg-stabilised cores hold
nucleotides that every secondary-structure model here reports as free.
**The bias runs one way:** where tertiary structure matters, predicted
availability is too high.

### Anything protein

RNA-binding proteins occlude 6–20 nt completely. A translating ribosome
unwinds structure ahead of itself and occludes ~30 nt around itself — which,
for anything placed in a 5′UTR or CDS, can dominate every number this tool
produces. Ligands and metabolites flip riboswitch elements between folds.

None of this is visible to a thermodynamic calculation. It needs data —
eCLIP/POSTAR footprints, ribosome profiling — not a better folding program.

### Rates

Everything here except `kinwalker` is an **equilibrium** quantity. Whether a
site binds *fast enough to matter in your assay* is a separate question with
no answer in this toolchain. Toehold-mediated strand displacement spans six
orders of magnitude in rate over a few nucleotides of toehold; two sites with
identical `dG` can behave completely differently.

---

## 7.4 Known biases in what *is* modelled

These are within scope and quantified, which makes them manageable.

### Nested structure only — the pseudoknot bias

Eleven of the twelve adapters are restricted to nested secondary structure by
construction. A pseudoknotted site reads as open to all of them.

This is a **one-directional bias**: predicted availability is too high, never
too low. `probknot` exists to detect it, and a note fires when it pairs a
large fraction of a site into a crossing helix. Believe that note over the
consensus.

### Quadruplex occupancy is not available as a joint opening probability

A G-quadruplex is held together by Hoogsteen bonds between four G-runs, not
ordinary Watson–Crick pairing. `gquad-scan` is therefore a signed sequence
propensity diagnostic: a positive G-rich peak at or above `+1.2` flags a
possible G4, while a strongly negative score is labelled C-rich composition,
not RNA i-motif occupancy.

`--gquad` does not make the headline joint-unpaired probability G4-aware.
`vienna-exact` refuses the calculation because its forced-unpaired constraint
does not exclude those nucleotides from a G4. RNAplfold's local/window engine
is rejected before execution because that ViennaRNA combination can crash.
`rnafold` can still provide global ensemble and structure descriptors with
`--gquad`, but it omits per-base unpaired probabilities and positional entropy
because the base-pair matrix does not encode G4 occupancy. Treat a G4 flag as
a reason to obtain orthogonal evidence, not as a corrected accessibility
estimate.

### Windowed and whole-sequence calculations answer different approximations

`rnaplfold` folds 200-nt windows independently, so a base never competes
against the whole molecule's ensemble, and it cannot see a pair longer than
the local `--max-bp-span`. Whole-sequence calculations are unrestricted by
that local cap unless `--global-max-bp-span` is set. Differences can arise
from long-range pairing, window boundaries, and the distinct partition
functions; their sign is not a universal property of the approximation.

The report surfaces this as `window_exact_gap` rather than averaging it away.
Use it to identify candidates whose rank changes with folding scope, then
inspect the sequence, model settings, and any experimental data before
choosing which protocol is relevant to the assay.

### The scoring anchors are uncalibrated

The desirability anchors and weights are **starting points, not truths**. The
source document is explicit that they should be fitted against measured gate
performance; that fitting has not been done.

The run tells you when this bites: on a real GFP run, `p_unpaired` was pinned
at its anchor for **7 of 10** candidates, meaning that criterion did no
ranking work at all despite its nominal weight
([5.5](05-consensus-and-scoring.md#55-checks-the-run-makes-on-itself)).

### The window length is a choice, and it changes the answer

`--window` is a statement about what will bind there, not a physical
constant. On the GFP transcript, the top-15 sites at window length 8 and at
window length 20 shared **exactly one site**. `dG_open/nt` is not even
monotonic in length — it tracks which helices the boundary falls across, a
step function.

Use `--length-robustness` to see whether a candidate survives nearby,
equally defensible choices, and read the landscape plot.

### Sweep frames differ from the headline number

`--ribosnitch`, `--context-robustness` and `--length-robustness` all fold a
**±100 nt local context** to keep cost bounded, while the headline `dG_open`
folds the whole sequence. Their spreads are internally consistent with each
other but **not directly comparable in magnitude** to `dG_open`. A run using
any of them says so in its warnings.

### `kinwalker` is one path, not a rate

It simulates one plausible co-transcriptional trajectory under one barrier
heuristic. It is not an ensemble and not a rate calculation. It also refuses
above 140 nt because its runtime explodes there (measured: 100 nt → 7.5 s,
140 nt → 17.7 s, 150 nt → over 30 s), so it is usable on a designed construct
and not on a transcript.

### Sampling cannot see rare events

`ensemble-sample` reports the exact one-sided 95% binomial upper bound
`1 − 0.05^(1/N)` rather than a point estimate when a region was never sampled
fully open — correct behaviour. It stays a raw numerical diagnostic when a
compatible exact partition-function calculation is present. If sampling is
the only compatible estimate, the upper bound leaves that candidate with less
primary evidence than a sampled point estimate; this is flagged automatically.

### Non-overlapping shortlisting hides plateaus

`scan` keeps non-overlapping candidates so the top ten is not ten one-base
shifts of the same loop. The cost is that the reported boundaries are one
arbitrary slice of what may be a broad accessible region. The landscape plot
is the antidote.

---

## 7.5 Input choices that quietly change the answer

Not tool limitations — things you control, that nothing will check for you.

### Where you cut the FASTA

Every adapter folds whatever sequence it is handed, **in full**. A bare CDS
folds differently from the same CDS inside its real transcript with UTRs. On
the GFP run, `--context-robustness` found spreads up to **8.5 kcal/mol**
attributable to flanking sequence alone.

For anything you will actually build, run the full transcript as expressed —
UTRs, RBS, terminators, assembly scars and all.

### Which isoform or annotation

A site in a 5′UTR under one annotation is in an intron under another. The
fold — and therefore the availability — is a property of the transcript you
actually get.

### Sequence variants

If your target has population variation, the site you scored may not be the
site in your sample. `--ribosnitch` quantifies how much a single substitution
can move the answer; on the GFP run every top candidate was flagged, with
worst-case swings of 3.9–7.1 kcal/mol.

### Ambiguous bases

Degenerate IUPAC codes (`N`, `R`, `Y`…) fold as *unpairable*, which inflates
apparent accessibility. The input is accepted and a warning is emitted.

---

## 7.6 How to use it well anyway

Given all of the above, the tool is still useful — provided it is read as
evidence rather than as an answer.

1. **Rank, then verify.** Treat the output as a shortlist to test, never as a
   design that is done.
2. **Read the notes before the score.** The score is one number; the notes
   name specific failure modes.
3. **Prefer robust candidates over top-scoring ones.** A site that survives
   `--robustness`, `--length-robustness` and `--context-robustness` is a
   better bet than one that scores 0.02 higher and moves under perturbation.
4. **Compare whole-sequence and windowed estimates** when they disagree, and
   read `window_exact_gap` as a scope-sensitivity warning.
5. **Fold the real construct**, not a trimmed CDS.
6. **Feed in compatible probing data if you have it** (`--shape`). Keep its
   sequence and condition matched to the target, and choose a DMS conversion
   explicitly rather than borrowing a SHAPE default.
7. **Remember what is missing.** Mg²⁺, proteins, ribosomes and kinetics are
   all absent, and any of them can dominate.

---

**Back to:** [the documentation index](../README.md)
