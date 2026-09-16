# YHL002W
Status: ok. Length: 1415 nt. Measured usable bases: 492. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 492 | 0.4105 | 0.4112 |
| rnafold | ok | 492 | 0.3053 | 0.3021 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 41 | 0.1999 | 0.2434 |
| seed_p | 41 | -0.3000 | -0.3074 |
| seed_p_vs_seed_pars | 24 | -0.5905 | -0.6800 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
