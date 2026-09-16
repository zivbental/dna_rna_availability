# YLR420W
Status: ok. Length: 1198 nt. Measured usable bases: 755. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 755 | 0.3052 | 0.3032 |
| rnafold | ok | 755 | 0.2862 | 0.2753 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 376 | 0.0542 | -0.0396 |
| seed_p | 376 | -0.0439 | -0.0601 |
| seed_p_vs_seed_pars | 193 | -0.1084 | -0.1922 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
