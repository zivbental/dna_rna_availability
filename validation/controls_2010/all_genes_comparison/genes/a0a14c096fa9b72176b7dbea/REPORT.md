# YBL009W
Status: ok. Length: 2187 nt. Measured usable bases: 859. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 859 | 0.3360 | 0.3147 |
| rnafold | ok | 859 | 0.2139 | 0.1950 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | 0.0643 | 0.2002 |
| seed_p | 42 | -0.6603 | -0.6101 |
| seed_p_vs_seed_pars | 24 | -0.9579 | -0.9575 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
