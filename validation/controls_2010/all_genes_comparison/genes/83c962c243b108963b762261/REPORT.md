# YNL190W
Status: ok. Length: 1428 nt. Measured usable bases: 850. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 850 | 0.2105 | 0.2025 |
| rnafold | ok | 850 | 0.1467 | 0.1582 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 604 | 0.0075 | -0.1092 |
| seed_p | 604 | -0.1913 | -0.1034 |
| seed_p_vs_seed_pars | 523 | -0.3454 | -0.2759 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
