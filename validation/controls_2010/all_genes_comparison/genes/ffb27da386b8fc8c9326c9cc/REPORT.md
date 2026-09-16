# YJL111W
Status: ok. Length: 1949 nt. Measured usable bases: 1244. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1244 | 0.3413 | 0.3437 |
| rnafold | ok | 1244 | 0.2423 | 0.2463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 623 | -0.0784 | -0.0519 |
| seed_p | 623 | -0.0424 | -0.0867 |
| seed_p_vs_seed_pars | 395 | -0.1246 | -0.1795 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
