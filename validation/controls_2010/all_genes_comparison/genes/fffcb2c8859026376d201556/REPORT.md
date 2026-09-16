# YHR111W
Status: ok. Length: 1323 nt. Measured usable bases: 645. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 645 | 0.3491 | 0.3407 |
| rnafold | ok | 645 | 0.3260 | 0.3325 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | -0.0054 | 0.0051 |
| seed_p | 71 | -0.2884 | -0.3372 |
| seed_p_vs_seed_pars | 40 | -0.3713 | -0.3094 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
