# YCR012W
Status: ok. Length: 1460 nt. Measured usable bases: 1339. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1339 | 0.3578 | 0.3308 |
| rnafold | ok | 1339 | 0.3179 | 0.2802 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1240 | -0.1254 | -0.2977 |
| seed_p | 1240 | -0.1936 | -0.2475 |
| seed_p_vs_seed_pars | 1227 | -0.3453 | -0.2811 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
