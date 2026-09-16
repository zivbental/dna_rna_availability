# YOR303W
Status: ok. Length: 1297 nt. Measured usable bases: 908. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 908 | 0.2970 | 0.2803 |
| rnafold | ok | 908 | 0.2522 | 0.2379 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 472 | 0.1257 | 0.2090 |
| seed_p | 472 | 0.1391 | 0.1389 |
| seed_p_vs_seed_pars | 390 | 0.1003 | 0.1173 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
