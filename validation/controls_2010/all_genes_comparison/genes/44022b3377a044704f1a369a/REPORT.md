# YOR253W
Status: ok. Length: 664 nt. Measured usable bases: 399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 399 | 0.4168 | 0.3895 |
| rnafold | ok | 399 | 0.3277 | 0.3230 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 276 | -0.3447 | -0.2669 |
| seed_p | 276 | -0.4185 | -0.3868 |
| seed_p_vs_seed_pars | 187 | -0.4543 | -0.4318 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
