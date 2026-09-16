# YOR014W
Status: ok. Length: 2593 nt. Measured usable bases: 1245. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1245 | 0.1832 | 0.1677 |
| rnafold | ok | 1245 | 0.1863 | 0.1758 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 141 | 0.1824 | 0.3419 |
| seed_p | 141 | 0.3088 | 0.3001 |
| seed_p_vs_seed_pars | 80 | 0.1360 | 0.1119 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
