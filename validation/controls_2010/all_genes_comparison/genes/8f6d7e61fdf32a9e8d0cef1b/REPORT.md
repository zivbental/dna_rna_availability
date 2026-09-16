# YML099C
Status: ok. Length: 2760 nt. Measured usable bases: 937. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 937 | 0.2947 | 0.3054 |
| rnafold | ok | 937 | 0.3008 | 0.3068 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.0225 | -0.1088 |
| seed_p | 39 | -0.4468 | -0.4575 |
| seed_p_vs_seed_pars | 24 | -0.3301 | -0.5679 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
