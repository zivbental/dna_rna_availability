# YLL035W
Status: ok. Length: 2189 nt. Measured usable bases: 889. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 889 | 0.2972 | 0.3014 |
| rnafold | ok | 889 | 0.1962 | 0.1942 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 107 | -0.0137 | -0.1128 |
| seed_p | 107 | -0.4098 | -0.3440 |
| seed_p_vs_seed_pars | 74 | -0.5648 | -0.5168 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
