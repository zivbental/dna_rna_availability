# YAL029C
Status: ok. Length: 4499 nt. Measured usable bases: 1834.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1834 | 0.3887 | 0.3733 |
| rnafold | ok | 1834 | 0.3178 | 0.3150 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 140 | 0.1886 | 0.2829 |
| seed_p | 140 | 0.2620 | 0.2405 |
| seed_p_vs_seed_pars | 107 | 0.3898 | 0.4730 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
