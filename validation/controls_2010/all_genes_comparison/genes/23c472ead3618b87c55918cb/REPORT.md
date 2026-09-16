# YLR335W
Status: ok. Length: 2275 nt. Measured usable bases: 1171. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1171 | 0.3135 | 0.2995 |
| rnafold | ok | 1171 | 0.2519 | 0.2488 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 309 | -0.1271 | -0.2126 |
| seed_p | 309 | -0.3126 | -0.3593 |
| seed_p_vs_seed_pars | 217 | -0.1145 | -0.2003 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
