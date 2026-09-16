# YJL050W
Status: ok. Length: 3454 nt. Measured usable bases: 1593. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1593 | 0.3314 | 0.3136 |
| rnafold | ok | 1593 | 0.2594 | 0.2533 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 296 | 0.0046 | 0.1100 |
| seed_p | 296 | 0.0459 | 0.1117 |
| seed_p_vs_seed_pars | 217 | -0.1051 | -0.0030 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
