# YLR017W
Status: ok. Length: 1130 nt. Measured usable bases: 828. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 828 | 0.2430 | 0.2389 |
| rnafold | ok | 828 | 0.2434 | 0.2537 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 668 | -0.0539 | -0.0202 |
| seed_p | 668 | -0.0490 | -0.0306 |
| seed_p_vs_seed_pars | 572 | 0.0092 | 0.0356 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
