# YEL060C
Status: ok. Length: 2370 nt. Measured usable bases: 1043. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1043 | 0.3663 | 0.3608 |
| rnafold | ok | 1043 | 0.3192 | 0.3121 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 188 | -0.3545 | -0.1165 |
| seed_p | 188 | -0.3934 | -0.3718 |
| seed_p_vs_seed_pars | 142 | -0.2213 | -0.3151 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
