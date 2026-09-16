# YOL008W
Status: ok. Length: 789 nt. Measured usable bases: 329. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 329 | 0.2525 | 0.2583 |
| rnafold | ok | 329 | 0.2426 | 0.2521 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.2043 | -0.5950 |
| seed_p | 61 | -0.1351 | -0.5112 |
| seed_p_vs_seed_pars | 60 | 0.2338 | -0.2421 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
