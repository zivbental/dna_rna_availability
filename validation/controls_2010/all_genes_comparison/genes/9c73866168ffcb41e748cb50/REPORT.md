# YMR108W
Status: ok. Length: 2458 nt. Measured usable bases: 1828. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1828 | 0.3050 | 0.2771 |
| rnafold | ok | 1828 | 0.3032 | 0.2754 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1334 | 0.0360 | -0.1366 |
| seed_p | 1334 | -0.0140 | -0.1208 |
| seed_p_vs_seed_pars | 1091 | -0.1550 | -0.2500 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
