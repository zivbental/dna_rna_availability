# YDL047W
Status: ok. Length: 1315 nt. Measured usable bases: 713. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 713 | 0.3433 | 0.3262 |
| rnafold | ok | 713 | 0.2209 | 0.2206 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 181 | -0.2766 | -0.2273 |
| seed_p | 181 | -0.4368 | -0.2715 |
| seed_p_vs_seed_pars | 141 | -0.6461 | -0.5645 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
