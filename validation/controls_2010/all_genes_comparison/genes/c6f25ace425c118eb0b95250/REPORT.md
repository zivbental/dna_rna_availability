# YER006W
Status: ok. Length: 1648 nt. Measured usable bases: 1039. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1039 | 0.3630 | 0.3600 |
| rnafold | ok | 1039 | 0.2779 | 0.2862 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 496 | -0.1336 | -0.0741 |
| seed_p | 496 | -0.1824 | -0.1011 |
| seed_p_vs_seed_pars | 373 | -0.1158 | -0.0405 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
