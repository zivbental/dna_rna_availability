# YAL059W
Status: ok. Length: 740 nt. Measured usable bases: 345.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 345 | 0.3192 | 0.3404 |
| rnafold | ok | 345 | 0.3070 | 0.3177 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 102 | -0.2892 | -0.3996 |
| seed_p | 102 | -0.2487 | -0.1498 |
| seed_p_vs_seed_pars | 81 | -0.5638 | -0.6419 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
