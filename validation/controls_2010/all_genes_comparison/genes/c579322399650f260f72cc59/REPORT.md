# YPL235W
Status: ok. Length: 1575 nt. Measured usable bases: 972. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 972 | 0.3835 | 0.3792 |
| rnafold | ok | 972 | 0.3087 | 0.3081 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 390 | -0.3061 | -0.3774 |
| seed_p | 390 | -0.6179 | -0.5544 |
| seed_p_vs_seed_pars | 308 | -0.6971 | -0.6219 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
