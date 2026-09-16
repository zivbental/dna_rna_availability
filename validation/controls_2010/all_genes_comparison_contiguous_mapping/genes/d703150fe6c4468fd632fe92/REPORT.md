# YBL001C
Status: ok. Length: 423 nt. Measured usable bases: 315.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 315 | 0.3316 | 0.3320 |
| rnafold | ok | 315 | 0.2695 | 0.2794 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 249 | -0.1249 | -0.5169 |
| seed_p | 249 | -0.1265 | -0.2218 |
| seed_p_vs_seed_pars | 236 | -0.1926 | -0.1598 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
