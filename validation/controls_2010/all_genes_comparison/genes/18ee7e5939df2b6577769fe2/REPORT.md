# YMR295C
Status: ok. Length: 809 nt. Measured usable bases: 513. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 513 | 0.2556 | 0.2553 |
| rnafold | ok | 513 | 0.2582 | 0.2619 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 376 | 0.1568 | -0.0436 |
| seed_p | 376 | -0.1853 | -0.1972 |
| seed_p_vs_seed_pars | 310 | -0.3056 | -0.2365 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
