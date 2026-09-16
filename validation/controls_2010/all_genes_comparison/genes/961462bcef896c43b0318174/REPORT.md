# YNL030W
Status: ok. Length: 546 nt. Measured usable bases: 238. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 238 | 0.3578 | 0.3369 |
| rnafold | ok | 238 | 0.2822 | 0.2429 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 134 | -0.0393 | -0.4247 |
| seed_p | 134 | -0.3292 | -0.5508 |
| seed_p_vs_seed_pars | 122 | -0.2123 | -0.5381 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
