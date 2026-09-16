# YML063W
Status: ok. Length: 861 nt. Measured usable bases: 528. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 528 | 0.2805 | 0.2754 |
| rnafold | ok | 528 | 0.2489 | 0.2434 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 316 | -0.1309 | -0.4038 |
| seed_p | 316 | -0.2646 | -0.3023 |
| seed_p_vs_seed_pars | 274 | -0.2924 | -0.3321 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
