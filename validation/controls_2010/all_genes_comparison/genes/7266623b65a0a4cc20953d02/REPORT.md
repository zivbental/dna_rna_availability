# YJR059W
Status: ok. Length: 2643 nt. Measured usable bases: 1164. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1164 | 0.3287 | 0.3309 |
| rnafold | ok | 1164 | 0.3111 | 0.3013 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | -0.2875 | -0.4008 |
| seed_p | 86 | -0.2069 | -0.2963 |
| seed_p_vs_seed_pars | 38 | -0.2448 | -0.4245 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
