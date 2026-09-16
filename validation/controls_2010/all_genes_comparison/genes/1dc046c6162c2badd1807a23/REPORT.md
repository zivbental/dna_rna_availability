# YER136W
Status: ok. Length: 1762 nt. Measured usable bases: 1162. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1162 | 0.3221 | 0.3128 |
| rnafold | ok | 1162 | 0.3186 | 0.3055 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 640 | -0.0799 | -0.0106 |
| seed_p | 640 | -0.1417 | -0.0421 |
| seed_p_vs_seed_pars | 425 | -0.3826 | -0.2843 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
