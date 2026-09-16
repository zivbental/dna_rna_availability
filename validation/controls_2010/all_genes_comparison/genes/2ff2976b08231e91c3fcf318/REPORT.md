# YJL151C
Status: ok. Length: 471 nt. Measured usable bases: 388. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 388 | 0.2748 | 0.2541 |
| rnafold | ok | 388 | 0.2577 | 0.2306 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 319 | -0.1494 | -0.2267 |
| seed_p | 319 | -0.3186 | -0.2525 |
| seed_p_vs_seed_pars | 283 | -0.3294 | -0.3475 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
