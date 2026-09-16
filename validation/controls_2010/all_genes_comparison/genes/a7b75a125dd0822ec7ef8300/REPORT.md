# YER178W
Status: ok. Length: 1415 nt. Measured usable bases: 1303. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1303 | 0.3492 | 0.3314 |
| rnafold | ok | 1303 | 0.3020 | 0.2828 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1310 | -0.2608 | -0.2260 |
| seed_p | 1310 | -0.2917 | -0.2464 |
| seed_p_vs_seed_pars | 1253 | -0.4207 | -0.3733 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
