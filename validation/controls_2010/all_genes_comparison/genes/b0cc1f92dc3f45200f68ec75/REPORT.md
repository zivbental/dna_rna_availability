# YML010W
Status: ok. Length: 3276 nt. Measured usable bases: 1676. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1676 | 0.3509 | 0.3486 |
| rnafold | ok | 1676 | 0.3143 | 0.3143 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 339 | 0.1128 | 0.1491 |
| seed_p | 339 | 0.0565 | -0.0698 |
| seed_p_vs_seed_pars | 244 | -0.1147 | -0.2379 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
