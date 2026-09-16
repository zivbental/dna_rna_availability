# YGL068W
Status: ok. Length: 743 nt. Measured usable bases: 608. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 608 | 0.2650 | 0.2408 |
| rnafold | ok | 608 | 0.1818 | 0.1845 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 526 | 0.0540 | -0.2204 |
| seed_p | 526 | -0.0670 | -0.1227 |
| seed_p_vs_seed_pars | 489 | -0.1246 | -0.1336 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
