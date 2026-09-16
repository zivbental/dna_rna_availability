# YHR143W
Status: ok. Length: 1488 nt. Measured usable bases: 1115. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1115 | 0.1505 | 0.1266 |
| rnafold | ok | 1115 | 0.1610 | 0.1501 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 863 | -0.1543 | -0.1241 |
| seed_p | 863 | -0.1178 | -0.0574 |
| seed_p_vs_seed_pars | 766 | -0.2076 | -0.1196 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
