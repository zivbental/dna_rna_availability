# YBL022C
Status: ok. Length: 3572 nt. Measured usable bases: 1884.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1884 | 0.3685 | 0.3667 |
| rnafold | ok | 1884 | 0.2991 | 0.3154 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 408 | 0.0704 | 0.0610 |
| seed_p | 408 | -0.0779 | -0.0629 |
| seed_p_vs_seed_pars | 306 | -0.4075 | -0.3383 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
