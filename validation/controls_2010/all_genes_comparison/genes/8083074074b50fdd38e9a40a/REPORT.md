# YER156C
Status: ok. Length: 1121 nt. Measured usable bases: 809. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 809 | 0.3717 | 0.3668 |
| rnafold | ok | 809 | 0.2652 | 0.2587 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 523 | -0.3054 | -0.1702 |
| seed_p | 523 | -0.2790 | -0.1127 |
| seed_p_vs_seed_pars | 397 | -0.3362 | -0.2488 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
