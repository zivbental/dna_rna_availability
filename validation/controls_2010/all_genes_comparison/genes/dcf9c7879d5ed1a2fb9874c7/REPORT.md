# YNR009W
Status: ok. Length: 1052 nt. Measured usable bases: 363. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 363 | 0.3712 | 0.3580 |
| rnafold | ok | 363 | 0.3389 | 0.3521 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 21 | 0.2605 | 0.2353 |
| seed_p | 21 | 0.3624 | 0.1576 |
| seed_p_vs_seed_pars | 6 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
