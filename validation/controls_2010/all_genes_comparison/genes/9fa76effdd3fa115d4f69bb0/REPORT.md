# YEL002C
Status: ok. Length: 1467 nt. Measured usable bases: 1089. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1089 | 0.3145 | 0.2926 |
| rnafold | ok | 1089 | 0.2548 | 0.2474 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 908 | -0.2809 | -0.2598 |
| seed_p | 908 | -0.2434 | -0.1950 |
| seed_p_vs_seed_pars | 751 | -0.2694 | -0.2312 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
