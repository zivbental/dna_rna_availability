# YJL044C
Status: ok. Length: 1491 nt. Measured usable bases: 767. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 767 | 0.3769 | 0.3530 |
| rnafold | ok | 767 | 0.2830 | 0.2753 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 184 | 0.0047 | -0.2499 |
| seed_p | 184 | 0.1675 | -0.0431 |
| seed_p_vs_seed_pars | 122 | 0.3793 | 0.1662 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
