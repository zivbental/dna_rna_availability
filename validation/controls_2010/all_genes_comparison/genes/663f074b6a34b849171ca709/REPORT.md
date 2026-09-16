# YMR049C
Status: ok. Length: 2493 nt. Measured usable bases: 1261. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1261 | 0.3246 | 0.3306 |
| rnafold | ok | 1261 | 0.2632 | 0.2719 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 304 | -0.0278 | 0.0224 |
| seed_p | 304 | -0.0138 | -0.0551 |
| seed_p_vs_seed_pars | 241 | 0.0735 | 0.0760 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
