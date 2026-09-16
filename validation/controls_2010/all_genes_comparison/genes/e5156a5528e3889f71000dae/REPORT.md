# YDL022W
Status: ok. Length: 1380 nt. Measured usable bases: 1065. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1065 | 0.2958 | 0.2700 |
| rnafold | ok | 1065 | 0.2605 | 0.2427 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 805 | -0.0619 | -0.0088 |
| seed_p | 805 | -0.1419 | -0.0877 |
| seed_p_vs_seed_pars | 705 | -0.2281 | -0.1229 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
