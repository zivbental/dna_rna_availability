# YMR208W
Status: ok. Length: 1440 nt. Measured usable bases: 283. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 283 | 0.2655 | 0.2687 |
| rnafold | ok | 283 | 0.2383 | 0.2948 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 134 | 0.0197 | 0.1124 |
| seed_p | 134 | -0.0385 | 0.0634 |
| seed_p_vs_seed_pars | 111 | -0.3967 | -0.2735 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
