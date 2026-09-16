# YNL209W
Status: ok. Length: 1987 nt. Measured usable bases: 504. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 504 | 0.3026 | 0.3048 |
| rnafold | ok | 504 | 0.3259 | 0.3452 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 261 | -0.3606 | -0.3344 |
| seed_p | 261 | -0.2314 | -0.1844 |
| seed_p_vs_seed_pars | 250 | -0.2740 | -0.2257 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
