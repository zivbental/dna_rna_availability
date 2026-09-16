# YBR022W
Status: ok. Length: 769 nt. Measured usable bases: 282.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 282 | 0.3831 | 0.3746 |
| rnafold | ok | 282 | 0.3783 | 0.3887 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.4475 | -0.3861 |
| seed_p | 34 | -0.3356 | -0.4551 |
| seed_p_vs_seed_pars | 32 | -0.8984 | -0.9537 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
