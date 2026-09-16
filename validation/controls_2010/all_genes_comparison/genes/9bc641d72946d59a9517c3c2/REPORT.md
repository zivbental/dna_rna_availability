# YKL047W
Status: ok. Length: 1748 nt. Measured usable bases: 663. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 663 | 0.2927 | 0.2939 |
| rnafold | ok | 663 | 0.1892 | 0.2070 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | 0.2659 | 0.2846 |
| seed_p | 43 | 0.1619 | -0.0222 |
| seed_p_vs_seed_pars | 29 | -0.2049 | -0.7286 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
