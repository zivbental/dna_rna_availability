# YNL151C
Status: ok. Length: 895 nt. Measured usable bases: 376. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 376 | 0.2707 | 0.2655 |
| rnafold | ok | 376 | 0.2532 | 0.2648 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 29 | -0.7288 | -0.9429 |
| seed_p | 29 | -0.5728 | -0.7149 |
| seed_p_vs_seed_pars | 19 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
