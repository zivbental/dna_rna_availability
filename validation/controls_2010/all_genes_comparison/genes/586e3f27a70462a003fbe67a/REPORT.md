# YMR312W
Status: ok. Length: 953 nt. Measured usable bases: 444. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.2466 | 0.2381 |
| rnafold | ok | 444 | 0.1708 | 0.1799 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | -0.3174 | -0.4459 |
| seed_p | 66 | -0.7477 | -0.4781 |
| seed_p_vs_seed_pars | 58 | -0.6353 | -0.3257 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
