# YER004W
Status: ok. Length: 1092 nt. Measured usable bases: 748. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 748 | 0.2984 | 0.3065 |
| rnafold | ok | 748 | 0.2327 | 0.2472 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 435 | -0.1856 | -0.0696 |
| seed_p | 435 | -0.0599 | -0.1468 |
| seed_p_vs_seed_pars | 370 | -0.1364 | -0.2345 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
