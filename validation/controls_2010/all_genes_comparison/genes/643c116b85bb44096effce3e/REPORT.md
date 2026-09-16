# YEL050C
Status: ok. Length: 1358 nt. Measured usable bases: 658. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 658 | 0.4153 | 0.3837 |
| rnafold | ok | 658 | 0.3836 | 0.3573 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 83 | -0.2613 | -0.2886 |
| seed_p | 83 | -0.1574 | 0.1318 |
| seed_p_vs_seed_pars | 49 | -0.0194 | 0.0681 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
