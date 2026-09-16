# YKL087C
Status: ok. Length: 949 nt. Measured usable bases: 366. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 366 | 0.3324 | 0.3286 |
| rnafold | ok | 366 | 0.3025 | 0.2879 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | -0.1491 | -0.4820 |
| seed_p | 60 | -0.4052 | -0.4556 |
| seed_p_vs_seed_pars | 36 | 0.4402 | 0.3560 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
