# YJL109C
Status: ok. Length: 5398 nt. Measured usable bases: 2796. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2796 | 0.3325 | 0.3187 |
| rnafold | ok | 2796 | 0.2612 | 0.2508 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 661 | -0.1393 | 0.0081 |
| seed_p | 661 | -0.1957 | -0.1425 |
| seed_p_vs_seed_pars | 439 | -0.3475 | -0.3012 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
