# YJR142W
Status: ok. Length: 1143 nt. Measured usable bases: 450. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 450 | 0.3376 | 0.3152 |
| rnafold | ok | 450 | 0.3184 | 0.2995 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.0980 | -0.2710 |
| seed_p | 37 | 0.0296 | 0.0512 |
| seed_p_vs_seed_pars | 27 | -0.5526 | -0.2970 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
