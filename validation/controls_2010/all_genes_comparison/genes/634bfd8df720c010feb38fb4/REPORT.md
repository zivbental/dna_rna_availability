# YHR112C
Status: ok. Length: 1378 nt. Measured usable bases: 650. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 650 | 0.2704 | 0.2616 |
| rnafold | ok | 650 | 0.2488 | 0.2508 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 142 | -0.3700 | -0.3320 |
| seed_p | 142 | 0.3657 | 0.2031 |
| seed_p_vs_seed_pars | 93 | 0.3143 | 0.0932 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
