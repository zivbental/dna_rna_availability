# YDR087C
Status: ok. Length: 905 nt. Measured usable bases: 443. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 443 | 0.3369 | 0.3186 |
| rnafold | ok | 443 | 0.2997 | 0.2982 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | -0.0488 | -0.3777 |
| seed_p | 91 | 0.1104 | 0.1099 |
| seed_p_vs_seed_pars | 78 | 0.2094 | 0.0954 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
