# YJR017C
Status: ok. Length: 754 nt. Measured usable bases: 488. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 488 | 0.2615 | 0.2540 |
| rnafold | ok | 488 | 0.2362 | 0.2170 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 338 | -0.1375 | 0.0711 |
| seed_p | 338 | 0.0743 | 0.0142 |
| seed_p_vs_seed_pars | 299 | -0.0429 | -0.1008 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
