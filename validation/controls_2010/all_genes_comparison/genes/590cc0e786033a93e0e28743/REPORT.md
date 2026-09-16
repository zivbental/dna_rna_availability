# YJR101W
Status: ok. Length: 1027 nt. Measured usable bases: 587. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 587 | 0.2794 | 0.2699 |
| rnafold | ok | 587 | 0.2356 | 0.2583 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 160 | -0.0274 | 0.0167 |
| seed_p | 160 | -0.3647 | -0.2843 |
| seed_p_vs_seed_pars | 105 | -0.3860 | -0.4361 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
