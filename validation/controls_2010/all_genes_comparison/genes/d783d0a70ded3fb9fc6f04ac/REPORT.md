# YGL245W
Status: ok. Length: 2208 nt. Measured usable bases: 1901. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1901 | 0.3323 | 0.3148 |
| rnafold | ok | 1901 | 0.2663 | 0.2531 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1810 | -0.1896 | -0.0388 |
| seed_p | 1810 | -0.0442 | 0.0195 |
| seed_p_vs_seed_pars | 1533 | -0.2174 | -0.1481 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
