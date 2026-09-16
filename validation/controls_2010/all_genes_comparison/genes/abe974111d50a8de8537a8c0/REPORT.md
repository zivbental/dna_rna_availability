# YOR098C
Status: ok. Length: 3362 nt. Measured usable bases: 1681. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1681 | 0.3136 | 0.2918 |
| rnafold | ok | 1681 | 0.2468 | 0.2361 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 276 | -0.2215 | -0.0844 |
| seed_p | 276 | -0.0671 | -0.0548 |
| seed_p_vs_seed_pars | 183 | -0.3611 | -0.3967 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
