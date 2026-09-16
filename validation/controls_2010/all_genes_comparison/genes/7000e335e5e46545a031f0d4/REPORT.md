# YNL141W
Status: ok. Length: 1226 nt. Measured usable bases: 888. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 888 | 0.3304 | 0.2956 |
| rnafold | ok | 888 | 0.3132 | 0.2846 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 674 | -0.1857 | -0.1762 |
| seed_p | 674 | -0.3040 | -0.1902 |
| seed_p_vs_seed_pars | 573 | -0.3233 | -0.1941 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
