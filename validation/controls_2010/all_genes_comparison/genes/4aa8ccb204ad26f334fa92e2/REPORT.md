# YGR136W
Status: ok. Length: 726 nt. Measured usable bases: 458. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 458 | 0.1631 | 0.1600 |
| rnafold | ok | 458 | 0.1877 | 0.1973 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 208 | -0.3408 | 0.0759 |
| seed_p | 208 | -0.1438 | -0.1635 |
| seed_p_vs_seed_pars | 181 | -0.0712 | -0.0548 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
