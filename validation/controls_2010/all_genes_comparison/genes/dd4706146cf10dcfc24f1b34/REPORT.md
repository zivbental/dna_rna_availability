# YOR340C
Status: ok. Length: 1159 nt. Measured usable bases: 584. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 584 | 0.4007 | 0.3761 |
| rnafold | ok | 584 | 0.3447 | 0.3215 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 133 | -0.3897 | -0.4497 |
| seed_p | 133 | -0.5200 | -0.6094 |
| seed_p_vs_seed_pars | 99 | -0.4139 | -0.4639 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
