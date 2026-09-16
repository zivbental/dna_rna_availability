# YNL186W
Status: ok. Length: 2723 nt. Measured usable bases: 1126. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1126 | 0.3337 | 0.3068 |
| rnafold | ok | 1126 | 0.2694 | 0.2598 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | -0.0769 | -0.0267 |
| seed_p | 125 | 0.0349 | -0.0509 |
| seed_p_vs_seed_pars | 73 | 0.0143 | 0.0596 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
