# YOR197W
Status: ok. Length: 1369 nt. Measured usable bases: 1030. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1030 | 0.3300 | 0.3187 |
| rnafold | ok | 1030 | 0.2762 | 0.2955 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 739 | -0.1539 | -0.2400 |
| seed_p | 739 | -0.4438 | -0.4116 |
| seed_p_vs_seed_pars | 573 | -0.3956 | -0.3686 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
