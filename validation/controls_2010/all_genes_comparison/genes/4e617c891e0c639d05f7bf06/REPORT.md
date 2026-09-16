# YHR191C
Status: ok. Length: 624 nt. Measured usable bases: 196. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 196 | 0.3381 | 0.3310 |
| rnafold | ok | 196 | 0.2418 | 0.2762 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.3632 | -0.5098 |
| seed_p | 39 | -0.4025 | -0.3927 |
| seed_p_vs_seed_pars | 29 | -0.6790 | -0.6356 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
