# YNL075W
Status: ok. Length: 1166 nt. Measured usable bases: 510. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 510 | 0.2498 | 0.2631 |
| rnafold | ok | 510 | 0.1917 | 0.2259 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 103 | -0.1075 | -0.2174 |
| seed_p | 103 | -0.1199 | -0.4061 |
| seed_p_vs_seed_pars | 62 | -0.7452 | -0.7292 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
