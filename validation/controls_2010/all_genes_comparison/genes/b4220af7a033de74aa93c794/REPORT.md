# YNR043W
Status: ok. Length: 1348 nt. Measured usable bases: 1078. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1078 | 0.2150 | 0.2013 |
| rnafold | ok | 1078 | 0.1368 | 0.1333 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 930 | 0.0718 | 0.0298 |
| seed_p | 930 | -0.1596 | -0.1387 |
| seed_p_vs_seed_pars | 734 | -0.3848 | -0.2977 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
