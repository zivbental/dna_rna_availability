# YGR159C
Status: ok. Length: 1363 nt. Measured usable bases: 1099. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1099 | 0.2940 | 0.2690 |
| rnafold | ok | 1099 | 0.2954 | 0.2795 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 897 | -0.0564 | 0.0635 |
| seed_p | 897 | -0.1341 | -0.0809 |
| seed_p_vs_seed_pars | 754 | -0.1082 | -0.1077 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
