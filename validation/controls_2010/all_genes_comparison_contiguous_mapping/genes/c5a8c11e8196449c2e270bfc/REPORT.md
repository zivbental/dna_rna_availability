# YAR027W
Status: ok. Length: 895 nt. Measured usable bases: 467.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 467 | 0.3679 | 0.3702 |
| rnafold | ok | 467 | 0.3239 | 0.3197 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 106 | -0.1482 | 0.0027 |
| seed_p | 106 | -0.2308 | 0.0400 |
| seed_p_vs_seed_pars | 82 | -0.4022 | -0.4495 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
