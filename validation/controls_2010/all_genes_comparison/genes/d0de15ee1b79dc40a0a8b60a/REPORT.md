# YDR261C
Status: ok. Length: 1848 nt. Measured usable bases: 1082. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1082 | 0.2902 | 0.2703 |
| rnafold | ok | 1082 | 0.2039 | 0.2068 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 363 | -0.1798 | -0.1839 |
| seed_p | 363 | -0.3921 | -0.2480 |
| seed_p_vs_seed_pars | 267 | -0.5429 | -0.3433 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
