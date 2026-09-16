# YER018C
Status: ok. Length: 865 nt. Measured usable bases: 468. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 468 | 0.3280 | 0.3374 |
| rnafold | ok | 468 | 0.3178 | 0.3441 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 170 | -0.1660 | -0.1196 |
| seed_p | 170 | -0.2572 | -0.3643 |
| seed_p_vs_seed_pars | 127 | -0.1471 | -0.1607 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
