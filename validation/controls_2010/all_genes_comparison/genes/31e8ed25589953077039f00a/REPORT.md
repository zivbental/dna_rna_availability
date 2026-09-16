# YMR120C
Status: ok. Length: 1960 nt. Measured usable bases: 1145. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1145 | 0.2942 | 0.2893 |
| rnafold | ok | 1145 | 0.2316 | 0.2273 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 410 | -0.2305 | -0.1569 |
| seed_p | 410 | -0.1674 | -0.1224 |
| seed_p_vs_seed_pars | 316 | -0.2878 | -0.2535 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
