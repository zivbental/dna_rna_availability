# YMR031C
Status: ok. Length: 2696 nt. Measured usable bases: 1082. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1082 | 0.3527 | 0.3584 |
| rnafold | ok | 1082 | 0.3416 | 0.3540 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | 0.2035 | 0.1768 |
| seed_p | 101 | 0.1167 | 0.0862 |
| seed_p_vs_seed_pars | 66 | -0.3799 | -0.4962 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
