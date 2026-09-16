# YDR156W
Status: ok. Length: 544 nt. Measured usable bases: 378. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 378 | 0.3272 | 0.3018 |
| rnafold | ok | 378 | 0.3018 | 0.2645 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | -0.1112 | -0.2655 |
| seed_p | 246 | -0.4424 | -0.3546 |
| seed_p_vs_seed_pars | 224 | -0.5464 | -0.5623 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
