# YBR173C
Status: ok. Length: 510 nt. Measured usable bases: 324. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 324 | 0.2639 | 0.2635 |
| rnafold | ok | 324 | 0.2848 | 0.2953 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | -0.1000 | -0.1531 |
| seed_p | 203 | 0.0098 | -0.0264 |
| seed_p_vs_seed_pars | 142 | 0.1303 | 0.0297 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
