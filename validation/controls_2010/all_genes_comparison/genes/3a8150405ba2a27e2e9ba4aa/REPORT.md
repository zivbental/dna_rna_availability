# YFR006W
Status: ok. Length: 1879 nt. Measured usable bases: 1047. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1047 | 0.2425 | 0.2422 |
| rnafold | ok | 1047 | 0.1421 | 0.1604 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 536 | 0.1707 | 0.1915 |
| seed_p | 536 | 0.0609 | 0.1024 |
| seed_p_vs_seed_pars | 428 | -0.1206 | -0.0346 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
