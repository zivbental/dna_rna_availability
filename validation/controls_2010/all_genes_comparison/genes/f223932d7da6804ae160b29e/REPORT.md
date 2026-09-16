# YML032C
Status: ok. Length: 1752 nt. Measured usable bases: 615. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 615 | 0.2966 | 0.2913 |
| rnafold | ok | 615 | 0.2984 | 0.2899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.0861 | 0.3084 |
| seed_p | 37 | 0.1624 | 0.1254 |
| seed_p_vs_seed_pars | 34 | 0.2019 | 0.2015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
