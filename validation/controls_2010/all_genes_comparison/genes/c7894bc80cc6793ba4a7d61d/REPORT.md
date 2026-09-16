# YAL009W
Status: ok. Length: 921 nt. Measured usable bases: 380. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 380 | 0.3379 | 0.3068 |
| rnafold | ok | 380 | 0.3516 | 0.3042 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.6015 | 0.5849 |
| seed_p | 67 | 0.2426 | 0.2692 |
| seed_p_vs_seed_pars | 46 | 0.1750 | 0.5394 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
