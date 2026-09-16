# YOR377W
Status: ok. Length: 1894 nt. Measured usable bases: 745. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 745 | 0.3233 | 0.3195 |
| rnafold | ok | 745 | 0.2778 | 0.2884 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.1487 | -0.3098 |
| seed_p | 43 | -0.1378 | 0.1113 |
| seed_p_vs_seed_pars | 43 | -0.1650 | 0.1479 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
