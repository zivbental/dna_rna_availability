# YBL056W
Status: ok. Length: 1882 nt. Measured usable bases: 1201.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1201 | 0.2654 | 0.2661 |
| rnafold | ok | 1201 | 0.1880 | 0.1890 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 664 | -0.0671 | -0.1048 |
| seed_p | 664 | -0.2339 | -0.2268 |
| seed_p_vs_seed_pars | 515 | -0.1464 | -0.1482 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
