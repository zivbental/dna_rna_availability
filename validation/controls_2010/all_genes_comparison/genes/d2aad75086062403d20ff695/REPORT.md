# YMR276W
Status: ok. Length: 1252 nt. Measured usable bases: 1071. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1071 | 0.3667 | 0.3603 |
| rnafold | ok | 1071 | 0.3095 | 0.3086 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 969 | -0.3614 | -0.2991 |
| seed_p | 969 | -0.4104 | -0.3239 |
| seed_p_vs_seed_pars | 877 | -0.5378 | -0.4464 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
