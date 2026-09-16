# YCL057W
Status: ok. Length: 2283 nt. Measured usable bases: 1553. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1553 | 0.3269 | 0.2960 |
| rnafold | ok | 1553 | 0.2529 | 0.2371 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 781 | 0.0001 | -0.0480 |
| seed_p | 781 | -0.1258 | -0.1179 |
| seed_p_vs_seed_pars | 589 | -0.3895 | -0.3148 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
