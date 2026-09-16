# YMR309C
Status: ok. Length: 2663 nt. Measured usable bases: 1768. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1768 | 0.2932 | 0.2924 |
| rnafold | ok | 1768 | 0.2360 | 0.2487 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 774 | -0.1087 | 0.0478 |
| seed_p | 774 | -0.0277 | -0.0169 |
| seed_p_vs_seed_pars | 587 | -0.0325 | -0.0871 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
