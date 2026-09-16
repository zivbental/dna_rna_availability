# YOR109W
Status: ok. Length: 3487 nt. Measured usable bases: 1491. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1491 | 0.2928 | 0.2787 |
| rnafold | ok | 1491 | 0.2095 | 0.2013 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | -0.1330 | 0.0869 |
| seed_p | 179 | 0.0925 | 0.0373 |
| seed_p_vs_seed_pars | 114 | 0.1629 | 0.1700 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
