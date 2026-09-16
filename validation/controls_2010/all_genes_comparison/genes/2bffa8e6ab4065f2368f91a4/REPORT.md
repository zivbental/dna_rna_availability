# YOR061W
Status: ok. Length: 1359 nt. Measured usable bases: 593. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 593 | 0.3277 | 0.2979 |
| rnafold | ok | 593 | 0.2383 | 0.2092 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | 0.1459 | 0.3518 |
| seed_p | 124 | 0.1396 | 0.1511 |
| seed_p_vs_seed_pars | 76 | -0.3505 | -0.3808 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
