# YHR137W
Status: ok. Length: 1869 nt. Measured usable bases: 1104. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1104 | 0.2829 | 0.2720 |
| rnafold | ok | 1104 | 0.2311 | 0.2230 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 502 | -0.1199 | 0.0109 |
| seed_p | 502 | 0.1770 | 0.1296 |
| seed_p_vs_seed_pars | 339 | 0.0412 | -0.0149 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
