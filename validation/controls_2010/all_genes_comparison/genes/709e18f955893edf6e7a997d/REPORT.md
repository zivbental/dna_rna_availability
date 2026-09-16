# YJR109C
Status: ok. Length: 3526 nt. Measured usable bases: 1324. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1324 | 0.3297 | 0.3138 |
| rnafold | ok | 1324 | 0.2612 | 0.2573 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 116 | -0.2819 | -0.4524 |
| seed_p | 116 | -0.5273 | -0.4682 |
| seed_p_vs_seed_pars | 86 | -0.5607 | -0.5456 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
