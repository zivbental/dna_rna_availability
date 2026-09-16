# YJL004C
Status: ok. Length: 885 nt. Measured usable bases: 397. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 397 | 0.3081 | 0.2914 |
| rnafold | ok | 397 | 0.2332 | 0.2206 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | 0.1109 | 0.1207 |
| seed_p | 69 | 0.2372 | 0.1779 |
| seed_p_vs_seed_pars | 29 | -0.4411 | -0.3661 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
