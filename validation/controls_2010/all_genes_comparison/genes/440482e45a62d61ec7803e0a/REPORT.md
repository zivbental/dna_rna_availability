# YPL208W
Status: ok. Length: 1818 nt. Measured usable bases: 925. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 925 | 0.3255 | 0.3124 |
| rnafold | ok | 925 | 0.2497 | 0.2375 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | 0.0215 | -0.2281 |
| seed_p | 203 | -0.3013 | -0.3735 |
| seed_p_vs_seed_pars | 142 | -0.2633 | -0.3845 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
