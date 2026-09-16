# YKL073W
Status: ok. Length: 2833 nt. Measured usable bases: 1383. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1383 | 0.3549 | 0.3430 |
| rnafold | ok | 1383 | 0.2834 | 0.2728 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 288 | 0.0055 | -0.0020 |
| seed_p | 288 | -0.0234 | -0.0900 |
| seed_p_vs_seed_pars | 235 | -0.0530 | -0.1836 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
