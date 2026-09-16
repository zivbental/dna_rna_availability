# YBL069W
Status: ok. Length: 1429 nt. Measured usable bases: 695.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 695 | 0.3184 | 0.3290 |
| rnafold | ok | 695 | 0.2813 | 0.3070 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | -0.1558 | 0.1107 |
| seed_p | 109 | 0.3576 | 0.3483 |
| seed_p_vs_seed_pars | 81 | 0.2350 | 0.1935 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
