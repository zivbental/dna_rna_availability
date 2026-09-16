# YNR018W
Status: ok. Length: 843 nt. Measured usable bases: 624. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 624 | 0.3280 | 0.2988 |
| rnafold | ok | 624 | 0.3095 | 0.2900 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 561 | -0.0565 | -0.2631 |
| seed_p | 561 | -0.3404 | -0.3243 |
| seed_p_vs_seed_pars | 480 | -0.4685 | -0.4039 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
