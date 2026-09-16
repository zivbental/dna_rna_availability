# YGR007W
Status: ok. Length: 1153 nt. Measured usable bases: 574. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 574 | 0.4166 | 0.3915 |
| rnafold | ok | 574 | 0.3031 | 0.3007 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 152 | -0.2104 | -0.1676 |
| seed_p | 152 | -0.1254 | -0.1199 |
| seed_p_vs_seed_pars | 67 | -0.6942 | -0.6247 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
