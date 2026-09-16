# YHR032W
Status: ok. Length: 1746 nt. Measured usable bases: 1141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1141 | 0.2834 | 0.2668 |
| rnafold | ok | 1141 | 0.2138 | 0.1949 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 433 | -0.1040 | 0.1581 |
| seed_p | 433 | 0.0776 | 0.0965 |
| seed_p_vs_seed_pars | 325 | -0.0812 | -0.1401 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
