# YBL099W
Status: ok. Length: 2203 nt. Measured usable bases: 1489.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1489 | 0.3018 | 0.2902 |
| rnafold | ok | 1489 | 0.2425 | 0.2166 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 984 | -0.0525 | -0.0442 |
| seed_p | 984 | -0.1979 | -0.1411 |
| seed_p_vs_seed_pars | 777 | -0.0964 | -0.0812 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
