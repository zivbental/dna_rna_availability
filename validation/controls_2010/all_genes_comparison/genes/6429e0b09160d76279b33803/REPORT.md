# YEL006W
Status: ok. Length: 1195 nt. Measured usable bases: 643. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 643 | 0.3443 | 0.3242 |
| rnafold | ok | 643 | 0.3166 | 0.3001 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 251 | -0.4258 | -0.3243 |
| seed_p | 251 | -0.4379 | -0.3960 |
| seed_p_vs_seed_pars | 198 | -0.3696 | -0.3958 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
