# YOR212W
Status: ok. Length: 1560 nt. Measured usable bases: 895. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 895 | 0.2976 | 0.2645 |
| rnafold | ok | 895 | 0.2683 | 0.2315 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 363 | 0.0296 | -0.0278 |
| seed_p | 363 | -0.1515 | -0.1828 |
| seed_p_vs_seed_pars | 234 | 0.0986 | -0.0094 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
