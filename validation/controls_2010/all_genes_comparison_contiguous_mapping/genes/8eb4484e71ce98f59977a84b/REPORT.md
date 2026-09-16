# YBL058W
Status: ok. Length: 1419 nt. Measured usable bases: 1005.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1005 | 0.3508 | 0.3546 |
| rnafold | ok | 1005 | 0.3170 | 0.3188 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 670 | -0.0387 | -0.0829 |
| seed_p | 670 | -0.2115 | -0.1629 |
| seed_p_vs_seed_pars | 539 | -0.2405 | -0.3100 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
