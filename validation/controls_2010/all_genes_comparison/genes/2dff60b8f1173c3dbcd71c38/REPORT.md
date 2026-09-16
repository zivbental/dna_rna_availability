# YOR276W
Status: ok. Length: 620 nt. Measured usable bases: 491. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 491 | 0.3167 | 0.3106 |
| rnafold | ok | 491 | 0.3599 | 0.3969 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 423 | -0.2714 | -0.3381 |
| seed_p | 423 | -0.3048 | -0.2349 |
| seed_p_vs_seed_pars | 343 | -0.3921 | -0.2070 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
