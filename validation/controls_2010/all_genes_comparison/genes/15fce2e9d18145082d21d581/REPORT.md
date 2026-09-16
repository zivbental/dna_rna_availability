# YDL112W
Status: ok. Length: 4464 nt. Measured usable bases: 1719. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1719 | 0.2662 | 0.2537 |
| rnafold | ok | 1719 | 0.2447 | 0.2267 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 194 | 0.2528 | 0.2524 |
| seed_p | 194 | 0.3534 | 0.3385 |
| seed_p_vs_seed_pars | 130 | 0.2431 | 0.2660 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
