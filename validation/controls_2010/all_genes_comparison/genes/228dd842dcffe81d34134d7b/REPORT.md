# YBR159W
Status: ok. Length: 1272 nt. Measured usable bases: 921. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 921 | 0.3445 | 0.3230 |
| rnafold | ok | 921 | 0.3275 | 0.3068 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 712 | -0.1208 | -0.1901 |
| seed_p | 712 | -0.2456 | -0.2549 |
| seed_p_vs_seed_pars | 635 | -0.3084 | -0.2710 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
