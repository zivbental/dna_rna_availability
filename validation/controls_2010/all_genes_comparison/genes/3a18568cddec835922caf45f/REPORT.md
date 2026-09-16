# YOR136W
Status: ok. Length: 1266 nt. Measured usable bases: 1085. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1085 | 0.2532 | 0.2438 |
| rnafold | ok | 1085 | 0.1968 | 0.1932 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1010 | -0.0344 | 0.0973 |
| seed_p | 1010 | -0.1304 | -0.1118 |
| seed_p_vs_seed_pars | 954 | -0.3451 | -0.3231 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
