# YAR007C
Status: ok. Length: 1983 nt. Measured usable bases: 1217.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1217 | 0.3555 | 0.3570 |
| rnafold | ok | 1217 | 0.3301 | 0.3381 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 464 | -0.0438 | -0.2046 |
| seed_p | 464 | -0.1936 | -0.1508 |
| seed_p_vs_seed_pars | 323 | -0.2726 | -0.1908 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
