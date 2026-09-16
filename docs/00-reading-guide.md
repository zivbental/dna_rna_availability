# 0. Reading guide and glossary

This repository answers one narrow question carefully:

> Before a binder arrives, how often is a chosen stretch of one RNA molecule
> unpaired and therefore structurally available?

It does **not** predict that binding will occur. Accessibility is one necessary
part of binding, alongside complementarity, interaction energy, concentration,
kinetics, competing molecules and the cellular environment.

## Choose a path

### I want to use the program

1. Read [the question](01-the-question.md).
2. Follow [the pipeline](02-pipeline.md).
3. Keep [the output guide](06-outputs.md) beside the generated report.
4. Read [the limitations](07-limitations.md) before selecting a design.
5. Use the [current command reference](11-command-reference.md).

### I want to understand or review the implementation

Read [architecture](03-architecture.md), [tools](04-tools.md), and
[consensus and scoring](05-consensus-and-scoring.md). The source of truth is
the code; documentation intentionally avoids fragile source line numbers.

### I want the scientific derivation

Read [mathematical and chemical foundations](10-mathematical-and-chemical-foundations.md),
then the [literature review](08-rna-accessibility-literature-review.md).

### I want to extend the project

Read the [current implementation status and roadmap](09-rna-accessibility-implementation-proposal.md).
The long [Katzir/CGMD research note](../RNA_Target_Region_Accessibility_Katzir_CGMD.md)
is historical design background, not a description of the current program.

## The program in one picture

```text
RNA sequence + intended footprint + declared conditions
                       │
                       ▼
        fast local scan of every possible location
                       │
                       ▼
          non-overlapping candidate shortlist
                       │
                       ▼
 whole-RNA confirmation + alternative-model diagnostics
                       │
                       ▼
 rank + coverage + disagreements + warnings + provenance
```

The screen is fast because RNAplfold computes a table for many intervals in
one pass. The confirmation is slower because a constrained whole-molecule
partition function is evaluated for each shortlisted interval.

## Vocabulary

| Term | Plain-language meaning | Precise meaning here |
|---|---|---|
| nucleotide, base, nt | one RNA letter | A, C, G or U; DNA uses T instead of U |
| target interval | the stretch being considered | one-based, inclusive coordinates `i..j` |
| footprint | how many bases a binder needs | the scan window length |
| base pair | two bases attached through hydrogen bonding and stacking | usually AU, GC or GU in the modeled RNA secondary structure |
| secondary structure | which bases pair with which | no three-dimensional coordinates; most engines require non-crossing pairs |
| ensemble | the RNA does not have one permanent fold | a Boltzmann-weighted distribution over allowed secondary structures |
| partition function, `Z` | the accounting total for all folds | `Z = Σs exp(−G(s)/RT)` |
| marginal probability | whether one base is unpaired | `P(base k unpaired)` |
| joint probability | whether a complete stretch is open together | `P_unpaired(i,j)` |
| opening free energy, `ΔG_open` | work needed to expose the stretch | `−RT ln P_unpaired`, in kcal/mol |
| seed | short initially exposed segment | a declared subinterval that may nucleate complementary recognition |
| estimand | the kind of quantity being estimated | probability, learned posterior, sequence propensity or one-structure state |
| model family | shared physical/statistical assumptions | used to avoid counting related calculations as independent votes |
| adapter | connector around an external library/program | translates one request into the shared result schema |
| consensus | summary of comparable readings | median and spread after compatibility and independence gates |
| heuristic rank | structural preference score | weighted geometric mean of up to four desirabilities; not a success probability |
| coverage | how much intended scoring evidence existed | present criterion weight divided by intended weight |
| conditioning | experimental information applied to folding | for example a validated SHAPE conversion |
| provenance | what produced the result | sequence hash, protocol, tool/version, settings and condition identity |

## Three distinctions to keep in mind

### One open base is not an open footprint

If each position is unpaired at different times, the average per-base value
can be high while the probability that all positions are free together is
tiny. `rnavail` reports both, but ranks with the joint-event energy rather than
substituting the average.

### A probability is not a learned confidence or a drawing

Partition-function tools report probabilities. CONTRAfold-family tools report
posteriors learned from training data. LinearFold, ProbKnot and Kinwalker
return one structure or trajectory. These results are useful together, but
they are not numerically interchangeable.

### A rank is not a biological prediction

The rank orders structural candidates under declared assumptions. A value of
`0.9` does not mean 90% binding, cleavage, repression or expression. Such a
claim would require target- and assay-specific experimental calibration.

**Next:** [1. The question](01-the-question.md).
