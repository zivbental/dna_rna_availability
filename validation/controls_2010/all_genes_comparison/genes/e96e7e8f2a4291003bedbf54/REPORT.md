# YDR032C
Status: ok. Length: 784 nt. Measured usable bases: 672. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 672 | 0.3346 | 0.3225 |
| rnafold | ok | 672 | 0.3426 | 0.3309 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 593 | -0.1086 | -0.2024 |
| seed_p | 593 | -0.2770 | -0.2577 |
| seed_p_vs_seed_pars | 547 | -0.3189 | -0.3738 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
