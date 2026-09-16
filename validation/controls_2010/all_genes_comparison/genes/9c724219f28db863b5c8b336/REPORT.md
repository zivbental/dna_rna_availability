# YOL130W
Status: ok. Length: 3091 nt. Measured usable bases: 1735. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1735 | 0.3159 | 0.3086 |
| rnafold | ok | 1735 | 0.2744 | 0.2713 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 404 | 0.1314 | 0.0290 |
| seed_p | 404 | -0.0042 | 0.0704 |
| seed_p_vs_seed_pars | 290 | 0.0974 | 0.0316 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
