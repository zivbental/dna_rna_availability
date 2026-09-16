# YOL140W
Status: ok. Length: 1338 nt. Measured usable bases: 607. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 607 | 0.3781 | 0.3736 |
| rnafold | ok | 607 | 0.3486 | 0.3610 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 102 | -0.1053 | -0.0243 |
| seed_p | 102 | 0.0067 | -0.0387 |
| seed_p_vs_seed_pars | 68 | -0.2266 | -0.2956 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
