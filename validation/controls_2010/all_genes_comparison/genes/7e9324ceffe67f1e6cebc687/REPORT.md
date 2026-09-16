# YLR058C
Status: ok. Length: 1566 nt. Measured usable bases: 1340. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1340 | 0.3268 | 0.3038 |
| rnafold | ok | 1340 | 0.3397 | 0.3178 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1178 | -0.0127 | -0.1512 |
| seed_p | 1178 | -0.2569 | -0.2347 |
| seed_p_vs_seed_pars | 1019 | -0.3483 | -0.3233 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
