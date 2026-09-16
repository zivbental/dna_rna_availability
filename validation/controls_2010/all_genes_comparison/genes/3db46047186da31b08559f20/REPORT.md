# YGR155W
Status: ok. Length: 1681 nt. Measured usable bases: 1459. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1459 | 0.3475 | 0.3262 |
| rnafold | ok | 1459 | 0.3037 | 0.2750 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1359 | -0.0960 | -0.1534 |
| seed_p | 1359 | -0.1106 | -0.1198 |
| seed_p_vs_seed_pars | 1222 | -0.3163 | -0.3068 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
