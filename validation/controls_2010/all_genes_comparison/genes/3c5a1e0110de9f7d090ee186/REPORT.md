# YLR028C
Status: ok. Length: 2036 nt. Measured usable bases: 1594. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1594 | 0.3465 | 0.3369 |
| rnafold | ok | 1594 | 0.2992 | 0.3014 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1298 | 0.0050 | 0.0059 |
| seed_p | 1298 | -0.1521 | -0.0998 |
| seed_p_vs_seed_pars | 1102 | -0.3600 | -0.2680 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
