# YLR438W
Status: ok. Length: 1385 nt. Measured usable bases: 977. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 977 | 0.3147 | 0.3021 |
| rnafold | ok | 977 | 0.2355 | 0.2292 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 749 | -0.0899 | -0.0731 |
| seed_p | 749 | -0.1779 | -0.1743 |
| seed_p_vs_seed_pars | 636 | -0.3871 | -0.4213 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
