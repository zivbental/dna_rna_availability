# YFL010C
Status: ok. Length: 790 nt. Measured usable bases: 629. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 629 | 0.3235 | 0.3254 |
| rnafold | ok | 629 | 0.3085 | 0.3074 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 500 | -0.4195 | -0.4206 |
| seed_p | 500 | -0.4711 | -0.3553 |
| seed_p_vs_seed_pars | 419 | -0.5081 | -0.3390 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
