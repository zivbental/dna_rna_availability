# YLR130C
Status: ok. Length: 1457 nt. Measured usable bases: 1036. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1036 | 0.3487 | 0.3296 |
| rnafold | ok | 1036 | 0.2381 | 0.2508 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 658 | 0.0488 | -0.2741 |
| seed_p | 658 | -0.1095 | -0.1894 |
| seed_p_vs_seed_pars | 536 | -0.2095 | -0.2746 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
