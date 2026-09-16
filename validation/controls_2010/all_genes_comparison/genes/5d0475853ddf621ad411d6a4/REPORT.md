# YOR027W
Status: ok. Length: 2045 nt. Measured usable bases: 1488. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1488 | 0.3821 | 0.3855 |
| rnafold | ok | 1488 | 0.3187 | 0.3246 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1122 | -0.2738 | -0.2110 |
| seed_p | 1122 | -0.3855 | -0.3410 |
| seed_p_vs_seed_pars | 927 | -0.3580 | -0.2768 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
