# YLR249W
Status: ok. Length: 3263 nt. Measured usable bases: 3085. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3085 | 0.3429 | 0.3372 |
| rnafold | ok | 3085 | 0.2793 | 0.2833 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 3004 | -0.0517 | -0.1178 |
| seed_p | 3004 | -0.1628 | -0.1561 |
| seed_p_vs_seed_pars | 2943 | -0.2515 | -0.2555 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
