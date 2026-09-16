# YMR109W
Status: ok. Length: 3768 nt. Measured usable bases: 1333. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1333 | 0.3452 | 0.3322 |
| rnafold | ok | 1333 | 0.3432 | 0.3256 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | -0.1801 | -0.5295 |
| seed_p | 66 | 0.1807 | 0.0184 |
| seed_p_vs_seed_pars | 49 | 0.1207 | 0.1608 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
