# YNL010W
Status: ok. Length: 867 nt. Measured usable bases: 731. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 731 | 0.3317 | 0.3141 |
| rnafold | ok | 731 | 0.2520 | 0.2542 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 649 | -0.1699 | -0.1076 |
| seed_p | 649 | -0.1956 | -0.1551 |
| seed_p_vs_seed_pars | 583 | -0.1868 | -0.1595 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
