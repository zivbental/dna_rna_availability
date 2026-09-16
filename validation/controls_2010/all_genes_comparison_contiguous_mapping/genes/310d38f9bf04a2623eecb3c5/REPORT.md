# YBL016W
Status: ok. Length: 1418 nt. Measured usable bases: 744.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 744 | 0.2719 | 0.2792 |
| rnafold | ok | 744 | 0.2366 | 0.2482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 284 | -0.1477 | -0.2564 |
| seed_p | 284 | -0.1059 | -0.1597 |
| seed_p_vs_seed_pars | 241 | -0.1129 | -0.1473 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
