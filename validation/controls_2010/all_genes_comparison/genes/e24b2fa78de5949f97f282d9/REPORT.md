# YGL097W
Status: ok. Length: 1589 nt. Measured usable bases: 1076. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1076 | 0.3380 | 0.3319 |
| rnafold | ok | 1076 | 0.2736 | 0.2881 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 596 | -0.1126 | -0.2898 |
| seed_p | 596 | -0.3175 | -0.3675 |
| seed_p_vs_seed_pars | 427 | -0.3447 | -0.3283 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
