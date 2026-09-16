# YBL082C
Status: ok. Length: 1377 nt. Measured usable bases: 857.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 857 | 0.2952 | 0.2559 |
| rnafold | ok | 857 | 0.2818 | 0.2591 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 309 | -0.0314 | 0.1170 |
| seed_p | 309 | -0.1290 | -0.1014 |
| seed_p_vs_seed_pars | 247 | -0.3374 | -0.3291 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
