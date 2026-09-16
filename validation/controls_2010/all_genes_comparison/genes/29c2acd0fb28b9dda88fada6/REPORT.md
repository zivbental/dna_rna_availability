# YJR063W
Status: ok. Length: 551 nt. Measured usable bases: 383. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 383 | 0.2609 | 0.2453 |
| rnafold | ok | 383 | 0.1625 | 0.1569 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 226 | 0.0739 | -0.1612 |
| seed_p | 226 | -0.2994 | -0.4351 |
| seed_p_vs_seed_pars | 189 | -0.3033 | -0.4101 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
