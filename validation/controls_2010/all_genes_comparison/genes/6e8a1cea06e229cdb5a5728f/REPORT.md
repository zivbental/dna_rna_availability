# YBR171W
Status: ok. Length: 776 nt. Measured usable bases: 359. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 359 | 0.2469 | 0.2519 |
| rnafold | ok | 359 | 0.2247 | 0.2515 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 100 | -0.0605 | 0.1128 |
| seed_p | 100 | -0.3400 | -0.2279 |
| seed_p_vs_seed_pars | 72 | -0.4855 | -0.4012 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
