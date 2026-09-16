# YDR204W
Status: ok. Length: 1210 nt. Measured usable bases: 621. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 621 | 0.3823 | 0.3831 |
| rnafold | ok | 621 | 0.3275 | 0.3339 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 170 | 0.1503 | 0.0340 |
| seed_p | 170 | 0.2396 | 0.2746 |
| seed_p_vs_seed_pars | 118 | 0.1536 | 0.1310 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
