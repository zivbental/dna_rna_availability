# YBR053C
Status: ok. Length: 1171 nt. Measured usable bases: 700.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 700 | 0.3234 | 0.3048 |
| rnafold | ok | 700 | 0.2986 | 0.2789 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 321 | -0.0040 | -0.2306 |
| seed_p | 321 | -0.0879 | -0.2016 |
| seed_p_vs_seed_pars | 264 | -0.2003 | -0.2603 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
