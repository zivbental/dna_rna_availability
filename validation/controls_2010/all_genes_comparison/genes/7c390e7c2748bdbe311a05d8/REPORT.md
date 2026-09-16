# YJL026W
Status: ok. Length: 1379 nt. Measured usable bases: 1127. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1127 | 0.3309 | 0.3148 |
| rnafold | ok | 1127 | 0.2740 | 0.2786 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 988 | -0.2290 | -0.1898 |
| seed_p | 988 | -0.3412 | -0.2909 |
| seed_p_vs_seed_pars | 853 | -0.4278 | -0.3415 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
