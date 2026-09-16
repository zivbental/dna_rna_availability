# 10. Mathematical and chemical foundations

This page derives the quantities used by `rnavail`. It starts with an intuitive
description and then gives enough detail to review the implementation.

## 10.1 What makes RNA fold?

RNA bases form hydrogen-bonded pairs, most commonly GC and AU, with GU wobble
pairs also allowed by the default RNA model. Hydrogen bonds help determine
which partners fit, but stacking between neighboring base pairs contributes
strongly to helix stability. Loops, bulges, helix ends and unpaired nucleotides
carry energetic costs or bonuses.

Nearest-neighbor models represent a secondary structure as a sum of empirical
free-energy terms:

```text
G(structure) ≈ stacking + hairpin loops + internal loops
             + multibranch loops + dangling ends + terminal terms
```

The parameters are fitted from experiments on short molecules. Turner 2004 is
the default RNA parameter set. Alternative RNA and DNA sets can be selected;
mixing a DNA target with RNA parameters would answer the wrong chemical model,
so `ModelSettings.for_molecule()` selects a matching family.

Secondary structure records pairs, not atom positions. It therefore omits
tertiary contacts, solvent geometry, most explicit ions, proteins and steric
access in three dimensions.

## 10.2 From one fold to an ensemble

The minimum-free-energy structure is the single allowed structure with the
lowest modeled `G`. Real molecules fluctuate, so accessibility requires the
whole ensemble.

For structure `s`, its unnormalized Boltzmann weight is

```text
w(s) = exp(−G(s) / RT)
```

and the partition function is

```text
Z = Σs exp(−G(s) / RT).
```

`R` is the gas constant and `T` is absolute temperature in kelvin. The
probability of one structure is `w(s)/Z`. Dynamic-programming algorithms
compute `Z` and related probabilities without enumerating every structure,
which would be exponentially expensive.

At 37 °C (`310.15 K`), `RT` is about `0.616 kcal/mol`. Higher temperature
changes both `RT` and the parameterized free energies; it is not implemented
merely by changing the divisor in the equation.

## 10.3 Joint opening probability

For an inclusive interval `i..j`, let `Open(i,j)` be the set of structures in
which every base in that interval is unpaired. Then

```text
P_unpaired(i,j)
  = Σ[s in Open(i,j)] exp(−G(s)/RT) / Z.
```

This is a **joint event**. It is not

```text
(1 / length) Σk P(base k is unpaired).
```

The latter is a marginal average. It can be useful for locating flexible
bases, but it cannot say that an entire footprint is available simultaneously.

## 10.4 Opening free energy

The same joint probability is expressed as a reversible free-energy penalty:

```text
ΔG_open(i,j) = −RT ln P_unpaired(i,j).
```

The transform is monotonic: high probability means low opening cost. For
example at 37 °C:

| `P_unpaired` | `ΔG_open` | Interpretation within the model |
|---:|---:|---|
| 0.9 | 0.065 kcal/mol | almost always open |
| 0.1 | 1.42 kcal/mol | often accessible |
| 0.001 | 4.26 kcal/mol | rarely pre-open |
| 10⁻⁶ | 8.51 kcal/mol | extremely rarely pre-open |

`ΔG_open / length` is useful when comparing different footprint lengths, but
it does not make length irrelevant: a binder still requires its actual
physical footprint, and interval boundaries can cross different helices.

### How `vienna-exact` calculates it

The global adapter evaluates the whole-molecule partition function twice:

```text
G0 = −RT ln Z0                         unconstrained ensemble
G1 = −RT ln Z1                         interval forced unpaired
ΔG_open = G1 − G0 = −RT ln(Z1/Z0)
P_unpaired = Z1/Z0.
```

Keeping `P` and `ΔG` in one `OpeningObservation` prevents aggregation from
creating a probability from one protocol and an energy from another.

### How RNAplfold approximates it

RNAplfold repeatedly considers a local window and limits the largest allowed
pair span. It computes a table indexed by interval end and length. This makes
all transcript positions affordable in one pass, but it omits competition
with sequence outside the local context and cannot form a pair longer than
the selected local span. The sign of the difference from a whole-RNA result
is sequence-dependent; it is reported rather than “corrected” by a universal
offset.

## 10.5 Seeds and nucleation

A complementary strand does not necessarily wait for its full final footprint
to be pre-open. A shorter exposed segment can pair first and then extend while
displacing structure. `rnavail` therefore records two distinct events:

```text
full-site event: every base of the final footprint is unpaired
seed event:      one permitted shorter subinterval is unpaired
```

With `seed_mode=any`, the best permitted placement is selected but every
tested placement remains in the JSON provenance. Fixed, terminal or listed
placement modes represent mechanisms that cannot nucleate everywhere.

