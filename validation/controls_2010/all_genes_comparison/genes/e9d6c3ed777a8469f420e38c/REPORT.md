# YAL046C
Status: ok. Length: 524 nt. Measured usable bases: 306. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 306 | 0.3230 | 0.3064 |
| rnafold | ok | 306 | 0.2718 | 0.2763 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 171 | -0.2426 | -0.0905 |
| seed_p | 171 | -0.1744 | -0.0773 |
| seed_p_vs_seed_pars | 95 | 0.3059 | 0.2050 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
