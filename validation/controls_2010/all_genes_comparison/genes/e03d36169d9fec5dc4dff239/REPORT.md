# YPL091W
Status: ok. Length: 1625 nt. Measured usable bases: 1140. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1140 | 0.3595 | 0.3641 |
| rnafold | ok | 1140 | 0.2920 | 0.2861 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 733 | -0.1297 | -0.1200 |
| seed_p | 733 | -0.1753 | -0.2247 |
| seed_p_vs_seed_pars | 602 | -0.2118 | -0.3352 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