Seed openness alone does not calculate hybridization energy, strand-
displacement rate or final occupancy. It says only that a plausible starting
patch exists in the target's self-structure.

## 10.6 Base-pair probabilities and entropy

Partition-function tools can calculate `p(k,l)`, the probability that bases
`k` and `l` pair. Per-base unpaired probability is

```text
u(k) = 1 − Σl p(k,l).
```

The base-pair heatmap in the HTML report visualizes `p(k,l)`. Bright cells
identify likely partners; several competing bands indicate alternative folds.

Positional Shannon entropy summarizes how dispersed the pairing choices are.
For a discrete set of states with probabilities `p_a`,

```text
H = −Σa p_a log2(p_a).
```

Higher entropy means the model distributes probability across more alternatives.
It is not automatically “better”: flexibility can help exposure, but it can
also mean an uncertain structural prediction. Entropy remains diagnostic.

## 10.7 Sampling and uncertainty

Boltzmann sampling draws structures from the modeled ensemble. If `x` of `N`
draws contain the fully open interval, `x/N` estimates its probability.
Sampling is useful for inspecting populations, but rare events require many
draws. When `x=0`, the program does not claim the probability is zero. It
reports the one-sided 95% upper bound

```text
P < 1 − 0.05^(1/N).
```

For `N=2000`, that bound is about `0.0015`. The constrained partition function
can resolve much rarer events without waiting to observe them in samples.

## 10.8 Consensus mathematics

Before summarizing a metric, `rnavail` asks four questions:

1. Are these separate calculations, or two interfaces to the same algorithm?
2. Are they estimating the same kind of quantity?
3. Were they conditioned on the same probing data?
4. Did they implement the materially requested protocol settings?

Within each declared calculation group, eligible values are averaged. The
median and range are then calculated across groups. The median resists one
extreme implementation; the range is deliberately retained because local vs.
global or ViennaRNA vs. RNAstructure disagreement is scientific information.

Learned posteriors and single-structure calls are not mixed into a physical
probability. They stay visible as alternative-model diagnostics.

## 10.9 Ranking mathematics

Each available scoring metric is converted to a desirability `d` between 0
and 1 using fixed anchors:

| Criterion | Weight | Bad → good | Mapping |
|---|---:|---:|---|
| seed joint probability | 2.0 | `10⁻⁴ → 0.5` | linear in `log10(P)` |
| opening cost per nt | 1.5 | `1.0 → 0.05` kcal/mol/nt | linear |
| model-setting spread | 0.75 | `4.0 → 0.5` kcal/mol | linear |
| footprint-length spread | 0.75 | `0.15 → 0.01` kcal/mol/nt | linear |

Values beyond the anchors are clamped to 0 or 1. The score is the weighted
geometric mean

```text
score = exp(Σi wi ln(di) / Σi wi).
```

The geometric mean represents an “and” decision: an excellent seed should not
fully hide a disastrous opening cost or severe instability. A zero
desirability makes the combined score zero.

Missing optional criteria are omitted, not treated as failure. Coverage is

```text
coverage = Σ weights present / Σ weights intended.
```

For non-complementary recognition classes, seed criteria are removed because
their mechanism has not been justified. `P_unpaired` itself is not scored in
addition to `ΔG_open/nt`, because at fixed interval and temperature it is the
same observation under a deterministic transform; scoring both would count
one fact twice.

The anchors and weights are uncalibrated design heuristics. They preserve an
auditable order; they do not define a probability of experimental success.

## 10.10 Chemical conditions and probing

### Salt and ions

Electrostatic repulsion between negatively charged phosphate groups makes ion
conditions important. Compatible ViennaRNA paths can apply the declared
monovalent-salt setting. Potassium and magnesium fields are recorded, but the
current secondary-structure layer does not convert them into a general
condition-specific correction. Magnesium can stabilize tertiary contacts and
pseudoknots, so recording it is not equivalent to modeling it.

### SHAPE and DMS

Chemical probing reactivity is an experimental observable, not directly an
unpaired probability. A declared conversion adds pseudoenergy or soft
constraints that bias compatible folding calculations toward structures
consistent with the measurements. Different chemistries react through
different mechanisms, so DMS requires an explicit conversion choice rather
than silently inheriting a SHAPE rule.

Input positions, optional base identities, finite values, duplicates,
sequence hashes, conversion parameters and condition identity are validated
and preserved. Tools unable to apply the requested conditioning remain raw
diagnostics and are excluded from the conditioned consensus.

### What the model still omits

The calculation does not represent protein occupancy, translating ribosomes,
partner concentration, molecular crowding, most pH effects, tertiary geometry
or cellular remodeling. See [limitations](07-limitations.md).

**Back to:** [the reading guide](00-reading-guide.md).
