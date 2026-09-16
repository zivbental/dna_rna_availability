# YOL123W
Status: ok. Length: 2091 nt. Measured usable bases: 1261. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1261 | 0.3295 | 0.3271 |
| rnafold | ok | 1261 | 0.3355 | 0.3234 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 478 | -0.0963 | -0.1055 |
| seed_p | 478 | -0.3189 | -0.3419 |
| seed_p_vs_seed_pars | 316 | -0.4180 | -0.3053 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
