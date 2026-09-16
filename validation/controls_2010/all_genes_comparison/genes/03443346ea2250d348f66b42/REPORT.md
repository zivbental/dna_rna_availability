# YLL049W
Status: ok. Length: 657 nt. Measured usable bases: 305. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 305 | 0.2154 | 0.1966 |
| rnafold | ok | 305 | 0.1381 | 0.1032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | 0.4441 | 0.1224 |
| seed_p | 62 | 0.6218 | 0.7651 |
| seed_p_vs_seed_pars | 43 | -0.2770 | -0.2513 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
