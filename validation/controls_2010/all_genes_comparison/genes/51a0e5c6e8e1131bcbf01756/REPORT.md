# YPL106C
Status: ok. Length: 2242 nt. Measured usable bases: 1948. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1948 | 0.3600 | 0.3465 |
| rnafold | ok | 1948 | 0.3236 | 0.3082 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1862 | -0.0796 | -0.2120 |
| seed_p | 1862 | -0.3116 | -0.2530 |
| seed_p_vs_seed_pars | 1714 | -0.3303 | -0.2447 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
