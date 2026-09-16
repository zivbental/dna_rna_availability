# YGR175C
Status: ok. Length: 1714 nt. Measured usable bases: 1433. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1433 | 0.2928 | 0.2886 |
| rnafold | ok | 1433 | 0.1957 | 0.2094 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1355 | -0.0337 | 0.0433 |
| seed_p | 1355 | -0.1046 | -0.1215 |
| seed_p_vs_seed_pars | 1146 | -0.0963 | -0.1619 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
