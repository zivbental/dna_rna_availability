# YER143W
Status: ok. Length: 1502 nt. Measured usable bases: 634. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 634 | 0.3084 | 0.3030 |
| rnafold | ok | 634 | 0.2636 | 0.2598 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.3532 | -0.4485 |
| seed_p | 54 | -0.1897 | -0.1426 |
| seed_p_vs_seed_pars | 24 | -0.6835 | -0.9020 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
