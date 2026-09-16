# YBR235W
Status: ok. Length: 3525 nt. Measured usable bases: 1309. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1309 | 0.3435 | 0.3490 |
| rnafold | ok | 1309 | 0.2812 | 0.2957 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 178 | -0.1454 | -0.0754 |
| seed_p | 178 | -0.1239 | -0.0328 |
| seed_p_vs_seed_pars | 127 | -0.2616 | -0.3314 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
