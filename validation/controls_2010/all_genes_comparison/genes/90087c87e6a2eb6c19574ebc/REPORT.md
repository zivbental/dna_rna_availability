# YCR067C
Status: ok. Length: 3399 nt. Measured usable bases: 1744. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1744 | 0.2227 | 0.2162 |
| rnafold | ok | 1744 | 0.1841 | 0.1793 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 379 | -0.1115 | -0.0702 |
| seed_p | 379 | -0.0904 | -0.0981 |
| seed_p_vs_seed_pars | 259 | -0.1451 | -0.1382 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
