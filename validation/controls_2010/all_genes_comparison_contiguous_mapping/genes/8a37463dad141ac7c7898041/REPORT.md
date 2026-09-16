# YAL044W-A
Status: ok. Length: 446 nt. Measured usable bases: 271.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 271 | 0.3787 | 0.3788 |
| rnafold | ok | 271 | 0.2513 | 0.2418 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 177 | 0.1214 | 0.2569 |
| seed_p | 177 | -0.4524 | -0.3822 |
| seed_p_vs_seed_pars | 154 | -0.3497 | -0.3075 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
