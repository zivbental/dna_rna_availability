# YLR395C
Status: ok. Length: 563 nt. Measured usable bases: 388. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 388 | 0.1877 | 0.1809 |
| rnafold | ok | 388 | 0.1576 | 0.1802 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 232 | 0.0210 | 0.0189 |
| seed_p | 232 | -0.2153 | -0.0175 |
| seed_p_vs_seed_pars | 185 | -0.2212 | -0.0611 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
