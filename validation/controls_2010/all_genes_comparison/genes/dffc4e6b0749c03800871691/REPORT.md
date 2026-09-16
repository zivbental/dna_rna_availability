# YNL221C
Status: ok. Length: 2821 nt. Measured usable bases: 1141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1141 | 0.3020 | 0.2900 |
| rnafold | ok | 1141 | 0.2575 | 0.2440 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 76 | 0.0262 | -0.3600 |
| seed_p | 76 | 0.3488 | 0.0922 |
| seed_p_vs_seed_pars | 61 | 0.3720 | 0.1382 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
