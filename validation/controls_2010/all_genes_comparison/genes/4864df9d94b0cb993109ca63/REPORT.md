# YGR084C
Status: ok. Length: 1070 nt. Measured usable bases: 448. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 448 | 0.4190 | 0.3980 |
| rnafold | ok | 448 | 0.3594 | 0.3555 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | 0.1548 | -0.3075 |
| seed_p | 77 | -0.4620 | -0.5747 |
| seed_p_vs_seed_pars | 56 | -0.0194 | -0.2259 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
