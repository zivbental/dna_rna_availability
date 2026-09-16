# YDL110C
Status: ok. Length: 670 nt. Measured usable bases: 257. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 257 | 0.3158 | 0.3015 |
| rnafold | ok | 257 | 0.2529 | 0.2662 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.0339 | 0.5472 |
| seed_p | 34 | 0.1723 | 0.3828 |
| seed_p_vs_seed_pars | 29 | 0.4105 | 0.8218 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
