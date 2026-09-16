# YMR191W
Status: ok. Length: 1311 nt. Measured usable bases: 753. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 753 | 0.2325 | 0.2108 |
| rnafold | ok | 753 | 0.1949 | 0.1877 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 300 | 0.0079 | 0.3948 |
| seed_p | 300 | -0.0456 | -0.0015 |
| seed_p_vs_seed_pars | 213 | -0.1539 | -0.1286 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
