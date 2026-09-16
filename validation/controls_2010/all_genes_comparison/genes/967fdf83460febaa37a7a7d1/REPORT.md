# YOR198C
Status: ok. Length: 1613 nt. Measured usable bases: 1062. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1062 | 0.3468 | 0.3399 |
| rnafold | ok | 1062 | 0.3455 | 0.3477 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 579 | -0.2720 | -0.3129 |
| seed_p | 579 | -0.2972 | -0.2769 |
| seed_p_vs_seed_pars | 452 | -0.3349 | -0.3285 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
