# YNL006W
Status: ok. Length: 1120 nt. Measured usable bases: 700. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 700 | 0.3279 | 0.3124 |
| rnafold | ok | 700 | 0.2921 | 0.3030 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 279 | -0.0395 | 0.0932 |
| seed_p | 279 | -0.0809 | 0.0309 |
| seed_p_vs_seed_pars | 196 | -0.1404 | -0.0730 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
