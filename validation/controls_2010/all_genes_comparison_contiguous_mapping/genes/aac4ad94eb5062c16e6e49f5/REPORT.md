# YAL038W
Status: ok. Length: 1698 nt. Measured usable bases: 1619.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1619 | 0.3711 | 0.3527 |
| rnafold | ok | 1619 | 0.3396 | 0.3241 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1576 | -0.1619 | -0.1862 |
| seed_p | 1576 | -0.2099 | -0.1358 |
| seed_p_vs_seed_pars | 1563 | -0.3631 | -0.3076 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
