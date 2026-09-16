# YFR033C
Status: ok. Length: 675 nt. Measured usable bases: 204. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 204 | 0.3525 | 0.3348 |
| rnafold | ok | 204 | 0.3894 | 0.3482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.3552 | -0.4646 |
| seed_p | 64 | -0.3266 | -0.1405 |
| seed_p_vs_seed_pars | 60 | -0.3609 | -0.3154 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
