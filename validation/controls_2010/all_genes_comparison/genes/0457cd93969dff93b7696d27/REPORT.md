# YDL137W
Status: ok. Length: 1072 nt. Measured usable bases: 561. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 561 | 0.3273 | 0.3007 |
| rnafold | ok | 561 | 0.2364 | 0.2324 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 320 | -0.0465 | -0.1564 |
| seed_p | 320 | -0.2185 | -0.3332 |
| seed_p_vs_seed_pars | 215 | -0.0795 | -0.1746 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
