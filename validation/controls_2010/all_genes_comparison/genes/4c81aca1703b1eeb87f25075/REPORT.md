# YHR018C
Status: ok. Length: 1582 nt. Measured usable bases: 965. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 965 | 0.3319 | 0.3175 |
| rnafold | ok | 965 | 0.2225 | 0.2223 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 414 | -0.0290 | -0.0669 |
| seed_p | 414 | -0.1306 | -0.0335 |
| seed_p_vs_seed_pars | 337 | -0.2357 | -0.1131 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
