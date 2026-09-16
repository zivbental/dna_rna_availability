# YML127W
Status: ok. Length: 2775 nt. Measured usable bases: 1160. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1160 | 0.2348 | 0.2204 |
| rnafold | ok | 1160 | 0.2162 | 0.2031 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 437 | 0.1532 | 0.1093 |
| seed_p | 437 | 0.0364 | -0.0848 |
| seed_p_vs_seed_pars | 294 | -0.0754 | -0.1589 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
