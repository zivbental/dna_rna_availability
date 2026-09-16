# YIL134W
Status: ok. Length: 1152 nt. Measured usable bases: 490. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 490 | 0.2665 | 0.2718 |
| rnafold | ok | 490 | 0.2268 | 0.2492 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | 0.1451 | -0.0532 |
| seed_p | 73 | -0.0550 | -0.1161 |
| seed_p_vs_seed_pars | 50 | -0.1521 | -0.3635 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
