# YMR074C
Status: ok. Length: 495 nt. Measured usable bases: 356. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 356 | 0.4446 | 0.4561 |
| rnafold | ok | 356 | 0.2929 | 0.3210 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 275 | -0.2160 | -0.3502 |
| seed_p | 275 | -0.3998 | -0.4471 |
| seed_p_vs_seed_pars | 218 | -0.3626 | -0.5252 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
