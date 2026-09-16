# YGR103W
Status: ok. Length: 2004 nt. Measured usable bases: 1148. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1148 | 0.3284 | 0.3134 |
| rnafold | ok | 1148 | 0.3245 | 0.3136 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 376 | -0.0513 | 0.0376 |
| seed_p | 376 | -0.1051 | -0.1346 |
| seed_p_vs_seed_pars | 261 | -0.1505 | -0.1295 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
