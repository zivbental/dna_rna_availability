# YBR036C
Status: ok. Length: 1339 nt. Measured usable bases: 1136.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1136 | 0.2697 | 0.2605 |
| rnafold | ok | 1136 | 0.1970 | 0.1939 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1049 | -0.0491 | -0.0537 |
| seed_p | 1049 | -0.1068 | -0.1115 |
| seed_p_vs_seed_pars | 900 | -0.1937 | -0.2055 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
