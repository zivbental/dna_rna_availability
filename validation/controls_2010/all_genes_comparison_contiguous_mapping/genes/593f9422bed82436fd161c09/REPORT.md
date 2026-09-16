# YBL011W
Status: ok. Length: 2486 nt. Measured usable bases: 1327.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1327 | 0.2915 | 0.2854 |
| rnafold | ok | 1327 | 0.2950 | 0.2968 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 348 | -0.0698 | -0.1156 |
| seed_p | 348 | 0.1326 | 0.1840 |
| seed_p_vs_seed_pars | 269 | 0.1262 | 0.0761 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
