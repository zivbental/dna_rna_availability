# YKL069W
Status: ok. Length: 608 nt. Measured usable bases: 333. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 333 | 0.2600 | 0.2743 |
| rnafold | ok | 333 | 0.2438 | 0.2520 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 161 | 0.2505 | 0.0895 |
| seed_p | 161 | 0.2092 | -0.1004 |
| seed_p_vs_seed_pars | 106 | 0.2824 | -0.1495 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
