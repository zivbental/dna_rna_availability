# YHR198C
Status: ok. Length: 966 nt. Measured usable bases: 469. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 469 | 0.3190 | 0.3130 |
| rnafold | ok | 469 | 0.2901 | 0.2928 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | -0.0704 | -0.0729 |
| seed_p | 62 | -0.3878 | -0.4268 |
| seed_p_vs_seed_pars | 34 | -0.3878 | -0.3557 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
