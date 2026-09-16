# YNL321W
Status: ok. Length: 2727 nt. Measured usable bases: 1355. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1355 | 0.2672 | 0.2412 |
| rnafold | ok | 1355 | 0.2104 | 0.2127 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 333 | -0.1070 | -0.0941 |
| seed_p | 333 | -0.1344 | -0.1338 |
| seed_p_vs_seed_pars | 241 | -0.2671 | -0.1548 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
