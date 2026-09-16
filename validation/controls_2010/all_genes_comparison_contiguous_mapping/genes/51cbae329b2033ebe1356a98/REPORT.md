# YBL002W
Status: ok. Length: 635 nt. Measured usable bases: 525.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 525 | 0.2858 | 0.2559 |
| rnafold | ok | 525 | 0.1955 | 0.1711 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 469 | -0.2608 | -0.0563 |
| seed_p | 469 | -0.2816 | -0.2990 |
| seed_p_vs_seed_pars | 430 | -0.5034 | -0.4705 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
