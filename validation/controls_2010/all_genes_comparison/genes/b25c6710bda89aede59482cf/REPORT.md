# YDL061C
Status: ok. Length: 760 nt. Measured usable bases: 405. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 405 | 0.2602 | 0.2618 |
| rnafold | ok | 405 | 0.2451 | 0.2387 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 209 | 0.0932 | 0.0324 |
| seed_p | 209 | -0.1619 | -0.1097 |
| seed_p_vs_seed_pars | 149 | -0.1378 | -0.0776 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
