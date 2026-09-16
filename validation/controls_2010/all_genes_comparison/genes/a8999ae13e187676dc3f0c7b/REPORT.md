# YKL175W
Status: ok. Length: 1633 nt. Measured usable bases: 1141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1141 | 0.2430 | 0.2244 |
| rnafold | ok | 1141 | 0.1801 | 0.1657 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 644 | 0.0152 | -0.0607 |
| seed_p | 644 | -0.2593 | -0.2485 |
| seed_p_vs_seed_pars | 447 | -0.4665 | -0.5210 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
