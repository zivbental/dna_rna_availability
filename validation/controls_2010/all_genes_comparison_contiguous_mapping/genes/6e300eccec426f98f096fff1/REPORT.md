# YBR061C
Status: ok. Length: 1144 nt. Measured usable bases: 561.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 561 | 0.3193 | 0.3039 |
| rnafold | ok | 561 | 0.3066 | 0.2939 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 107 | -0.3641 | -0.1039 |
| seed_p | 107 | -0.3015 | -0.0609 |
| seed_p_vs_seed_pars | 94 | -0.3715 | -0.2269 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
