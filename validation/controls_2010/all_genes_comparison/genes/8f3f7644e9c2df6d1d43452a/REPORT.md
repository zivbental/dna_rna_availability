# YNL007C
Status: ok. Length: 1213 nt. Measured usable bases: 877. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 877 | 0.3748 | 0.3705 |
| rnafold | ok | 877 | 0.3003 | 0.2986 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 595 | -0.2013 | -0.2868 |
| seed_p | 595 | -0.3230 | -0.3475 |
| seed_p_vs_seed_pars | 449 | -0.4102 | -0.3918 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
