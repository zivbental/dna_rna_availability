# YOR175C
Status: ok. Length: 2077 nt. Measured usable bases: 1416. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1416 | 0.2526 | 0.2308 |
| rnafold | ok | 1416 | 0.2497 | 0.2296 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 847 | -0.1012 | -0.1653 |
| seed_p | 847 | -0.0954 | -0.0472 |
| seed_p_vs_seed_pars | 655 | -0.1530 | -0.1047 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
