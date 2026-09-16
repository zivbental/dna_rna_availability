# YGL082W
Status: ok. Length: 1381 nt. Measured usable bases: 676. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 676 | 0.2722 | 0.2699 |
| rnafold | ok | 676 | 0.2624 | 0.2506 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 140 | 0.0937 | 0.1922 |
| seed_p | 140 | 0.0622 | 0.2238 |
| seed_p_vs_seed_pars | 88 | -0.0570 | -0.0846 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
