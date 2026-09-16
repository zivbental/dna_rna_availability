# YOL094C
Status: ok. Length: 1026 nt. Measured usable bases: 418. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 418 | 0.3050 | 0.3120 |
| rnafold | ok | 418 | 0.2473 | 0.2550 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.1582 | 0.0229 |
| seed_p | 49 | 0.1900 | 0.2748 |
| seed_p_vs_seed_pars | 44 | 0.1610 | 0.5440 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
