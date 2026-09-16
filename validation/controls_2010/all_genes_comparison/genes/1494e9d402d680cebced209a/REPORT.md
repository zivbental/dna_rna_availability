# YLR099C
Status: ok. Length: 1369 nt. Measured usable bases: 797. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 797 | 0.3024 | 0.3052 |
| rnafold | ok | 797 | 0.3046 | 0.3321 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 323 | 0.1295 | 0.3138 |
| seed_p | 323 | 0.1258 | 0.1987 |
| seed_p_vs_seed_pars | 216 | 0.0060 | 0.0338 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
