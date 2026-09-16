# YOR165W
Status: ok. Length: 2503 nt. Measured usable bases: 1037. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1037 | 0.3253 | 0.3176 |
| rnafold | ok | 1037 | 0.2973 | 0.3016 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 85 | 0.0013 | 0.2528 |
| seed_p | 85 | -0.0633 | -0.1580 |
| seed_p_vs_seed_pars | 72 | -0.2389 | -0.1438 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
