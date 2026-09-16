# YOL124C
Status: ok. Length: 1390 nt. Measured usable bases: 683. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 683 | 0.3262 | 0.3213 |
| rnafold | ok | 683 | 0.3042 | 0.3096 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 131 | -0.4169 | -0.1309 |
| seed_p | 131 | -0.3151 | -0.2303 |
| seed_p_vs_seed_pars | 74 | -0.6275 | -0.6234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
