# YDR302W
Status: ok. Length: 861 nt. Measured usable bases: 323. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 323 | 0.1152 | 0.1483 |
| rnafold | ok | 323 | 0.1286 | 0.1465 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | 0.1153 | -0.2535 |
| seed_p | 40 | 0.6225 | 0.4458 |
| seed_p_vs_seed_pars | 39 | 0.1179 | -0.0269 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
