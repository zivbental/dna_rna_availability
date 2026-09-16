# rnavail

**Is this stretch of RNA actually available for something to bind to?**

Being present in the sequence is not the same as being available. A stretch
of RNA can be right there in the sequence and still be permanently stuck to
another part of the same molecule — folded shut, and useless as a target.
`rnavail` estimates a target region's single-molecule self-accessibility under
a declared folding protocol. It preserves the model family, sequence scope,
conditioning, and adapter capabilities behind each result, so shared
calculations are not mistaken for independent evidence.

```bash
rnavail scan transcript.fa --window 25 --keep 25 --save-run
```

To carry condition-linked experimental annotations alongside a structural run,
use a versioned JSON evidence track. It is shown with matching status in the
report and does not alter the uncalibrated structural rank.

```bash
rnavail evaluate transcript.fa --region 205-224 --condition-id buffer-A \
  --evidence eclip.json --json report.json
```

The track format and its sequence-hash requirement are documented in the
[implementation status](docs/09-rna-accessibility-implementation-proposal.md#validated-probing-and-evidence).

```
      region      len     rank    seedP    P_unp   dGopen    dG/nt
        w205       20    1.000    0.975    0.934     0.04     0.00
        w357       20    0.953    0.335    0.025     2.47     0.12
         w11       20    0.952    0.427 8.52e-03     3.08     0.15
```

---

## Documentation

To benchmark the current RNA availability ranking across PARS, DMS-seq,
icSHAPE and SHAPE-MaP experiments, see the
[multi-dataset run guide](validation/multi_dataset/README.md). It includes
download/preparation commands, parallel execution, resume support and per-RNA reports.

The documentation is written in layers. Start with the reading guide if RNA
folding is new to you; each technical page begins with a plain-language answer
and then develops the chemistry, mathematics, algorithm and implementation.

| | |
|---|---|
| **[0. Reading guide and glossary](docs/00-reading-guide.md)** | Where to start, a map of the repository, and definitions of the terms used throughout. |
| **[1. The question](docs/01-the-question.md)** | What "available" means, why it is not obvious, and the mistake this tool exists to prevent. *No biology assumed.* |
| **[2. How it works](docs/02-pipeline.md)** | Top-down walk through every step, from FASTA in to ranked list out — what each does, why, and the algorithm behind it. |
| **[3. Architecture](docs/03-architecture.md)** | The components, the data structures, and how they connect. |
| **[4. The tools](docs/04-tools.md)** | All twelve prediction engines: what each computes, and what each is blind to. |
| **[5. Consensus and scoring](docs/05-consensus-and-scoring.md)** | How compatible readings become a heuristic rank — and why only four metrics feed it. |
| **[6. Reading the output](docs/06-outputs.md)** | Every output file, and a worked example of interpreting a real report. |
| **[7. Limitations](docs/07-limitations.md)** | What this cannot tell you. Read before trusting a number. |
| **[8. Literature review](docs/08-rna-accessibility-literature-review.md)** | Evidence for further constraints: binding pathways, kinetics, tertiary structure, solution conditions, cellular context and assay interpretation. |
| **[9. Status and roadmap](docs/09-rna-accessibility-implementation-proposal.md)** | What is implemented now, what remains outside scope, and the evidence required for extensions. |
| **[10. Mathematical and chemical foundations](docs/10-mathematical-and-chemical-foundations.md)** | The deeper derivations: ensembles, partition functions, opening free energy, salt, probing constraints, sampling uncertainty and score transforms. |
| **[11. Command reference](docs/11-command-reference.md)** | Current commands, defaults, common recipes, and which options are modeled versus recorded only. |

---

## The one idea to take away

The quantity everything is organised around is the probability that a target
interval is **simultaneously** unpaired:

```
P_unpaired(i,j)     and its opening penalty     dG_open = −RT · ln P_unpaired
```

That is deliberately **not** the average of per-nucleotide unpaired
probabilities. On this repository's own test molecule, region 9–20 averages
**0.81** unpaired per base but its joint probability is **0.00026** — those
nucleotides are open at different times, not together.

The full-footprint joint quantity answers the strict event in which an entire
target must be open *at once*. Complementary strands can instead initiate
through a shorter declared seed; `rnavail` records that event separately when
the recognition mechanism supports it. Neither event can be replaced by an
average of per-base probabilities. `rnavail` reports the marginal value only
as a diagnostic and prints an explicit note whenever it diverges from joint
accessibility.

See [1. The question](docs/01-the-question.md) for the full explanation.

---

## Install

```bash
python3 -m venv .venv && .venv/bin/pip install -e .   # core + ViennaRNA
bash tools/install_tools.sh                            # external CLI tools
```

`install_tools.sh` drops a self-contained micromamba environment in `.tools/`
(several GB; delete with `rm -rf .tools`) holding RNAstructure, CONTRAfold,
LinearFold, kinwalker and the ViennaRNA command-line suite.

Everything degrades gracefully without it — adapters report themselves
unavailable with a fix hint rather than failing the run — and `gquad-scan`
needs none of it.

```bash
rnavail tools        # what is installed, what is missing, how to get it
pip install -e .[viz]   # matplotlib, for the visual reports
```

---

## Quick start

```bash
# "I don't know where to look" — tile the transcript and rank every window
rnavail scan transcript.fa --window 25 --keep 25 --save-run

# "I know where to look" — characterise specific regions in depth
rnavail evaluate transcript.fa --region 205-224 --region loop:117-136 -v

# a region can also be given as the literal subsequence
rnavail evaluate transcript.fa --region AAUCAAACAAAUCAAACAAA

# ask how much to trust the answer (all four sweeps, all opt-in)
rnavail scan transcript.fa --window 20 --keep 10 \
        --robustness --length-robustness --ribosnitch --context-robustness
```

`--save-run` writes a timestamped `runs/<timestamp>[-tag]/` containing the
text, JSON, TSV, per-position profile and HTML reports plus a `meta.json`
recording exactly what was run. `runs/latest` always points at the most
recent.

### Choosing `--window`

The window length is a statement about **what will bind there**, not a tuning
knob — read it off your binder's footprint:

| Binder | Footprint |
|---|---|
| microRNA seed | 6–8 nt |
| antisense oligo | 15–25 nt |
| sgRNA spacer | 20 nt |
| toehold trigger | 20–30 nt |

The current CLI default is 25 nt and the default shortlist is 25 candidates.
Those defaults are convenient starting points, not biological constants. The
choice matters: on a real GFP transcript the top-15 sites at window
length 8 and at length 20 shared **exactly one site**. Use
`--length-robustness` to check whether a candidate survives nearby choices.

---

## What's inside

Twelve adapters collectively provide joint-opening estimates, structural
diagnostics, and integration checks. They are not twelve independent biological votes: the
local RNAplfold bindings and CLI are a parity pair, while ViennaRNA global
partition-function calculations and sampling share one model family.

| | |
|---|---|
| **Accessibility** | `rnaplfold` · `rnaplfold-cli` · `vienna-exact` · `gquad-scan` |
| **Structure** | `rnafold` · `ensemble-sample` · `rnastructure-partition` · `contrafold` · `eternafold` · `linearfold` · `probknot` · `kinwalker` |

Three of them exist to see things the others *cannot represent at all*:
`probknot` (pseudoknots), `gquad-scan` (G-quadruplexes) and `kinwalker`
(kinetic traps during transcription). Full descriptions in
[4. The tools](docs/04-tools.md).

Experimental SHAPE/DMS data can be supplied with `--shape`; recognition,
condition, and probing provenance are written into every report. DNA targets
use `--molecule dna` for target self-folding only.

---

## What it deliberately does not do

**`rnavail` answers a single-molecule question.** It does not predict whether
one RNA binds another — that is a separate, much harder problem and is not a
current adapter layer.

An open site is **necessary, not sufficient**. A top-ranked candidate here is
a shortlist entry, not a validated design.

It records magnesium, pH, crowding, preparation, partner concentration, and
cellular context when declared, but the target-RNA secondary-structure layer
does not model those effects. Compatible adapters apply temperature and the
declared monovalent salt setting; it does not model RNA-binding proteins,
ribosomes, 3D structure, interaction energetics, or cellular binding. See
[7. Limitations](docs/07-limitations.md) before trusting any number here.

---

## Tests

```bash
.venv/bin/python -m pytest -q
```

The scientifically meaningful checks compare compatible calculations and
known model boundaries — local versus global ViennaRNA under matched scope,
the RNAplfold bindings versus CLI, and ViennaRNA versus RNAstructure
per-base pairing — so a regression surfaces as a failing test rather than a
plausible-looking number.

---

## Background

This implements the accessibility tiers described in
[`RNA_Target_Region_Accessibility_Katzir_CGMD.md`](RNA_Target_Region_Accessibility_Katzir_CGMD.md),
the source research document for the project. The interaction, gate-design
and molecular-dynamics tiers that document also describes are out of scope
here by design.
