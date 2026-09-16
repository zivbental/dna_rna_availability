# YNR052C
Status: ok. Length: 1431 nt. Measured usable bases: 906. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 906 | 0.3362 | 0.3217 |
| rnafold | ok | 906 | 0.2595 | 0.2409 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 406 | -0.0096 | 0.0296 |
| seed_p | 406 | -0.2296 | -0.0625 |
| seed_p_vs_seed_pars | 324 | -0.3363 | -0.1156 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
