# YML013W
Status: ok. Length: 1979 nt. Measured usable bases: 957. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 957 | 0.3417 | 0.3251 |
| rnafold | ok | 957 | 0.3465 | 0.3336 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | 0.1420 | 0.3256 |
| seed_p | 129 | 0.1969 | 0.3118 |
| seed_p_vs_seed_pars | 98 | -0.0400 | 0.0263 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
