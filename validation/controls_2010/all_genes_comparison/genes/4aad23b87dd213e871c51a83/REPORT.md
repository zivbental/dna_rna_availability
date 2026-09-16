# YDR245W
Status: ok. Length: 1383 nt. Measured usable bases: 922. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 922 | 0.2812 | 0.2743 |
| rnafold | ok | 922 | 0.2827 | 0.2781 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 498 | -0.0926 | -0.1223 |
| seed_p | 498 | -0.3098 | -0.2127 |
| seed_p_vs_seed_pars | 385 | -0.3308 | -0.2707 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
