# YCL034W
Status: ok. Length: 1269 nt. Measured usable bases: 789. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 789 | 0.2488 | 0.2282 |
| rnafold | ok | 789 | 0.2296 | 0.2180 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 434 | -0.2375 | 0.1040 |
| seed_p | 434 | -0.1832 | 0.0327 |
| seed_p_vs_seed_pars | 359 | -0.2124 | -0.1440 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
