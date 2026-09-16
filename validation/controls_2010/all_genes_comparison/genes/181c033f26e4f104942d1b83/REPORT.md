# YDL143W
Status: ok. Length: 1728 nt. Measured usable bases: 1367. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1367 | 0.2907 | 0.2888 |
| rnafold | ok | 1367 | 0.2580 | 0.2683 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1030 | -0.0115 | -0.0766 |
| seed_p | 1030 | -0.1566 | -0.1421 |
| seed_p_vs_seed_pars | 900 | -0.2046 | -0.1841 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
