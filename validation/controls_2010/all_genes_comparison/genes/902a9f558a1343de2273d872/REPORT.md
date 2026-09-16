# YJR042W
Status: ok. Length: 2391 nt. Measured usable bases: 1096. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1096 | 0.2641 | 0.2624 |
| rnafold | ok | 1096 | 0.1951 | 0.1909 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 152 | -0.0978 | -0.2070 |
| seed_p | 152 | 0.1589 | 0.1514 |
| seed_p_vs_seed_pars | 110 | -0.0537 | -0.0388 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
