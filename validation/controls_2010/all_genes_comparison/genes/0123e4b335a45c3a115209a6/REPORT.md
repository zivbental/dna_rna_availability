# YLR180W
Status: ok. Length: 1453 nt. Measured usable bases: 1226. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1226 | 0.3115 | 0.3043 |
| rnafold | ok | 1226 | 0.2388 | 0.2407 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1106 | -0.1766 | -0.1650 |
| seed_p | 1106 | -0.1503 | -0.1738 |
| seed_p_vs_seed_pars | 1008 | -0.2080 | -0.2726 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
