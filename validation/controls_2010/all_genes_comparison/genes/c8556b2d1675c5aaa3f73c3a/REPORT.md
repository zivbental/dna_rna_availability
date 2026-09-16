# YMR262W
Status: ok. Length: 1074 nt. Measured usable bases: 552. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 552 | 0.2701 | 0.2692 |
| rnafold | ok | 552 | 0.2529 | 0.2471 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 145 | 0.1435 | 0.2702 |
| seed_p | 145 | 0.0528 | 0.2897 |
| seed_p_vs_seed_pars | 94 | -0.1873 | -0.1250 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
