# YOR280C
Status: ok. Length: 904 nt. Measured usable bases: 425. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 425 | 0.3022 | 0.3028 |
| rnafold | ok | 425 | 0.2519 | 0.2660 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.0918 | -0.3989 |
| seed_p | 34 | -0.2404 | -0.2127 |
| seed_p_vs_seed_pars | 23 | -0.2421 | 0.2152 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
