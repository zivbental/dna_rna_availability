# YAL016W
Status: ok. Length: 1978 nt. Measured usable bases: 1267.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1267 | 0.2474 | 0.2207 |
| rnafold | ok | 1267 | 0.2391 | 0.2147 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 590 | 0.0891 | 0.2389 |
| seed_p | 590 | 0.1647 | 0.1711 |
| seed_p_vs_seed_pars | 427 | 0.0825 | 0.0621 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
