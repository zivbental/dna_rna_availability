# YOR310C
Status: ok. Length: 1637 nt. Measured usable bases: 1122. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1122 | 0.3366 | 0.3284 |
| rnafold | ok | 1122 | 0.3118 | 0.3243 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 712 | -0.1498 | -0.0985 |
| seed_p | 712 | -0.3437 | -0.1165 |
| seed_p_vs_seed_pars | 568 | -0.5146 | -0.2746 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
