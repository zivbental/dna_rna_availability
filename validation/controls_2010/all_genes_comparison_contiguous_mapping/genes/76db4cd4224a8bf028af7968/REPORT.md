# YBL068W
Status: ok. Length: 1122 nt. Measured usable bases: 690.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 690 | 0.2983 | 0.2969 |
| rnafold | ok | 690 | 0.2071 | 0.2069 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 284 | 0.1969 | -0.0772 |
| seed_p | 284 | 0.0067 | 0.0235 |
| seed_p_vs_seed_pars | 215 | -0.1221 | -0.1306 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
