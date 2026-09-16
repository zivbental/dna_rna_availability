# YKL141W
Status: ok. Length: 719 nt. Measured usable bases: 544. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 544 | 0.2884 | 0.2920 |
| rnafold | ok | 544 | 0.2027 | 0.2027 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 418 | -0.1718 | -0.1079 |
| seed_p | 418 | -0.1630 | -0.0702 |
| seed_p_vs_seed_pars | 375 | -0.2801 | -0.2674 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
