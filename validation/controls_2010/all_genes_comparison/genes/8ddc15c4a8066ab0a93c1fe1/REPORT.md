# YNL056W
Status: ok. Length: 750 nt. Measured usable bases: 450. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 450 | 0.3003 | 0.2956 |
| rnafold | ok | 450 | 0.1552 | 0.1623 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 139 | -0.1311 | -0.4489 |
| seed_p | 139 | -0.4296 | -0.4122 |
| seed_p_vs_seed_pars | 113 | -0.6681 | -0.6110 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
