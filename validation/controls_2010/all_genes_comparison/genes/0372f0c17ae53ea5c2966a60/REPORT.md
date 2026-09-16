# YBR286W
Status: ok. Length: 1697 nt. Measured usable bases: 1557. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1557 | 0.3130 | 0.2916 |
| rnafold | ok | 1557 | 0.2437 | 0.2345 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1539 | -0.1447 | -0.1531 |
| seed_p | 1539 | -0.2960 | -0.2360 |
| seed_p_vs_seed_pars | 1495 | -0.3258 | -0.2676 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
