# YML098W
Status: ok. Length: 739 nt. Measured usable bases: 334. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 334 | 0.3039 | 0.3080 |
| rnafold | ok | 334 | 0.3182 | 0.3297 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | -0.6439 | -0.4582 |
| seed_p | 55 | -0.6482 | -0.3455 |
| seed_p_vs_seed_pars | 41 | -0.4070 | -0.3878 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
