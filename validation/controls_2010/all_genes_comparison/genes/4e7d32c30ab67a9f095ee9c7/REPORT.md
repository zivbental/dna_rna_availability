# YPL093W
Status: ok. Length: 2241 nt. Measured usable bases: 1636. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1636 | 0.3401 | 0.3245 |
| rnafold | ok | 1636 | 0.2892 | 0.2695 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1357 | 0.1559 | 0.0563 |
| seed_p | 1357 | -0.1244 | -0.1097 |
| seed_p_vs_seed_pars | 1086 | -0.1577 | -0.0952 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
