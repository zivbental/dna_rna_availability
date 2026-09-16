# YMR092C
Status: ok. Length: 1988 nt. Measured usable bases: 1471. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1471 | 0.2901 | 0.2777 |
| rnafold | ok | 1471 | 0.1865 | 0.1896 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 959 | 0.1187 | -0.0638 |
| seed_p | 959 | 0.0523 | -0.0304 |
| seed_p_vs_seed_pars | 703 | 0.0018 | -0.0643 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
