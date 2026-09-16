# YCR048W
Status: ok. Length: 2016 nt. Measured usable bases: 1315. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1315 | 0.2321 | 0.1902 |
| rnafold | ok | 1315 | 0.1754 | 0.1527 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 591 | -0.0535 | -0.0550 |
| seed_p | 591 | -0.1489 | -0.1084 |
| seed_p_vs_seed_pars | 449 | -0.2244 | -0.1779 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
