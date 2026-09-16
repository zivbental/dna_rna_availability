# YMR203W
Status: ok. Length: 1440 nt. Measured usable bases: 1106. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1106 | 0.2754 | 0.2582 |
| rnafold | ok | 1106 | 0.2412 | 0.2267 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 932 | 0.0026 | -0.2102 |
| seed_p | 932 | -0.0445 | -0.1507 |
| seed_p_vs_seed_pars | 785 | -0.2276 | -0.3513 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
