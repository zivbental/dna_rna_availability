# YHR116W
Status: ok. Length: 722 nt. Measured usable bases: 294. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 294 | 0.4311 | 0.4023 |
| rnafold | ok | 294 | 0.4821 | 0.4512 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | -0.2704 | -0.5958 |
| seed_p | 28 | -0.9089 | -0.7279 |
| seed_p_vs_seed_pars | 24 | -0.9603 | -0.8897 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
