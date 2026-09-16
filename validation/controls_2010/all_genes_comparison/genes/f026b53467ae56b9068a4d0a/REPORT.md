# YJR044C
Status: ok. Length: 644 nt. Measured usable bases: 414. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 414 | 0.0518 | 0.0465 |
| rnafold | ok | 414 | 0.0546 | 0.0375 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 233 | 0.2126 | -0.0816 |
| seed_p | 233 | 0.1491 | 0.0115 |
| seed_p_vs_seed_pars | 190 | -0.0124 | -0.1231 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
