# YNL208W
Status: ok. Length: 728 nt. Measured usable bases: 625. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 625 | 0.3348 | 0.3490 |
| rnafold | ok | 625 | 0.2957 | 0.3126 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 558 | 0.0539 | -0.1497 |
| seed_p | 558 | -0.1676 | -0.1256 |
| seed_p_vs_seed_pars | 534 | -0.2085 | -0.1809 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
