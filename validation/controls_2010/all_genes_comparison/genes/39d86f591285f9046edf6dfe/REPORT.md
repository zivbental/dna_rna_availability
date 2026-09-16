# YJL101C
Status: ok. Length: 2397 nt. Measured usable bases: 1219. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1219 | 0.3068 | 0.3012 |
| rnafold | ok | 1219 | 0.2428 | 0.2463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 274 | -0.0291 | -0.1747 |
| seed_p | 274 | -0.0354 | -0.0583 |
| seed_p_vs_seed_pars | 215 | -0.2184 | -0.1121 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
