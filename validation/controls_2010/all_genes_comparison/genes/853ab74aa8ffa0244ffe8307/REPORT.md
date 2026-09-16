# YLR083C
Status: ok. Length: 2168 nt. Measured usable bases: 1569. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1569 | 0.3088 | 0.2888 |
| rnafold | ok | 1569 | 0.2679 | 0.2513 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 986 | -0.1689 | -0.1215 |
| seed_p | 986 | -0.2427 | -0.1699 |
| seed_p_vs_seed_pars | 808 | -0.3456 | -0.2536 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
