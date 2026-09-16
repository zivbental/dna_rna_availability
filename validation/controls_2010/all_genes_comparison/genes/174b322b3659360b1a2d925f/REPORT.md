# YEL025C
Status: ok. Length: 3845 nt. Measured usable bases: 1321. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1321 | 0.3040 | 0.3054 |
| rnafold | ok | 1321 | 0.2268 | 0.2369 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 74 | 0.0022 | -0.1150 |
| seed_p | 74 | -0.0197 | 0.0367 |
| seed_p_vs_seed_pars | 44 | -0.3549 | -0.0138 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
