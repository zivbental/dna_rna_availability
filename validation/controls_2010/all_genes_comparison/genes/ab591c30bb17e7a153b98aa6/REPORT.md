# YOR056C
Status: ok. Length: 1442 nt. Measured usable bases: 636. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 636 | 0.3604 | 0.3510 |
| rnafold | ok | 636 | 0.3646 | 0.3433 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 80 | 0.0482 | 0.1896 |
| seed_p | 80 | -0.0075 | 0.2739 |
| seed_p_vs_seed_pars | 58 | 0.1710 | 0.2540 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
