# YPL226W
Status: ok. Length: 3905 nt. Measured usable bases: 2850. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2850 | 0.2990 | 0.2872 |
| rnafold | ok | 2850 | 0.2482 | 0.2350 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1858 | -0.0309 | -0.1561 |
| seed_p | 1858 | -0.1215 | -0.1972 |
| seed_p_vs_seed_pars | 1463 | -0.1314 | -0.2432 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
