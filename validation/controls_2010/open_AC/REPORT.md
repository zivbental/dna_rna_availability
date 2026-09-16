# open_AC

Designed positive control: A/C-only RNA has no AU, GC or GU pairing partners under the canonical secondary-structure model. Expected joint opening probability: 1.

RNA, Turner 2004, 37 °C, dangles=2, unrestricted global pairing. Local window and pair span equal the full transcript length for a matched-scope comparison. Experimental buffer/temperature are not asserted to match this computational protocol. Magnesium, tertiary contacts, proteins and cellular binding are not modeled. No experimental data constrain any prediction. All coordinates are one-based and inclusive.

| Site | Coordinates | Sequence | Joint P(open), global exact | Opening cost (kcal/mol) |
| --- | --- | --- | --- | --- |
| open_8nt | 5–12 | ACACACAC | 1 | 0.0000 |
| open_20nt | 5–24 | ACACACACACACACACACAC | 1 | 0.0000 |


| Adapter | Site | Joint P(open) | Mean per-base P(unpaired), distinct diagnostic |
| --- | --- | --- | --- |
| rnaplfold | open_8nt | 1 | 1 |
| rnaplfold | open_20nt | 1 | 1 |
| rnaplfold-cli | open_8nt | 1 | not provided |
| rnaplfold-cli | open_20nt | 1 | not provided |
| vienna-exact | open_8nt | 1 | not provided |
| vienna-exact | open_20nt | 1 | not provided |
| rnafold | open_8nt | not provided | 1 |
| rnafold | open_20nt | not provided | 1 |
| ensemble-sample | open_8nt | 1 | 1 |
| ensemble-sample | open_20nt | 1 | 1 |
| rnastructure-partition | open_8nt | not provided | 1 |
| rnastructure-partition | open_20nt | not provided | 1 |
| contrafold | open_8nt | not provided | 1 |
| contrafold | open_20nt | not provided | 1 |
| eternafold | open_8nt | not provided | 1 |
| eternafold | open_20nt | not provided | 1 |


The heuristic rank is not used as a pass/fail criterion. Compare probabilities and opening costs under the same scope and footprint.


| Temperature °C | Site | Joint P(open) | Opening cost |
| --- | --- | --- | --- |
| 25 | open_8nt | 1 | 0.0000 |
| 25 | open_20nt | 1 | 0.0000 |
| 37 | open_8nt | 1 | 0.0000 |
| 37 | open_20nt | 1 | 0.0000 |
| 50 | open_8nt | 1 | 0.0000 |
| 50 | open_20nt | 1 | 0.0000 |


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


Elapsed run time: 0.55 s. [Visual pipeline report](report.html), [full JSON](report.json), [metrics TSV](metrics.tsv), [input FASTA](target.fa). Heatmaps use the complete transcript, matching the prediction scope.
