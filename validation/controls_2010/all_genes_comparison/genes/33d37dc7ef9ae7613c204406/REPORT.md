# YOR341W
Status: ok. Length: 5379 nt. Measured usable bases: 3434. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3434 | 0.3108 | 0.2925 |
| rnafold | ok | 3434 | 0.2548 | 0.2521 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1493 | -0.0927 | -0.1688 |
| seed_p | 1493 | -0.2245 | -0.2422 |
| seed_p_vs_seed_pars | 1147 | -0.3015 | -0.3202 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
