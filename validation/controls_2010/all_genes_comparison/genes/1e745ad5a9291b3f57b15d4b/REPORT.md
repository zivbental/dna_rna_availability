# YJR113C
Status: ok. Length: 858 nt. Measured usable bases: 422. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 422 | 0.3635 | 0.3480 |
| rnafold | ok | 422 | 0.3354 | 0.3264 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | 0.0102 | 0.2762 |
| seed_p | 147 | -0.4695 | -0.0498 |
| seed_p_vs_seed_pars | 106 | -0.7220 | -0.5125 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
