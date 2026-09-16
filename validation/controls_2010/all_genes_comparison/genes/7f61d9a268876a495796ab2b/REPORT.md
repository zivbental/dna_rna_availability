# YBR010W
Status: ok. Length: 582 nt. Measured usable bases: 316. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 316 | 0.3671 | 0.3472 |
| rnafold | ok | 316 | 0.3591 | 0.3284 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 206 | -0.4983 | -0.6012 |
| seed_p | 206 | -0.2215 | -0.2581 |
| seed_p_vs_seed_pars | 150 | -0.3089 | -0.4038 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
