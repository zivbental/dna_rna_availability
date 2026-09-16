# YIL090W
Status: ok. Length: 1916 nt. Measured usable bases: 1123. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1123 | 0.2823 | 0.2609 |
| rnafold | ok | 1123 | 0.2450 | 0.2154 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 401 | -0.0677 | 0.0744 |
| seed_p | 401 | -0.1477 | -0.0589 |
| seed_p_vs_seed_pars | 319 | -0.3099 | -0.1583 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
