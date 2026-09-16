# YHL004W
Status: ok. Length: 1368 nt. Measured usable bases: 713. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 713 | 0.3666 | 0.3442 |
| rnafold | ok | 713 | 0.3487 | 0.3305 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 116 | 0.0795 | -0.1067 |
| seed_p | 116 | -0.2715 | -0.3298 |
| seed_p_vs_seed_pars | 79 | -0.4438 | -0.5686 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
