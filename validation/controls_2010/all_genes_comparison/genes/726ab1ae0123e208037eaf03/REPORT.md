# YIL065C
Status: ok. Length: 572 nt. Measured usable bases: 325. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 325 | 0.2728 | 0.2924 |
| rnafold | ok | 325 | 0.3063 | 0.3147 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 144 | 0.0579 | 0.1139 |
| seed_p | 144 | 0.0425 | 0.0569 |
| seed_p_vs_seed_pars | 128 | -0.0356 | -0.0019 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
