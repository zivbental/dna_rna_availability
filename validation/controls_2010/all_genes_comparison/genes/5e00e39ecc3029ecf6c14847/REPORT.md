# YLL006W
Status: ok. Length: 1356 nt. Measured usable bases: 517. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 517 | 0.3023 | 0.2791 |
| rnafold | ok | 517 | 0.3195 | 0.2966 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | 0.2663 | -0.0825 |
| seed_p | 31 | -0.1284 | -0.0416 |
| seed_p_vs_seed_pars | 21 | 0.6273 | 0.4828 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
