# YGR257C
Status: ok. Length: 1226 nt. Measured usable bases: 728. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 728 | 0.3299 | 0.3145 |
| rnafold | ok | 728 | 0.1553 | 0.1652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 240 | 0.1375 | 0.1320 |
| seed_p | 240 | 0.0154 | 0.1559 |
| seed_p_vs_seed_pars | 203 | -0.1909 | -0.0741 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
