# YJL154C
Status: ok. Length: 2918 nt. Measured usable bases: 1253. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1253 | 0.2899 | 0.2765 |
| rnafold | ok | 1253 | 0.1748 | 0.1798 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | -0.1314 | 0.0400 |
| seed_p | 135 | -0.1527 | -0.1029 |
| seed_p_vs_seed_pars | 78 | -0.0025 | 0.0645 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
