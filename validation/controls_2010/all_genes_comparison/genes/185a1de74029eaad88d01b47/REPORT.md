# YCL028W
Status: ok. Length: 1292 nt. Measured usable bases: 858. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 858 | 0.3469 | 0.3375 |
| rnafold | ok | 858 | 0.3034 | 0.2978 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 459 | -0.1519 | -0.1186 |
| seed_p | 459 | 0.0671 | 0.0132 |
| seed_p_vs_seed_pars | 347 | -0.1801 | -0.2020 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
