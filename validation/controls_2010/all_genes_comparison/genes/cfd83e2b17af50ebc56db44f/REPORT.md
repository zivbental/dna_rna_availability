# YPL131W
Status: ok. Length: 1014 nt. Measured usable bases: 975. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 975 | 0.3410 | 0.3310 |
| rnafold | ok | 975 | 0.2671 | 0.2576 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 963 | -0.0237 | -0.1683 |
| seed_p | 963 | -0.0341 | -0.0447 |
| seed_p_vs_seed_pars | 943 | -0.1499 | -0.1627 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
