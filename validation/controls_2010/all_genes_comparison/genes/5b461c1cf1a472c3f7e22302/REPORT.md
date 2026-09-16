# YDR432W
Status: ok. Length: 1245 nt. Measured usable bases: 834. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 834 | 0.1982 | 0.1788 |
| rnafold | ok | 834 | 0.2526 | 0.2280 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 381 | 0.0343 | 0.2041 |
| seed_p | 381 | 0.0446 | 0.0248 |
| seed_p_vs_seed_pars | 315 | -0.1074 | -0.1369 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
