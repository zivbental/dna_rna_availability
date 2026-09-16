# YJR051W
Status: ok. Length: 1578 nt. Measured usable bases: 795. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 795 | 0.2477 | 0.2409 |
| rnafold | ok | 795 | 0.2088 | 0.1946 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 187 | -0.0311 | -0.0160 |
| seed_p | 187 | 0.2077 | 0.2364 |
| seed_p_vs_seed_pars | 108 | -0.2029 | 0.0989 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
