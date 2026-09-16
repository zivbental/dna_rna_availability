# YGL160W
Status: ok. Length: 1936 nt. Measured usable bases: 831. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 831 | 0.2359 | 0.2508 |
| rnafold | ok | 831 | 0.1564 | 0.1612 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | 0.0602 | -0.0726 |
| seed_p | 60 | 0.1564 | 0.2161 |
| seed_p_vs_seed_pars | 44 | -0.0674 | 0.0070 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
