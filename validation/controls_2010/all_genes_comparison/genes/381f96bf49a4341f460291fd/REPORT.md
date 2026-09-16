# YMR246W
Status: ok. Length: 2486 nt. Measured usable bases: 2000. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2000 | 0.3259 | 0.3215 |
| rnafold | ok | 2000 | 0.2472 | 0.2608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1682 | -0.1136 | -0.1719 |
| seed_p | 1682 | -0.2484 | -0.2562 |
| seed_p_vs_seed_pars | 1372 | -0.2474 | -0.2303 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
