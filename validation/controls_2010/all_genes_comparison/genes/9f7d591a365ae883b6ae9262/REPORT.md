# YER148W
Status: ok. Length: 913 nt. Measured usable bases: 485. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 485 | 0.4002 | 0.3953 |
| rnafold | ok | 485 | 0.2750 | 0.2835 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 360 | -0.1399 | -0.1557 |
| seed_p | 360 | -0.2275 | -0.3045 |
| seed_p_vs_seed_pars | 292 | -0.2583 | -0.4609 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
