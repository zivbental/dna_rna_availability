# YHR123W
Status: ok. Length: 1337 nt. Measured usable bases: 897. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 897 | 0.1949 | 0.1967 |
| rnafold | ok | 897 | 0.1551 | 0.1469 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 516 | -0.1790 | -0.0326 |
| seed_p | 516 | -0.0022 | -0.0482 |
| seed_p_vs_seed_pars | 362 | -0.1111 | -0.1583 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
