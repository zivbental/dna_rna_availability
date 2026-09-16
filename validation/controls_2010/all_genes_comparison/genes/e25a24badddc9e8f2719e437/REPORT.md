# YIL009W
Status: ok. Length: 2292 nt. Measured usable bases: 1347. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1347 | 0.3426 | 0.3380 |
| rnafold | ok | 1347 | 0.2745 | 0.2707 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 426 | -0.0157 | -0.1664 |
| seed_p | 426 | -0.2203 | -0.2004 |
| seed_p_vs_seed_pars | 319 | -0.1864 | -0.2124 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
