# YNL046W
Status: ok. Length: 767 nt. Measured usable bases: 476. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 476 | 0.3238 | 0.3135 |
| rnafold | ok | 476 | 0.0881 | 0.1107 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 249 | 0.0937 | 0.1699 |
| seed_p | 249 | -0.3149 | -0.1523 |
| seed_p_vs_seed_pars | 234 | -0.5589 | -0.5118 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
