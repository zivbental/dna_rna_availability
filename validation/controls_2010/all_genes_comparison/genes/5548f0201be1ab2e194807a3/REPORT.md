# YNR035C
Status: ok. Length: 1096 nt. Measured usable bases: 847. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 847 | 0.3108 | 0.3047 |
| rnafold | ok | 847 | 0.2701 | 0.2887 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 716 | 0.1310 | -0.0340 |
| seed_p | 716 | -0.0349 | -0.0626 |
| seed_p_vs_seed_pars | 576 | -0.1748 | -0.2918 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
