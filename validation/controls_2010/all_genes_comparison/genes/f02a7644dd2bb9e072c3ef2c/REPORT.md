# YNL071W
Status: ok. Length: 1639 nt. Measured usable bases: 1387. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1387 | 0.3394 | 0.3217 |
| rnafold | ok | 1387 | 0.3099 | 0.3003 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1323 | -0.1867 | -0.0840 |
| seed_p | 1323 | -0.2380 | -0.1397 |
| seed_p_vs_seed_pars | 1219 | -0.4230 | -0.3147 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
