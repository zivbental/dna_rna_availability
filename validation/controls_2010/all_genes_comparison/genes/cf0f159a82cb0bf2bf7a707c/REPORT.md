# YHR066W
Status: ok. Length: 1510 nt. Measured usable bases: 489. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 489 | 0.2713 | 0.2464 |
| rnafold | ok | 489 | 0.2397 | 0.2194 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | -0.4897 | -0.0667 |
| seed_p | 35 | -0.0707 | -0.2210 |
| seed_p_vs_seed_pars | 26 | 0.0409 | -0.1440 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
