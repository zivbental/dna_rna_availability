# YAL042W
Status: ok. Length: 1332 nt. Measured usable bases: 1136.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1136 | 0.3362 | 0.3265 |
| rnafold | ok | 1136 | 0.2604 | 0.2608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1099 | -0.1273 | -0.1853 |
| seed_p | 1099 | -0.1428 | -0.1344 |
| seed_p_vs_seed_pars | 934 | -0.1292 | -0.0629 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
