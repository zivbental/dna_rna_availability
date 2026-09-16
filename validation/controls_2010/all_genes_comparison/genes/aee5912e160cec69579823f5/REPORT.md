# YMR243C
Status: ok. Length: 1602 nt. Measured usable bases: 1429. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1429 | 0.2775 | 0.2611 |
| rnafold | ok | 1429 | 0.1969 | 0.1984 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1412 | -0.1398 | -0.1073 |
| seed_p | 1412 | -0.1315 | -0.1782 |
| seed_p_vs_seed_pars | 1208 | -0.1853 | -0.2054 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
