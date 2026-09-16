# closed_hairpin

Designed negative control: a 20-bp GC stem encloses an 8-A loop. The central stem should be strongly buried; the loop provides an open site in the same molecule. This is a model control, not an experimentally measured construct.

RNA, Turner 2004, 37 °C, dangles=2, unrestricted global pairing. Local window and pair span equal the full transcript length for a matched-scope comparison. Experimental buffer/temperature are not asserted to match this computational protocol. Magnesium, tertiary contacts, proteins and cellular binding are not modeled. No experimental data constrain any prediction. All coordinates are one-based and inclusive.

| Site | Coordinates | Sequence | Joint P(open), global exact | Opening cost (kcal/mol) |
| --- | --- | --- | --- | --- |
| stem_8nt | 5–12 | GCGCGCGC | 2.52178e-19 | 26.3939 |
| stem_20nt | 1–20 | GCGCGCGCGCGCGCGCGCGC | 3.5841e-25 | 34.6921 |
| loop_8nt | 21–28 | AAAAAAAA | 1 | 0.0000 |


| Adapter | Site | Joint P(open) | Mean per-base P(unpaired), distinct diagnostic |
| --- | --- | --- | --- |
| rnaplfold | stem_8nt | 2.51992e-19 | 3.68291e-05 |
| rnaplfold | stem_20nt | 3.58063e-25 | 0.00140732 |
| rnaplfold | loop_8nt | 1 | 1 |
| rnaplfold-cli | stem_8nt | 2.51992e-19 | not provided |
| rnaplfold-cli | stem_20nt | 3.58063e-25 | not provided |
| rnaplfold-cli | loop_8nt | 1 | not provided |
| vienna-exact | stem_8nt | 2.52178e-19 | not provided |
| vienna-exact | stem_20nt | 3.5841e-25 | not provided |
| vienna-exact | loop_8nt | 1 | not provided |
| rnafold | stem_8nt | not provided | 3.68291e-05 |
| rnafold | stem_20nt | not provided | 0.00140732 |
| rnafold | loop_8nt | not provided | 1 |
| ensemble-sample | stem_8nt | not provided | 2.5e-05 |
| ensemble-sample | stem_20nt | not provided | 0.001505 |
| ensemble-sample | loop_8nt | 1 | 1 |
| rnastructure-partition | stem_8nt | not provided | 3.68525e-05 |
| rnastructure-partition | stem_20nt | not provided | 0.00236153 |
| rnastructure-partition | loop_8nt | not provided | 1 |
| contrafold | stem_8nt | not provided | 0.00403483 |
| contrafold | stem_20nt | not provided | 0.0146599 |
| contrafold | loop_8nt | not provided | 1 |
| eternafold | stem_8nt | not provided | 0.00156989 |
| eternafold | stem_20nt | not provided | 0.00795437 |
| eternafold | loop_8nt | not provided | 1 |


The heuristic rank is not used as a pass/fail criterion. Compare probabilities and opening costs under the same scope and footprint.


| Temperature °C | Site | Joint P(open) | Opening cost |
| --- | --- | --- | --- |
| 25 | stem_8nt | 2.91835e-22 | 29.3789 |
| 25 | stem_20nt | 4.25189e-30 | 40.0699 |
| 25 | loop_8nt | 1 | 0.0000 |
| 37 | stem_8nt | 2.52178e-19 | 26.3939 |
| 37 | stem_20nt | 3.5841e-25 | 34.6921 |
| 37 | loop_8nt | 1 | 0.0000 |
| 50 | stem_8nt | 4.02028e-16 | 22.7648 |
| 50 | stem_20nt | 3.00542e-20 | 28.8661 |
| 50 | loop_8nt | 1 | 0.0000 |


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


Elapsed run time: 0.69 s. [Visual pipeline report](report.html), [full JSON](report.json), [metrics TSV](metrics.tsv), [input FASTA](target.fa). Heatmaps use the complete transcript, matching the prediction scope.
