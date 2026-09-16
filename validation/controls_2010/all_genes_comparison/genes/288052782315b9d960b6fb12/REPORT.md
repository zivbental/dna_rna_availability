# YJL130C
Status: ok. Length: 7346 nt. Measured usable bases: 4577. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 4577 | 0.2790 | 0.2647 |
| rnafold | ok | 4577 | 0.2279 | 0.2184 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2095 | 0.0445 | 0.0083 |
| seed_p | 2095 | -0.0573 | -0.0436 |
| seed_p_vs_seed_pars | 1601 | -0.2081 | -0.1834 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
