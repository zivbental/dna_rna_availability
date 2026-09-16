# YDL097C
Status: ok. Length: 1387 nt. Measured usable bases: 1054. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1054 | 0.3698 | 0.3772 |
| rnafold | ok | 1054 | 0.3612 | 0.3630 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 746 | -0.1071 | -0.2196 |
| seed_p | 746 | -0.2374 | -0.2588 |
| seed_p_vs_seed_pars | 607 | -0.3414 | -0.3206 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
