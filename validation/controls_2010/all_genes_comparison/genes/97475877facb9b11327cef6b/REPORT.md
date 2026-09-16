# YLR257W
Status: ok. Length: 1245 nt. Measured usable bases: 878. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 878 | 0.3286 | 0.3237 |
| rnafold | ok | 878 | 0.3012 | 0.3130 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 573 | -0.0464 | -0.0855 |
| seed_p | 573 | -0.1316 | -0.1338 |
| seed_p_vs_seed_pars | 450 | -0.2421 | -0.2868 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
