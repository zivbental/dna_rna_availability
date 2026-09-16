# YPR034W
Status: ok. Length: 1745 nt. Measured usable bases: 941. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 941 | 0.3448 | 0.3256 |
| rnafold | ok | 941 | 0.3575 | 0.3273 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 189 | -0.0462 | 0.0659 |
| seed_p | 189 | 0.1963 | 0.1676 |
| seed_p_vs_seed_pars | 150 | -0.1383 | -0.1505 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
