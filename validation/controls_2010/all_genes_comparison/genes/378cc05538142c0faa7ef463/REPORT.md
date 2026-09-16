# YNL111C
Status: ok. Length: 635 nt. Measured usable bases: 405. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 405 | 0.3551 | 0.3497 |
| rnafold | ok | 405 | 0.3067 | 0.3279 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 229 | -0.3080 | -0.3751 |
| seed_p | 229 | -0.4649 | -0.3775 |
| seed_p_vs_seed_pars | 176 | -0.3584 | -0.5715 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
