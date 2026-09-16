# YBR185C
Status: ok. Length: 1004 nt. Measured usable bases: 435. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 435 | 0.2185 | 0.2144 |
| rnafold | ok | 435 | 0.1540 | 0.1530 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 95 | 0.0593 | 0.0685 |
| seed_p | 95 | 0.1319 | 0.1303 |
| seed_p_vs_seed_pars | 81 | -0.3057 | -0.0729 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
