# YBL061C
Status: ok. Length: 2271 nt. Measured usable bases: 861.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 861 | 0.3578 | 0.3334 |
| rnafold | ok | 861 | 0.3479 | 0.3200 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 56 | -0.0214 | 0.1296 |
| seed_p | 56 | -0.0981 | -0.0833 |
| seed_p_vs_seed_pars | 40 | -0.1900 | 0.0597 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
