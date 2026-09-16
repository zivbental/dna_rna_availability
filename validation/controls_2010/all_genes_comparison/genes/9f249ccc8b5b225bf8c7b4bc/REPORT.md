# YCL052C
Status: ok. Length: 1437 nt. Measured usable bases: 611. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 611 | 0.2263 | 0.1851 |
| rnafold | ok | 611 | 0.2637 | 0.2404 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | 0.7218 | 0.7700 |
| seed_p | 73 | -0.1074 | -0.1612 |
| seed_p_vs_seed_pars | 64 | -0.2018 | -0.1802 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
