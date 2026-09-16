# YLR359W
Status: ok. Length: 1643 nt. Measured usable bases: 1368. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1368 | 0.3342 | 0.3314 |
| rnafold | ok | 1368 | 0.2592 | 0.2664 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1210 | -0.1803 | -0.2569 |
| seed_p | 1210 | -0.2446 | -0.2453 |
| seed_p_vs_seed_pars | 977 | -0.4031 | -0.3274 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
