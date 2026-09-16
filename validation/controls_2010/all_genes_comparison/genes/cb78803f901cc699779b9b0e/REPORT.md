# YKL184W
Status: ok. Length: 1625 nt. Measured usable bases: 982. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 982 | 0.2962 | 0.2603 |
| rnafold | ok | 982 | 0.2877 | 0.2492 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 391 | 0.0454 | 0.0217 |
| seed_p | 391 | -0.2361 | -0.1437 |
| seed_p_vs_seed_pars | 267 | -0.3285 | -0.3180 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
