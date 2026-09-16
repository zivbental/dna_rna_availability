# YGR048W
Status: ok. Length: 1215 nt. Measured usable bases: 504. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 504 | 0.3469 | 0.3412 |
| rnafold | ok | 504 | 0.3330 | 0.3274 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.8119 | -0.8072 |
| seed_p | 57 | -0.6433 | -0.6518 |
| seed_p_vs_seed_pars | 37 | -0.4957 | -0.3131 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
