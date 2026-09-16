# YGL228W
Status: ok. Length: 1921 nt. Measured usable bases: 1010. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1010 | 0.3593 | 0.3485 |
| rnafold | ok | 1010 | 0.2514 | 0.2341 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 324 | 0.2201 | 0.0574 |
| seed_p | 324 | 0.0942 | 0.1729 |
| seed_p_vs_seed_pars | 273 | -0.1469 | -0.0151 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
