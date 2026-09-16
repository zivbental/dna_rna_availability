# YKL068W
Status: ok. Length: 3117 nt. Measured usable bases: 1476. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1476 | 0.3662 | 0.3509 |
| rnafold | ok | 1476 | 0.3073 | 0.3126 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 184 | -0.0028 | 0.0633 |
| seed_p | 184 | -0.3521 | -0.2501 |
| seed_p_vs_seed_pars | 151 | -0.3901 | -0.3940 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
