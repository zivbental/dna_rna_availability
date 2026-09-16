# YBL015W
Status: ok. Length: 1901 nt. Measured usable bases: 799.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 799 | 0.4140 | 0.4007 |
| rnafold | ok | 799 | 0.3126 | 0.2945 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 145 | -0.4338 | -0.4202 |
| seed_p | 145 | -0.4354 | -0.7366 |
| seed_p_vs_seed_pars | 110 | 0.1604 | -0.2565 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
