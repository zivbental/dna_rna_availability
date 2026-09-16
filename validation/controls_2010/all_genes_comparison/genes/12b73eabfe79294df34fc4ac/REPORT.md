# YAL020C
Status: ok. Length: 1053 nt. Measured usable bases: 542. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 542 | 0.3727 | 0.3607 |
| rnafold | ok | 542 | 0.3313 | 0.3140 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | -0.1967 | -0.4609 |
| seed_p | 92 | -0.0750 | -0.3396 |
| seed_p_vs_seed_pars | 68 | -0.1449 | -0.2855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
