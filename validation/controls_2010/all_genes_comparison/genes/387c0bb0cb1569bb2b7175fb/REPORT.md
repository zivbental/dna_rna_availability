# YER154W
Status: ok. Length: 1297 nt. Measured usable bases: 652. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 652 | 0.2714 | 0.2571 |
| rnafold | ok | 652 | 0.1905 | 0.1775 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 144 | 0.1393 | -0.1681 |
| seed_p | 144 | -0.2804 | -0.2942 |
| seed_p_vs_seed_pars | 94 | -0.5990 | -0.4016 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
