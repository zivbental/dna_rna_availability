# YGR019W
Status: ok. Length: 1551 nt. Measured usable bases: 724. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 724 | 0.3391 | 0.3256 |
| rnafold | ok | 724 | 0.2327 | 0.2360 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 119 | 0.1622 | -0.2583 |
| seed_p | 119 | -0.2115 | -0.0785 |
| seed_p_vs_seed_pars | 94 | -0.4380 | -0.3504 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
