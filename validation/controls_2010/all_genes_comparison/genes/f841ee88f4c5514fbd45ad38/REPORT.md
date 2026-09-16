# YDL120W
Status: ok. Length: 776 nt. Measured usable bases: 403. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 403 | 0.2628 | 0.2411 |
| rnafold | ok | 403 | 0.2096 | 0.1919 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | -0.4328 | -0.3983 |
| seed_p | 98 | -0.5830 | -0.3822 |
| seed_p_vs_seed_pars | 60 | -0.1408 | -0.1688 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
