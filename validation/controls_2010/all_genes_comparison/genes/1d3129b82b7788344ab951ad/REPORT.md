# YGR211W
Status: ok. Length: 1719 nt. Measured usable bases: 1286. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1286 | 0.3174 | 0.3123 |
| rnafold | ok | 1286 | 0.2911 | 0.2728 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 980 | -0.0106 | -0.1243 |
| seed_p | 980 | -0.0693 | -0.0388 |
| seed_p_vs_seed_pars | 776 | -0.3171 | -0.2098 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
