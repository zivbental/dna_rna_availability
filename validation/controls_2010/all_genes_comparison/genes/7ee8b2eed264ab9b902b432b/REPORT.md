# YCR036W
Status: ok. Length: 1122 nt. Measured usable bases: 515. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 515 | 0.3466 | 0.3412 |
| rnafold | ok | 515 | 0.3129 | 0.3152 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 112 | 0.0004 | -0.1803 |
| seed_p | 112 | -0.3075 | -0.4378 |
| seed_p_vs_seed_pars | 88 | -0.0156 | 0.1612 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
