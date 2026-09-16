# YBR039W
Status: ok. Length: 1208 nt. Measured usable bases: 852.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 852 | 0.3247 | 0.3014 |
| rnafold | ok | 852 | 0.2651 | 0.2686 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 524 | -0.0461 | -0.1592 |
| seed_p | 524 | -0.1158 | -0.1203 |
| seed_p_vs_seed_pars | 363 | -0.1916 | -0.0714 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
