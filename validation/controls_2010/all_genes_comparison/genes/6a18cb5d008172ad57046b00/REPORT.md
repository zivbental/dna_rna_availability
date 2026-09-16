# YHR179W
Status: ok. Length: 1355 nt. Measured usable bases: 1187. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1187 | 0.3116 | 0.2923 |
| rnafold | ok | 1187 | 0.3076 | 0.2848 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1184 | 0.1295 | -0.0509 |
| seed_p | 1184 | 0.0440 | -0.0114 |
| seed_p_vs_seed_pars | 1062 | -0.1720 | -0.1977 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
