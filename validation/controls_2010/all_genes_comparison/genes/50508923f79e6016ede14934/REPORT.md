# YNL037C
Status: ok. Length: 1296 nt. Measured usable bases: 943. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 943 | 0.3746 | 0.3744 |
| rnafold | ok | 943 | 0.3344 | 0.3328 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 700 | -0.0544 | -0.3323 |
| seed_p | 700 | -0.3651 | -0.3639 |
| seed_p_vs_seed_pars | 594 | -0.4607 | -0.4674 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
