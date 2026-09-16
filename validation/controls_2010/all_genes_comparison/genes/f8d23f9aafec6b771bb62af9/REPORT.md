# YCR061W
Status: ok. Length: 2314 nt. Measured usable bases: 1059. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1059 | 0.2997 | 0.2807 |
| rnafold | ok | 1059 | 0.2649 | 0.2525 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | -0.1296 | -0.0111 |
| seed_p | 124 | -0.3223 | 0.0375 |
| seed_p_vs_seed_pars | 92 | -0.6359 | -0.0957 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
