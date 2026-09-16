# YJL212C
Status: ok. Length: 2532 nt. Measured usable bases: 1548. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1548 | 0.2411 | 0.2384 |
| rnafold | ok | 1548 | 0.2076 | 0.2059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 505 | 0.0092 | 0.2278 |
| seed_p | 505 | -0.0314 | 0.0390 |
| seed_p_vs_seed_pars | 388 | -0.1633 | -0.1350 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
