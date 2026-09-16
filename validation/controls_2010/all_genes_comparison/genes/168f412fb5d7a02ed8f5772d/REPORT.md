# YLR340W
Status: ok. Length: 1087 nt. Measured usable bases: 1007. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1007 | 0.3589 | 0.3214 |
| rnafold | ok | 1007 | 0.2919 | 0.2750 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 987 | -0.2334 | -0.1651 |
| seed_p | 987 | -0.2107 | -0.2069 |
| seed_p_vs_seed_pars | 970 | -0.2680 | -0.2624 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
