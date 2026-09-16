# YJR001W
Status: ok. Length: 1951 nt. Measured usable bases: 1407. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1407 | 0.3220 | 0.2999 |
| rnafold | ok | 1407 | 0.2180 | 0.2051 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 905 | -0.1234 | -0.1827 |
| seed_p | 905 | -0.3483 | -0.2969 |
| seed_p_vs_seed_pars | 695 | -0.4116 | -0.3705 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
