# YKR048C
Status: ok. Length: 1377 nt. Measured usable bases: 1102. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1102 | 0.3257 | 0.3310 |
| rnafold | ok | 1102 | 0.2142 | 0.2111 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 957 | -0.1586 | -0.1497 |
| seed_p | 957 | -0.2935 | -0.3188 |
| seed_p_vs_seed_pars | 805 | -0.3542 | -0.3399 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
