# YOR084W
Status: ok. Length: 1323 nt. Measured usable bases: 594. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 594 | 0.2581 | 0.2530 |
| rnafold | ok | 594 | 0.2586 | 0.2657 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 102 | 0.3523 | 0.3061 |
| seed_p | 102 | 0.1580 | 0.1028 |
| seed_p_vs_seed_pars | 84 | -0.0312 | -0.0805 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
