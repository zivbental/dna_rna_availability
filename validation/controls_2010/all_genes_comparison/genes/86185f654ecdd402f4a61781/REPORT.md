# YDR144C
Status: ok. Length: 2021 nt. Measured usable bases: 1441. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1441 | 0.2722 | 0.2548 |
| rnafold | ok | 1441 | 0.2269 | 0.2139 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 815 | -0.2157 | -0.1183 |
| seed_p | 815 | -0.3244 | -0.2098 |
| seed_p_vs_seed_pars | 599 | -0.4306 | -0.3061 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
