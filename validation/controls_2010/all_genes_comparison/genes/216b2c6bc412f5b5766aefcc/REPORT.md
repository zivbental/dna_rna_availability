# YJL126W
Status: ok. Length: 924 nt. Measured usable bases: 375. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 375 | 0.4019 | 0.3787 |
| rnafold | ok | 375 | 0.3401 | 0.3211 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 22 | -0.4075 | -0.2778 |
| seed_p | 22 | -0.7180 | -0.6054 |
| seed_p_vs_seed_pars | 8 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
