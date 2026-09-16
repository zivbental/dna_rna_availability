# YKR006C
Status: ok. Length: 864 nt. Measured usable bases: 471. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 471 | 0.3278 | 0.3017 |
| rnafold | ok | 471 | 0.2973 | 0.2637 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | 0.0691 | -0.3490 |
| seed_p | 179 | -0.1898 | -0.1459 |
| seed_p_vs_seed_pars | 131 | -0.2448 | -0.0902 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
