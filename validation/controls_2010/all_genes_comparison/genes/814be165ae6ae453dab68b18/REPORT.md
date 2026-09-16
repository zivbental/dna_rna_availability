# YML048W
Status: ok. Length: 1440 nt. Measured usable bases: 1084. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1084 | 0.3638 | 0.3535 |
| rnafold | ok | 1084 | 0.3306 | 0.3206 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 864 | -0.1280 | -0.1219 |
| seed_p | 864 | -0.1757 | -0.0930 |
| seed_p_vs_seed_pars | 706 | -0.4131 | -0.2148 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
