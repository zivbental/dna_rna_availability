# YDR296W
Status: ok. Length: 812 nt. Measured usable bases: 399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 399 | 0.2327 | 0.2292 |
| rnafold | ok | 399 | 0.1296 | 0.1239 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | -0.1593 | -0.3780 |
| seed_p | 67 | -0.2447 | -0.1450 |
| seed_p_vs_seed_pars | 46 | -0.1303 | -0.1442 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
