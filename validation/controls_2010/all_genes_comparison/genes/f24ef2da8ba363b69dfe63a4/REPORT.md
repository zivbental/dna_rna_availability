# YOR370C
Status: ok. Length: 2279 nt. Measured usable bases: 1279. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1279 | 0.2834 | 0.2819 |
| rnafold | ok | 1279 | 0.2072 | 0.2100 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 375 | -0.0151 | -0.0517 |
| seed_p | 375 | -0.2395 | 0.0214 |
| seed_p_vs_seed_pars | 292 | -0.2148 | -0.1510 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
