# YDR119W
Status: ok. Length: 2440 nt. Measured usable bases: 1681. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1681 | 0.2766 | 0.2624 |
| rnafold | ok | 1681 | 0.2674 | 0.2516 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 985 | -0.0309 | -0.0446 |
| seed_p | 985 | 0.0218 | 0.0426 |
| seed_p_vs_seed_pars | 722 | -0.1302 | -0.0805 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
