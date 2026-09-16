# YEL051W
Status: ok. Length: 922 nt. Measured usable bases: 724. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 724 | 0.3933 | 0.3722 |
| rnafold | ok | 724 | 0.3681 | 0.3500 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 630 | -0.0397 | -0.1814 |
| seed_p | 630 | -0.1306 | -0.1013 |
| seed_p_vs_seed_pars | 534 | -0.1731 | -0.1236 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
