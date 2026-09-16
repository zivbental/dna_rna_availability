# YJR137C
Status: ok. Length: 4436 nt. Measured usable bases: 1857. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1857 | 0.3486 | 0.3338 |
| rnafold | ok | 1857 | 0.2585 | 0.2474 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 170 | 0.0318 | -0.0433 |
| seed_p | 170 | -0.0410 | -0.1141 |
| seed_p_vs_seed_pars | 141 | -0.0713 | -0.1404 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
