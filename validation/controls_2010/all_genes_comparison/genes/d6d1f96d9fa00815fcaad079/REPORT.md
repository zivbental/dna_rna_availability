# YLL043W
Status: ok. Length: 2103 nt. Measured usable bases: 1172. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1172 | 0.3722 | 0.3620 |
| rnafold | ok | 1172 | 0.3449 | 0.3469 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 277 | -0.5088 | -0.4461 |
| seed_p | 277 | -0.2075 | -0.1595 |
| seed_p_vs_seed_pars | 213 | -0.6452 | -0.5961 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
