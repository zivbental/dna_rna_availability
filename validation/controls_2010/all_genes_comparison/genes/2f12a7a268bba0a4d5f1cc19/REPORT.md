# YMR215W
Status: ok. Length: 1724 nt. Measured usable bases: 1337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1337 | 0.3101 | 0.3075 |
| rnafold | ok | 1337 | 0.2534 | 0.2716 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1058 | -0.0950 | -0.1475 |
| seed_p | 1058 | -0.1532 | -0.1532 |
| seed_p_vs_seed_pars | 834 | -0.2447 | -0.2199 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
