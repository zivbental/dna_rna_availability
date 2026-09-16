# YOR264W
Status: ok. Length: 1418 nt. Measured usable bases: 625. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 625 | 0.3136 | 0.3216 |
| rnafold | ok | 625 | 0.2767 | 0.2777 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | 0.0854 | 0.1598 |
| seed_p | 92 | -0.0415 | 0.1178 |
| seed_p_vs_seed_pars | 57 | -0.3297 | -0.1190 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
