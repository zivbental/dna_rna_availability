# YDR264C
Status: ok. Length: 2591 nt. Measured usable bases: 1893. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1893 | 0.3202 | 0.2936 |
| rnafold | ok | 1893 | 0.2227 | 0.2077 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1293 | -0.0407 | -0.1506 |
| seed_p | 1293 | -0.3581 | -0.2479 |
| seed_p_vs_seed_pars | 997 | -0.4446 | -0.3328 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
