# YOR246C
Status: ok. Length: 1119 nt. Measured usable bases: 856. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 856 | 0.3025 | 0.2877 |
| rnafold | ok | 856 | 0.1705 | 0.1789 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 629 | -0.1160 | -0.1444 |
| seed_p | 629 | -0.2841 | -0.2191 |
| seed_p_vs_seed_pars | 537 | -0.3828 | -0.3530 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
