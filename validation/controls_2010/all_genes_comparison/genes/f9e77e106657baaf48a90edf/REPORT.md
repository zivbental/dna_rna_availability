# YOL127W
Status: ok. Length: 523 nt. Measured usable bases: 463. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 463 | 0.3008 | 0.2952 |
| rnafold | ok | 463 | 0.3042 | 0.2960 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 430 | 0.0133 | 0.2240 |
| seed_p | 430 | 0.0621 | 0.0648 |
| seed_p_vs_seed_pars | 406 | -0.1023 | -0.1234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
