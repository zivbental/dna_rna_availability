# YJL166W
Status: ok. Length: 550 nt. Measured usable bases: 385. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 385 | 0.3782 | 0.3607 |
| rnafold | ok | 385 | 0.3283 | 0.3203 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 234 | -0.4463 | -0.6774 |
| seed_p | 234 | -0.6602 | -0.6755 |
| seed_p_vs_seed_pars | 220 | -0.5749 | -0.6947 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
