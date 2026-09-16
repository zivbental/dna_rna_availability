# YOL151W
Status: ok. Length: 1118 nt. Measured usable bases: 705. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 705 | 0.3962 | 0.3977 |
| rnafold | ok | 705 | 0.3560 | 0.3452 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 340 | -0.0338 | -0.2968 |
| seed_p | 340 | -0.3023 | -0.2955 |
| seed_p_vs_seed_pars | 237 | -0.4529 | -0.4424 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
