# YLR137W
Status: ok. Length: 1141 nt. Measured usable bases: 438. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 438 | 0.3433 | 0.3396 |
| rnafold | ok | 438 | 0.3446 | 0.3261 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | 0.2566 | -0.1056 |
| seed_p | 79 | 0.0566 | 0.0158 |
| seed_p_vs_seed_pars | 62 | 0.3673 | 0.1774 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
