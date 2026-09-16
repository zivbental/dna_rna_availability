# YPR009W
Status: ok. Length: 979 nt. Measured usable bases: 424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 424 | 0.3327 | 0.3546 |
| rnafold | ok | 424 | 0.3063 | 0.3118 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | 0.1189 | 0.3282 |
| seed_p | 42 | -0.6434 | -0.5945 |
| seed_p_vs_seed_pars | 35 | -0.8089 | -0.6845 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
