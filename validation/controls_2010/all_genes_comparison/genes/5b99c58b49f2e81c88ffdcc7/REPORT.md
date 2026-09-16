# YDL217C
Status: ok. Length: 925 nt. Measured usable bases: 415. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 415 | 0.3530 | 0.3670 |
| rnafold | ok | 415 | 0.2928 | 0.3133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 76 | -0.2395 | -0.1222 |
| seed_p | 76 | 0.3041 | 0.2807 |
| seed_p_vs_seed_pars | 45 | -0.7378 | -0.7957 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
