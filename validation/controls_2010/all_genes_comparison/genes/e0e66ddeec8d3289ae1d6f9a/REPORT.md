# YGL129C
Status: ok. Length: 1564 nt. Measured usable bases: 594. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 594 | 0.3433 | 0.3362 |
| rnafold | ok | 594 | 0.3248 | 0.3230 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.5454 | -0.5160 |
| seed_p | 34 | -0.5692 | -0.4211 |
| seed_p_vs_seed_pars | 29 | -0.8380 | -0.7226 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
