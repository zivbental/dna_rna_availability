# YBR074W
Status: ok. Length: 2962 nt. Measured usable bases: 1582. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1582 | 0.2681 | 0.2624 |
| rnafold | ok | 1582 | 0.1728 | 0.1705 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 396 | -0.0262 | -0.1034 |
| seed_p | 396 | -0.1690 | -0.0984 |
| seed_p_vs_seed_pars | 302 | -0.2654 | -0.1108 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
