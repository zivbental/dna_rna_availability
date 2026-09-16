# YOR259C
Status: ok. Length: 1381 nt. Measured usable bases: 895. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 895 | 0.3676 | 0.3608 |
| rnafold | ok | 895 | 0.3104 | 0.3201 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 419 | 0.0676 | -0.1037 |
| seed_p | 419 | 0.0224 | -0.0796 |
| seed_p_vs_seed_pars | 331 | 0.0779 | 0.0385 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
