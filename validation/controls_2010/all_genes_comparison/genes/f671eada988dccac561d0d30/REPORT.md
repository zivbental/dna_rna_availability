# YOR026W
Status: ok. Length: 1066 nt. Measured usable bases: 504. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 504 | 0.3495 | 0.3228 |
| rnafold | ok | 504 | 0.2917 | 0.2729 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.1106 | -0.1411 |
| seed_p | 39 | -0.0999 | -0.1944 |
| seed_p_vs_seed_pars | 29 | -0.6362 | -0.6032 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
