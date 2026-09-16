# YJL217W
Status: ok. Length: 792 nt. Measured usable bases: 501. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 501 | 0.3065 | 0.3128 |
| rnafold | ok | 501 | 0.2862 | 0.3022 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 272 | -0.1233 | -0.2665 |
| seed_p | 272 | -0.0879 | -0.1804 |
| seed_p_vs_seed_pars | 174 | -0.2196 | -0.2561 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
