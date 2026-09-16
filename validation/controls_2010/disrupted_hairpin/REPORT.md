# disrupted_hairpin

Stem-disruption control: replace the opposing GC arm with 20 A bases, preserving length and the tested arm. Residual folding within the GC arm is possible, so complete opening is not guaranteed; the expectation is increased accessibility relative to the intact hairpin.

RNA, Turner 2004, 37 °C, dangles=2, unrestricted global pairing. Local window and pair span equal the full transcript length for a matched-scope comparison. Experimental buffer/temperature are not asserted to match this computational protocol. Magnesium, tertiary contacts, proteins and cellular binding are not modeled. No experimental data constrain any prediction. All coordinates are one-based and inclusive.

| Site | Coordinates | Sequence | Joint P(open), global exact | Opening cost (kcal/mol) |
| --- | --- | --- | --- | --- |
| same_site_8nt | 5–12 | GCGCGCGC | 1.04986e-08 | 11.3233 |
| same_site_20nt | 1–20 | GCGCGCGCGCGCGCGCGCGC | 1.07337e-13 | 18.4054 |


| Adapter | Site | Joint P(open) | Mean per-base P(unpaired), distinct diagnostic |
| --- | --- | --- | --- |
| rnaplfold | same_site_8nt | 1.04952e-08 | 0.500223 |
| rnaplfold | same_site_20nt | 1.07282e-13 | 0.20092 |
| rnaplfold-cli | same_site_8nt | 1.04952e-08 | not provided |
| rnaplfold-cli | same_site_20nt | 1.07282e-13 | not provided |
| vienna-exact | same_site_8nt | 1.04986e-08 | not provided |
| vienna-exact | same_site_20nt | 1.07337e-13 | not provided |
| rnafold | same_site_8nt | not provided | 0.500223 |
| rnafold | same_site_20nt | not provided | 0.20092 |
| ensemble-sample | same_site_8nt | not provided | 0.5002 |
| ensemble-sample | same_site_20nt | not provided | 0.20076 |
| rnastructure-partition | same_site_8nt | not provided | 0.499928 |
| rnastructure-partition | same_site_20nt | not provided | 0.201288 |
| contrafold | same_site_8nt | not provided | 0.044135 |
| contrafold | same_site_20nt | not provided | 0.0639285 |
| eternafold | same_site_8nt | not provided | 0.0269971 |
| eternafold | same_site_20nt | not provided | 0.0491818 |


The heuristic rank is not used as a pass/fail criterion. Compare probabilities and opening costs under the same scope and footprint.


The disrupted construct remains mostly closed: removing an opposing arm does not make this repetitive GC sequence unstructured. Its GC arm can form a shorter hairpin within itself. This is a directional perturbation control, not a positive open control; use open_AC or the A-only loop for the positive control.


| Temperature °C | Site | Joint P(open) | Opening cost |
| --- | --- | --- | --- |
| 25 | same_site_8nt | 5.43786e-10 | 12.6392 |
| 25 | same_site_20nt | 3.01112e-16 | 21.1748 |
| 37 | same_site_8nt | 1.04986e-08 | 11.3233 |
| 37 | same_site_20nt | 1.07337e-13 | 18.4054 |
| 50 | same_site_8nt | 2.12246e-07 | 9.8672 |
| 50 | same_site_20nt | 3.79942e-11 | 15.4078 |


| Adapter | Status | Version | Error |
| --- | --- | --- | --- |
| rnaplfold | ok | ViennaRNA 2.7.2 | — |
| rnaplfold-cli | ok | RNAplfold 2.4.7 | — |
| vienna-exact | ok | ViennaRNA 2.7.2 | — |
| rnafold | ok | ViennaRNA 2.7.2 | — |
| ensemble-sample | ok | ViennaRNA 2.7.2 | — |
| rnastructure-partition | ok | partition: Version 6.6 (April 2, 2026). | — |
| contrafold | ok | CONTRAfold | — |
| eternafold | ok | EternaFoldParams.v1 on CONTRAfold 2.02 | — |


Elapsed run time: 0.51 s. [Visual pipeline report](report.html), [full JSON](report.json), [metrics TSV](metrics.tsv), [input FASTA](target.fa). Heatmaps use the complete transcript, matching the prediction scope.
