# YIL078W
Status: ok. Length: 2318 nt. Measured usable bases: 1967. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1967 | 0.3453 | 0.3449 |
| rnafold | ok | 1967 | 0.2934 | 0.2970 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1799 | -0.1385 | -0.3269 |
| seed_p | 1799 | -0.2254 | -0.2311 |
| seed_p_vs_seed_pars | 1475 | -0.3469 | -0.3100 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
