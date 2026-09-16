# YOR232W
Status: ok. Length: 943 nt. Measured usable bases: 622. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 622 | 0.3519 | 0.3484 |
| rnafold | ok | 622 | 0.3339 | 0.3320 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 404 | -0.2232 | 0.0408 |
| seed_p | 404 | -0.2215 | -0.1327 |
| seed_p_vs_seed_pars | 341 | -0.3653 | -0.3468 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
