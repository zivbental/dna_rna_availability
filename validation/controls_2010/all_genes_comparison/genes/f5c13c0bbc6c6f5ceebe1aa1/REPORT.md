# YHL040C
Status: ok. Length: 1884 nt. Measured usable bases: 997. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 997 | 0.3015 | 0.2926 |
| rnafold | ok | 997 | 0.2953 | 0.2983 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 215 | 0.0547 | -0.1096 |
| seed_p | 215 | 0.0542 | -0.0592 |
| seed_p_vs_seed_pars | 191 | -0.1828 | -0.2569 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
