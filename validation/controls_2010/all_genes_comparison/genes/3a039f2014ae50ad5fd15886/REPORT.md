# YER125W
Status: ok. Length: 3315 nt. Measured usable bases: 2071. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2071 | 0.2886 | 0.2765 |
| rnafold | ok | 2071 | 0.2723 | 0.2585 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 898 | 0.0183 | 0.0994 |
| seed_p | 898 | -0.0897 | -0.0623 |
| seed_p_vs_seed_pars | 697 | -0.2357 | -0.2104 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
