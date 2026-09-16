# YBR054W
Status: ok. Length: 1713 nt. Measured usable bases: 705. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 705 | 0.2620 | 0.2653 |
| rnafold | ok | 705 | 0.2468 | 0.2499 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 114 | -0.5183 | -0.3305 |
| seed_p | 114 | -0.2878 | -0.3214 |
| seed_p_vs_seed_pars | 86 | -0.4428 | -0.2872 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
