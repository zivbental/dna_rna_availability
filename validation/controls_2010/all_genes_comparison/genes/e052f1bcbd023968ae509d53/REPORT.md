# YGL248W
Status: ok. Length: 1212 nt. Measured usable bases: 481. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 481 | 0.3362 | 0.3219 |
| rnafold | ok | 481 | 0.3313 | 0.3143 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | 0.1028 | -0.0814 |
| seed_p | 30 | 0.7355 | 0.8105 |
| seed_p_vs_seed_pars | 24 | 0.5894 | 0.5745 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
