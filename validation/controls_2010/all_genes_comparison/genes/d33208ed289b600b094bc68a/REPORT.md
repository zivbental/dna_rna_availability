# YLR050C
Status: ok. Length: 548 nt. Measured usable bases: 347. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 347 | 0.2701 | 0.2484 |
| rnafold | ok | 347 | 0.2569 | 0.2762 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 167 | 0.2741 | 0.3907 |
| seed_p | 167 | 0.1967 | 0.2251 |
| seed_p_vs_seed_pars | 142 | -0.0079 | 0.0237 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
