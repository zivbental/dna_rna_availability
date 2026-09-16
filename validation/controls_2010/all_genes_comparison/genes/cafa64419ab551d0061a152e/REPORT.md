# YBR043C
Status: ok. Length: 2345 nt. Measured usable bases: 1032. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1032 | 0.3728 | 0.3676 |
| rnafold | ok | 1032 | 0.3493 | 0.3375 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | -0.0091 | -0.1549 |
| seed_p | 132 | -0.3467 | -0.3551 |
| seed_p_vs_seed_pars | 115 | -0.3005 | -0.2780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
