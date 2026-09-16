# YBL039C
Status: ok. Length: 1875 nt. Measured usable bases: 1452.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1452 | 0.3826 | 0.3668 |
| rnafold | ok | 1452 | 0.3331 | 0.3280 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1127 | -0.1005 | -0.0326 |
| seed_p | 1127 | -0.3342 | -0.2821 |
| seed_p_vs_seed_pars | 878 | -0.4456 | -0.3410 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
