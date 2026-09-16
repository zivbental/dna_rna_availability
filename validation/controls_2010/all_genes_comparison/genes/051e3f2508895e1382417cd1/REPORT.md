# YCL035C
Status: ok. Length: 469 nt. Measured usable bases: 305. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 305 | 0.2329 | 0.2427 |
| rnafold | ok | 305 | 0.2532 | 0.2455 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 172 | 0.1026 | -0.0830 |
| seed_p | 172 | 0.2777 | 0.2430 |
| seed_p_vs_seed_pars | 150 | -0.0040 | 0.2294 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
