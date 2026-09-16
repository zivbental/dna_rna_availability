# YBR092C
Status: ok. Length: 1440 nt. Measured usable bases: 948.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 948 | 0.3356 | 0.3152 |
| rnafold | ok | 948 | 0.2752 | 0.2496 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 763 | 0.0302 | -0.0370 |
| seed_p | 763 | -0.3386 | -0.3201 |
| seed_p_vs_seed_pars | 658 | -0.3954 | -0.3744 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
