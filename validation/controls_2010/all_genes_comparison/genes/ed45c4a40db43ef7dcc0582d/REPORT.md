# YGR285C
Status: ok. Length: 1361 nt. Measured usable bases: 1185. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1185 | 0.3017 | 0.2903 |
| rnafold | ok | 1185 | 0.2680 | 0.2494 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1095 | -0.0295 | 0.0375 |
| seed_p | 1095 | -0.1200 | -0.0877 |
| seed_p_vs_seed_pars | 969 | -0.2674 | -0.1995 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
