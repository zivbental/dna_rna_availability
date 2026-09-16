# YGL039W
Status: ok. Length: 1255 nt. Measured usable bases: 767. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 767 | 0.3533 | 0.3381 |
| rnafold | ok | 767 | 0.3313 | 0.3257 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 290 | 0.0112 | -0.0506 |
| seed_p | 290 | -0.3187 | -0.2428 |
| seed_p_vs_seed_pars | 233 | -0.3582 | -0.3002 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
