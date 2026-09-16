# YLR253W
Status: ok. Length: 1899 nt. Measured usable bases: 712. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 712 | 0.2931 | 0.2835 |
| rnafold | ok | 712 | 0.2200 | 0.2366 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.0390 | -0.3423 |
| seed_p | 57 | -0.3518 | -0.5180 |
| seed_p_vs_seed_pars | 44 | 0.0106 | -0.0557 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
