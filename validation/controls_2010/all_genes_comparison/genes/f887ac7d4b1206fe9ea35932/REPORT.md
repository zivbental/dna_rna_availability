# YDR518W
Status: ok. Length: 1624 nt. Measured usable bases: 1032. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1032 | 0.2956 | 0.2802 |
| rnafold | ok | 1032 | 0.2638 | 0.2579 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 449 | -0.1669 | -0.0823 |
| seed_p | 449 | -0.3957 | -0.2897 |
| seed_p_vs_seed_pars | 350 | -0.5390 | -0.4207 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
