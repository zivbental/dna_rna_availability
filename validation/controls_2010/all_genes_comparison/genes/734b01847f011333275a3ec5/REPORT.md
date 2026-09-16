# YML027W
Status: ok. Length: 1615 nt. Measured usable bases: 569. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 569 | 0.3332 | 0.3284 |
| rnafold | ok | 569 | 0.2963 | 0.2947 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.3743 | -0.6339 |
| seed_p | 64 | -0.7495 | -0.7533 |
| seed_p_vs_seed_pars | 50 | -0.8163 | -0.8592 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
