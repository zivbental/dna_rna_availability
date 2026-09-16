# YGR031W
Status: ok. Length: 1484 nt. Measured usable bases: 883. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 883 | 0.3878 | 0.3637 |
| rnafold | ok | 883 | 0.3399 | 0.3449 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 334 | 0.0499 | 0.1381 |
| seed_p | 334 | -0.4022 | -0.2677 |
| seed_p_vs_seed_pars | 263 | -0.5453 | -0.4049 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
