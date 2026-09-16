# YNL155W
Status: ok. Length: 1086 nt. Measured usable bases: 490. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 490 | 0.3500 | 0.3528 |
| rnafold | ok | 490 | 0.3446 | 0.3604 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 89 | -0.3309 | -0.0892 |
| seed_p | 89 | -0.2877 | 0.0143 |
| seed_p_vs_seed_pars | 68 | -0.2237 | -0.1147 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
