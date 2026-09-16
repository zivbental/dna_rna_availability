# YOR090C
Status: ok. Length: 2006 nt. Measured usable bases: 878. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 878 | 0.3932 | 0.3818 |
| rnafold | ok | 878 | 0.3097 | 0.3152 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | -0.0032 | 0.0981 |
| seed_p | 126 | -0.3434 | -0.3131 |
| seed_p_vs_seed_pars | 87 | -0.6649 | -0.6248 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
