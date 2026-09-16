# YJL129C
Status: ok. Length: 3915 nt. Measured usable bases: 1424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1424 | 0.3061 | 0.2947 |
| rnafold | ok | 1424 | 0.2640 | 0.2593 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | 0.2758 | 0.1662 |
| seed_p | 147 | 0.2528 | 0.1846 |
| seed_p_vs_seed_pars | 130 | -0.0033 | -0.1322 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
