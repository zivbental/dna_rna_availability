# YER009W
Status: ok. Length: 559 nt. Measured usable bases: 444. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.0708 | 0.0660 |
| rnafold | ok | 444 | 0.1176 | 0.1221 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 442 | 0.2649 | 0.2052 |
| seed_p | 442 | 0.1314 | 0.1746 |
| seed_p_vs_seed_pars | 435 | -0.0499 | -0.0452 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
