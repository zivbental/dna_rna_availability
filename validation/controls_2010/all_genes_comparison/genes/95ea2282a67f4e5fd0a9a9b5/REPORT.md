# YGL065C
Status: ok. Length: 1512 nt. Measured usable bases: 570. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 570 | 0.3224 | 0.3127 |
| rnafold | ok | 570 | 0.3167 | 0.3216 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | 0.5018 | 0.5074 |
| seed_p | 25 | -0.6181 | -0.6785 |
| seed_p_vs_seed_pars | 21 | -0.7442 | -0.8067 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
