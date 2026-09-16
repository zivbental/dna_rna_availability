# YKR100C
Status: ok. Length: 1359 nt. Measured usable bases: 535. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 535 | 0.2493 | 0.2390 |
| rnafold | ok | 535 | 0.2495 | 0.2335 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 52 | 0.3494 | 0.4180 |
| seed_p | 52 | 0.3799 | 0.3972 |
| seed_p_vs_seed_pars | 37 | 0.1949 | 0.3324 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
