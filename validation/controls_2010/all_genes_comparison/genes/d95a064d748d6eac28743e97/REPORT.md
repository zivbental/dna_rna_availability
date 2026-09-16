# YDL236W
Status: ok. Length: 1148 nt. Measured usable bases: 752. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 752 | 0.3468 | 0.3451 |
| rnafold | ok | 752 | 0.2801 | 0.2636 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 519 | -0.0217 | 0.1118 |
| seed_p | 519 | -0.1043 | -0.1031 |
| seed_p_vs_seed_pars | 414 | -0.4108 | -0.4295 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
