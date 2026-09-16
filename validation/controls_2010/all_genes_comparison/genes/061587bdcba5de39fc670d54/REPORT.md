# YJL128C
Status: ok. Length: 2222 nt. Measured usable bases: 1016. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1016 | 0.3531 | 0.3462 |
| rnafold | ok | 1016 | 0.3174 | 0.3054 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | -0.0875 | -0.1620 |
| seed_p | 150 | -0.1235 | -0.1627 |
| seed_p_vs_seed_pars | 123 | -0.2059 | -0.2071 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
