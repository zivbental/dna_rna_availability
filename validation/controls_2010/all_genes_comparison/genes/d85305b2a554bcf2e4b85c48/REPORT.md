# YJR065C
Status: ok. Length: 1490 nt. Measured usable bases: 1185. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1185 | 0.3014 | 0.2661 |
| rnafold | ok | 1185 | 0.2064 | 0.1856 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 916 | 0.0715 | 0.0468 |
| seed_p | 916 | -0.0691 | -0.0622 |
| seed_p_vs_seed_pars | 781 | -0.2276 | -0.1941 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
