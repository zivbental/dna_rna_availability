# YOR020C
Status: ok. Length: 424 nt. Measured usable bases: 349. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 349 | 0.2520 | 0.2091 |
| rnafold | ok | 349 | 0.2724 | 0.2868 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 314 | -0.1047 | 0.0539 |
| seed_p | 314 | -0.3085 | 0.1161 |
| seed_p_vs_seed_pars | 290 | -0.4439 | 0.0505 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
