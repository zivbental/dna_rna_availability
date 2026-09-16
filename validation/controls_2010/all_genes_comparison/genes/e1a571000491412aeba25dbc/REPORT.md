# YMR256C
Status: ok. Length: 350 nt. Measured usable bases: 184. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 184 | 0.3838 | 0.3816 |
| rnafold | ok | 184 | 0.3921 | 0.3993 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.0786 | -0.2459 |
| seed_p | 44 | 0.1778 | 0.0021 |
| seed_p_vs_seed_pars | 30 | 0.1453 | 0.2073 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
