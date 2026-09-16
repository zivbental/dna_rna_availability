# YDL085C-A
Status: ok. Length: 490 nt. Measured usable bases: 205. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 205 | 0.3486 | 0.3397 |
| rnafold | ok | 205 | 0.0022 | 0.0092 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | -0.1743 | 0.0280 |
| seed_p | 98 | -0.3707 | -0.3598 |
| seed_p_vs_seed_pars | 59 | -0.7204 | -0.7251 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
