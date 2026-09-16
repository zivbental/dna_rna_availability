# YOR155C
Status: ok. Length: 1605 nt. Measured usable bases: 668. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 668 | 0.3741 | 0.3275 |
| rnafold | ok | 668 | 0.3553 | 0.3282 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | 0.2463 | 0.0425 |
| seed_p | 68 | 0.2081 | 0.1905 |
| seed_p_vs_seed_pars | 42 | 0.0742 | -0.0053 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
