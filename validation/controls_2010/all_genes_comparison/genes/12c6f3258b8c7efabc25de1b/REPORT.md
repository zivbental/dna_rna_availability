# YDL124W
Status: ok. Length: 1068 nt. Measured usable bases: 744. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 744 | 0.2970 | 0.2938 |
| rnafold | ok | 744 | 0.2441 | 0.2424 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 465 | -0.0642 | 0.0656 |
| seed_p | 465 | -0.0876 | -0.0260 |
| seed_p_vs_seed_pars | 328 | -0.1420 | -0.0737 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
