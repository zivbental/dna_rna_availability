# YOR260W
Status: ok. Length: 1990 nt. Measured usable bases: 1261. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1261 | 0.2413 | 0.2307 |
| rnafold | ok | 1261 | 0.2014 | 0.1995 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 582 | 0.2066 | 0.2257 |
| seed_p | 582 | 0.2155 | 0.1739 |
| seed_p_vs_seed_pars | 444 | 0.2225 | 0.1679 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
