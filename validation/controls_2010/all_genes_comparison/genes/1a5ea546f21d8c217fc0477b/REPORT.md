# YNL024C-A
Status: ok. Length: 533 nt. Measured usable bases: 347. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 347 | 0.2939 | 0.2790 |
| rnafold | ok | 347 | 0.2991 | 0.2923 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 172 | 0.0352 | -0.0362 |
| seed_p | 172 | -0.2271 | -0.2290 |
| seed_p_vs_seed_pars | 126 | -0.4100 | -0.4196 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
