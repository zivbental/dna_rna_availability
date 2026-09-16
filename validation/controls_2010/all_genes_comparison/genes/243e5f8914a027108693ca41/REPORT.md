# YLL027W
Status: ok. Length: 948 nt. Measured usable bases: 380. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 380 | 0.2520 | 0.2463 |
| rnafold | ok | 380 | 0.2323 | 0.2338 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 47 | 0.1641 | -0.0231 |
| seed_p | 47 | 0.4245 | 0.5106 |
| seed_p_vs_seed_pars | 30 | 0.4472 | 0.6428 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
