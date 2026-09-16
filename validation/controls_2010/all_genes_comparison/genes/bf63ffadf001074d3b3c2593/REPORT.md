# YOR132W
Status: ok. Length: 1758 nt. Measured usable bases: 751. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 751 | 0.3542 | 0.3536 |
| rnafold | ok | 751 | 0.2988 | 0.2989 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 114 | -0.1625 | -0.2069 |
| seed_p | 114 | -0.1267 | -0.1891 |
| seed_p_vs_seed_pars | 82 | -0.0581 | -0.1243 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
