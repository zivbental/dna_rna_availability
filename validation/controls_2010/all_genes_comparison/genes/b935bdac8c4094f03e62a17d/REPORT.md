# YDR456W
Status: ok. Length: 1975 nt. Measured usable bases: 1217. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1217 | 0.2226 | 0.2339 |
| rnafold | ok | 1217 | 0.2157 | 0.2294 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 461 | -0.0344 | 0.0068 |
| seed_p | 461 | 0.3113 | 0.1840 |
| seed_p_vs_seed_pars | 266 | 0.2895 | 0.2324 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
