# YAR068W
Status: ok. Length: 486 nt. Measured usable bases: 254.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 254 | 0.0359 | 0.0339 |
| rnafold | ok | 254 | 0.0771 | 0.1189 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | 0.1149 | -0.0090 |
| seed_p | 73 | -0.1820 | -0.1216 |
| seed_p_vs_seed_pars | 39 | -0.2495 | 0.0751 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
