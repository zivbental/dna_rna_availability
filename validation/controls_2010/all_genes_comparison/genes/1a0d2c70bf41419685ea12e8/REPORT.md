# YOR320C
Status: ok. Length: 1721 nt. Measured usable bases: 953. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 953 | 0.3392 | 0.3322 |
| rnafold | ok | 953 | 0.2551 | 0.2551 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 318 | -0.1099 | -0.1914 |
| seed_p | 318 | -0.1124 | -0.1485 |
| seed_p_vs_seed_pars | 191 | -0.2037 | -0.2157 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
