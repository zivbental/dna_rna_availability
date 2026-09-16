# YGR282C
Status: ok. Length: 1141 nt. Measured usable bases: 1016. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1016 | 0.2307 | 0.2205 |
| rnafold | ok | 1016 | 0.1941 | 0.1989 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 980 | -0.0452 | -0.0638 |
| seed_p | 980 | -0.2374 | -0.1697 |
| seed_p_vs_seed_pars | 914 | -0.3266 | -0.2899 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
