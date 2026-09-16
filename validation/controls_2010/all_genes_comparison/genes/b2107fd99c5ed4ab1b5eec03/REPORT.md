# YLR293C
Status: ok. Length: 780 nt. Measured usable bases: 695. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 695 | 0.3788 | 0.3668 |
| rnafold | ok | 695 | 0.3363 | 0.3254 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 660 | -0.2203 | -0.2031 |
| seed_p | 660 | -0.1481 | -0.1184 |
| seed_p_vs_seed_pars | 598 | -0.3559 | -0.3429 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
