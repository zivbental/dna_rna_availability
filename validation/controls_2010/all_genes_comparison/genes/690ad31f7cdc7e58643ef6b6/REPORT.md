# YHR216W
Status: ok. Length: 1948 nt. Measured usable bases: 994. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 994 | 0.3168 | 0.3104 |
| rnafold | ok | 994 | 0.2566 | 0.2514 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 390 | -0.1328 | -0.2757 |
| seed_p | 390 | -0.2147 | -0.2719 |
| seed_p_vs_seed_pars | 281 | -0.2248 | -0.2374 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
