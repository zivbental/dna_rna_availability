# YBR137W
Status: ok. Length: 895 nt. Measured usable bases: 385. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 385 | 0.3183 | 0.2911 |
| rnafold | ok | 385 | 0.3204 | 0.2841 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | 0.2760 | 0.0687 |
| seed_p | 71 | -0.3919 | -0.4379 |
| seed_p_vs_seed_pars | 61 | -0.3714 | -0.4064 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
