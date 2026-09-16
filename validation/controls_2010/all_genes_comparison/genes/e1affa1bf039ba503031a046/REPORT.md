# YNR012W
Status: ok. Length: 1680 nt. Measured usable bases: 703. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 703 | 0.3215 | 0.3336 |
| rnafold | ok | 703 | 0.2722 | 0.2792 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | 0.2175 | -0.0075 |
| seed_p | 46 | -0.1016 | -0.2093 |
| seed_p_vs_seed_pars | 30 | 0.1051 | 0.0891 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
