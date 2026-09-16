# YDR011W
Status: ok. Length: 4987 nt. Measured usable bases: 3300. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3300 | 0.2886 | 0.2800 |
| rnafold | ok | 3300 | 0.2172 | 0.2203 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1690 | -0.2311 | -0.1880 |
| seed_p | 1690 | -0.1571 | -0.1883 |
| seed_p_vs_seed_pars | 1320 | -0.2253 | -0.2380 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
