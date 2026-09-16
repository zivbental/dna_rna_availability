# YCR069W
Status: ok. Length: 1287 nt. Measured usable bases: 952. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 952 | 0.2532 | 0.2558 |
| rnafold | ok | 952 | 0.2061 | 0.2139 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 667 | -0.2567 | 0.0663 |
| seed_p | 667 | -0.3384 | -0.2396 |
| seed_p_vs_seed_pars | 523 | -0.4102 | -0.3166 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
