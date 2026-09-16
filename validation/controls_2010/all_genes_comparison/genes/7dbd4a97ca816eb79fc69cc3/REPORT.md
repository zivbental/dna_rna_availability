# YJL183W
Status: ok. Length: 1410 nt. Measured usable bases: 1092. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1092 | 0.3334 | 0.3142 |
| rnafold | ok | 1092 | 0.2995 | 0.2915 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 810 | -0.1761 | 0.0655 |
| seed_p | 810 | -0.1840 | 0.0138 |
| seed_p_vs_seed_pars | 642 | -0.3979 | -0.2040 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
