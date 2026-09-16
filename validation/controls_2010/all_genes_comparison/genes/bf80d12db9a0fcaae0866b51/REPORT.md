# YHR117W
Status: ok. Length: 1920 nt. Measured usable bases: 1039. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1039 | 0.3093 | 0.3013 |
| rnafold | ok | 1039 | 0.2775 | 0.2845 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 269 | -0.0378 | -0.2907 |
| seed_p | 269 | -0.2274 | -0.1962 |
| seed_p_vs_seed_pars | 204 | -0.4967 | -0.4524 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
