# YKR068C
Status: ok. Length: 769 nt. Measured usable bases: 367. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 367 | 0.2550 | 0.2729 |
| rnafold | ok | 367 | 0.2803 | 0.3049 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | 0.4282 | 0.1524 |
| seed_p | 79 | 0.6243 | 0.6873 |
| seed_p_vs_seed_pars | 68 | 0.6617 | 0.3619 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
