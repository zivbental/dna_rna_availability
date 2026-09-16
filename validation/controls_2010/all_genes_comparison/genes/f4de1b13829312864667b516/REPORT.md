# YOL098C
Status: ok. Length: 3434 nt. Measured usable bases: 1987. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1987 | 0.3131 | 0.3011 |
| rnafold | ok | 1987 | 0.2656 | 0.2686 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 671 | -0.2399 | -0.0877 |
| seed_p | 671 | -0.1038 | -0.1322 |
| seed_p_vs_seed_pars | 484 | -0.2814 | -0.1313 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
