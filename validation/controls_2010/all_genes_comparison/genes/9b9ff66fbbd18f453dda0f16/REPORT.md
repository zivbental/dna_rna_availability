# YPL231W
Status: ok. Length: 5830 nt. Measured usable bases: 4825. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 4825 | 0.3708 | 0.3433 |
| rnafold | ok | 4825 | 0.3065 | 0.2881 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 4195 | -0.0799 | -0.1013 |
| seed_p | 4195 | -0.2439 | -0.1792 |
| seed_p_vs_seed_pars | 3479 | -0.3906 | -0.3500 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
