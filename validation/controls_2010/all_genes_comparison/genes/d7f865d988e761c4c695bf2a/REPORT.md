# YKL154W
Status: ok. Length: 866 nt. Measured usable bases: 375. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 375 | 0.2535 | 0.2620 |
| rnafold | ok | 375 | 0.2034 | 0.2005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.1561 | -0.4252 |
| seed_p | 81 | -0.1531 | -0.1124 |
| seed_p_vs_seed_pars | 49 | -0.1376 | 0.1187 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
