# YGR165W
Status: ok. Length: 1214 nt. Measured usable bases: 676. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 676 | 0.3549 | 0.3477 |
| rnafold | ok | 676 | 0.3064 | 0.3118 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 131 | -0.0361 | -0.4186 |
| seed_p | 131 | -0.5924 | -0.4993 |
| seed_p_vs_seed_pars | 90 | -0.3816 | -0.0580 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
