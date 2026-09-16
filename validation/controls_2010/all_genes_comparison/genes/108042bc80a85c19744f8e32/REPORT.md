# YHR057C
Status: ok. Length: 708 nt. Measured usable bases: 407. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 407 | 0.2920 | 0.2357 |
| rnafold | ok | 407 | 0.2825 | 0.2384 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 131 | 0.0674 | -0.3212 |
| seed_p | 131 | 0.3865 | 0.2770 |
| seed_p_vs_seed_pars | 92 | -0.1360 | -0.1302 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
