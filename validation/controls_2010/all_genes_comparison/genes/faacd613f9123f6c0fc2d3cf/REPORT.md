# YOL020W
Status: ok. Length: 2009 nt. Measured usable bases: 1311. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1311 | 0.2858 | 0.2855 |
| rnafold | ok | 1311 | 0.2623 | 0.2528 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 628 | 0.1245 | -0.0104 |
| seed_p | 628 | -0.0577 | 0.0175 |
| seed_p_vs_seed_pars | 483 | -0.3043 | -0.1461 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
