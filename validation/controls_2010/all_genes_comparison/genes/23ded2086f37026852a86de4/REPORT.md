# YDL201W
Status: ok. Length: 1003 nt. Measured usable bases: 488. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 488 | 0.3253 | 0.3197 |
| rnafold | ok | 488 | 0.2973 | 0.2899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | 0.0198 | -0.2084 |
| seed_p | 87 | -0.3519 | -0.3644 |
| seed_p_vs_seed_pars | 63 | -0.3393 | -0.2311 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
