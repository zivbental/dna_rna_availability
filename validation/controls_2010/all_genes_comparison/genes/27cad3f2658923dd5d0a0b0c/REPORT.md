# YMR079W
Status: ok. Length: 1276 nt. Measured usable bases: 784. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 784 | 0.2959 | 0.2883 |
| rnafold | ok | 784 | 0.2878 | 0.2810 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 433 | 0.2474 | 0.1002 |
| seed_p | 433 | 0.0441 | -0.0178 |
| seed_p_vs_seed_pars | 328 | 0.0339 | -0.0951 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
