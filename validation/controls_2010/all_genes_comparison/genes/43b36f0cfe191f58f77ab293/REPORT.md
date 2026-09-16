# YDL155W
Status: ok. Length: 1545 nt. Measured usable bases: 751. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 751 | 0.2781 | 0.2716 |
| rnafold | ok | 751 | 0.2442 | 0.2379 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 159 | 0.0341 | 0.1310 |
| seed_p | 159 | 0.1515 | 0.2052 |
| seed_p_vs_seed_pars | 111 | 0.2356 | 0.4079 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
