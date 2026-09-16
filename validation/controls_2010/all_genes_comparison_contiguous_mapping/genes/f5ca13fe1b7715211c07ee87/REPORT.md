# YBR052C
Status: ok. Length: 709 nt. Measured usable bases: 497.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 497 | 0.4530 | 0.4246 |
| rnafold | ok | 497 | 0.3442 | 0.3157 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 328 | -0.1987 | -0.3417 |
| seed_p | 328 | -0.4805 | -0.3409 |
| seed_p_vs_seed_pars | 274 | -0.4072 | -0.3115 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
