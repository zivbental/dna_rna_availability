# YLR206W
Status: ok. Length: 1989 nt. Measured usable bases: 1025. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1025 | 0.2549 | 0.2429 |
| rnafold | ok | 1025 | 0.2502 | 0.2463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 217 | -0.0658 | -0.3367 |
| seed_p | 217 | -0.1195 | -0.0971 |
| seed_p_vs_seed_pars | 170 | -0.1336 | -0.1179 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
