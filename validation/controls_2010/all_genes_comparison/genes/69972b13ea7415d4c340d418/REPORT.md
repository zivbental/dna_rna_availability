# YKL054C
Status: ok. Length: 2490 nt. Measured usable bases: 1039. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1039 | 0.2275 | 0.2052 |
| rnafold | ok | 1039 | 0.2189 | 0.2024 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | -0.0872 | -0.4084 |
| seed_p | 125 | -0.4378 | -0.4225 |
| seed_p_vs_seed_pars | 86 | -0.3586 | -0.2782 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
