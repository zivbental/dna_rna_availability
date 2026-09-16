# YJL117W
Status: ok. Length: 1094 nt. Measured usable bases: 811. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 811 | 0.2913 | 0.2683 |
| rnafold | ok | 811 | 0.2621 | 0.2407 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 637 | -0.1873 | -0.0530 |
| seed_p | 637 | -0.2388 | -0.1913 |
| seed_p_vs_seed_pars | 527 | -0.1583 | -0.1841 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
