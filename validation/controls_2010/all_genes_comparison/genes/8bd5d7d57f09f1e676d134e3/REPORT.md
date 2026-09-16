# YNR040W
Status: ok. Length: 855 nt. Measured usable bases: 367. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 367 | 0.3312 | 0.3168 |
| rnafold | ok | 367 | 0.2543 | 0.2497 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | 0.0025 | 0.4561 |
| seed_p | 61 | -0.3207 | -0.0610 |
| seed_p_vs_seed_pars | 27 | -0.2359 | -0.4170 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
