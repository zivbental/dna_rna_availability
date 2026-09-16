# YBR212W
Status: ok. Length: 2392 nt. Measured usable bases: 927. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 927 | 0.1946 | 0.1671 |
| rnafold | ok | 927 | 0.1762 | 0.1527 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | 0.2094 | 0.3916 |
| seed_p | 153 | 0.2877 | 0.3003 |
| seed_p_vs_seed_pars | 107 | -0.0669 | 0.0062 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
