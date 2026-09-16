# YOL014W
Status: ok. Length: 655 nt. Measured usable bases: 290. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 290 | 0.2770 | 0.2839 |
| rnafold | ok | 290 | 0.2303 | 0.2510 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | 0.6893 | 0.6853 |
| seed_p | 58 | 0.7135 | 0.7748 |
| seed_p_vs_seed_pars | 26 | 0.8073 | 0.8295 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
