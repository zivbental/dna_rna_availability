# YHR204W
Status: ok. Length: 2720 nt. Measured usable bases: 1434. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1434 | 0.2664 | 0.2500 |
| rnafold | ok | 1434 | 0.2055 | 0.1985 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 359 | -0.0508 | 0.0236 |
| seed_p | 359 | -0.1529 | -0.1266 |
| seed_p_vs_seed_pars | 233 | -0.3206 | -0.2855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
