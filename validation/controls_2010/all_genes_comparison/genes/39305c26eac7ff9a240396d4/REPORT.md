# YDR441C
Status: ok. Length: 861 nt. Measured usable bases: 439. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 439 | 0.2279 | 0.2099 |
| rnafold | ok | 439 | 0.2026 | 0.1799 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.0750 | 0.1451 |
| seed_p | 118 | 0.2426 | 0.1955 |
| seed_p_vs_seed_pars | 105 | 0.2528 | 0.2550 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
