# YJL148W
Status: ok. Length: 807 nt. Measured usable bases: 428. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 428 | 0.2996 | 0.3028 |
| rnafold | ok | 428 | 0.3381 | 0.3537 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | -0.2569 | 0.0495 |
| seed_p | 179 | 0.1972 | 0.2695 |
| seed_p_vs_seed_pars | 105 | -0.2804 | -0.1881 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
