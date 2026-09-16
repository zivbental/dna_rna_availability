# YGR026W
Status: ok. Length: 991 nt. Measured usable bases: 598. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 598 | 0.2305 | 0.2079 |
| rnafold | ok | 598 | 0.1442 | 0.1298 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 183 | 0.1036 | 0.2951 |
| seed_p | 183 | -0.3825 | -0.1406 |
| seed_p_vs_seed_pars | 109 | -0.2701 | -0.0491 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
