# YJL133W
Status: ok. Length: 1248 nt. Measured usable bases: 625. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 625 | 0.2408 | 0.2228 |
| rnafold | ok | 625 | 0.2289 | 0.2241 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 191 | -0.0882 | 0.0743 |
| seed_p | 191 | -0.2571 | -0.1478 |
| seed_p_vs_seed_pars | 127 | 0.0405 | -0.0353 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
