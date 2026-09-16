# YHR003C
Status: ok. Length: 1428 nt. Measured usable bases: 627. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 627 | 0.3283 | 0.3264 |
| rnafold | ok | 627 | 0.3512 | 0.3547 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | 0.0906 | 0.0945 |
| seed_p | 72 | 0.3312 | 0.2408 |
| seed_p_vs_seed_pars | 50 | -0.0054 | 0.0433 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
