# YOL061W
Status: ok. Length: 1685 nt. Measured usable bases: 1341. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1341 | 0.2703 | 0.2651 |
| rnafold | ok | 1341 | 0.1841 | 0.2087 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1222 | -0.1029 | -0.2114 |
| seed_p | 1222 | -0.0769 | -0.0774 |
| seed_p_vs_seed_pars | 1040 | -0.1980 | -0.2344 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
