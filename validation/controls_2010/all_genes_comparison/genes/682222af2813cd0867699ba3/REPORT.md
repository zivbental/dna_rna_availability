# YDL004W
Status: ok. Length: 768 nt. Measured usable bases: 553. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 553 | 0.2754 | 0.2524 |
| rnafold | ok | 553 | 0.2459 | 0.2406 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 372 | -0.2540 | -0.0442 |
| seed_p | 372 | -0.3500 | -0.3345 |
| seed_p_vs_seed_pars | 307 | -0.1996 | -0.2797 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
