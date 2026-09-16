# YJL062W
Status: ok. Length: 2610 nt. Measured usable bases: 1360. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1360 | 0.2794 | 0.2559 |
| rnafold | ok | 1360 | 0.1613 | 0.1645 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 252 | 0.1377 | 0.1302 |
| seed_p | 252 | -0.1270 | -0.0288 |
| seed_p_vs_seed_pars | 156 | -0.0258 | -0.0344 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
