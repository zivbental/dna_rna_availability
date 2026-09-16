# YKL195W
Status: ok. Length: 1364 nt. Measured usable bases: 489. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 489 | 0.4374 | 0.4585 |
| rnafold | ok | 489 | 0.4047 | 0.4369 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | -0.2543 | -0.3516 |
| seed_p | 42 | -0.2975 | -0.3991 |
| seed_p_vs_seed_pars | 25 | -0.2129 | -0.5145 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
