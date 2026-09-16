# YCL045C
Status: ok. Length: 2359 nt. Measured usable bases: 1701. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1701 | 0.3130 | 0.3030 |
| rnafold | ok | 1701 | 0.2503 | 0.2389 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1039 | -0.1436 | -0.1872 |
| seed_p | 1039 | -0.2379 | -0.1054 |
| seed_p_vs_seed_pars | 829 | -0.2918 | -0.2059 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
