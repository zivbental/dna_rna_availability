# YEL065W
Status: ok. Length: 2098 nt. Measured usable bases: 1299. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1299 | 0.2634 | 0.2549 |
| rnafold | ok | 1299 | 0.2649 | 0.2497 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 529 | -0.1034 | 0.1265 |
| seed_p | 529 | -0.2401 | -0.1651 |
| seed_p_vs_seed_pars | 422 | -0.3674 | -0.2952 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
