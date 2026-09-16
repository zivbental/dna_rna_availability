# YER025W
Status: ok. Length: 1891 nt. Measured usable bases: 1510. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1510 | 0.3064 | 0.2987 |
| rnafold | ok | 1510 | 0.2934 | 0.2856 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1337 | -0.0722 | -0.0782 |
| seed_p | 1337 | -0.1777 | -0.1506 |
| seed_p_vs_seed_pars | 1073 | -0.1844 | -0.1903 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
