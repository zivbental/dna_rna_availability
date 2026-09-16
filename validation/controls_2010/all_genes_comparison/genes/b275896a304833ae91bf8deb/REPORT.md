# YDR044W
Status: ok. Length: 1248 nt. Measured usable bases: 885. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 885 | 0.2966 | 0.2814 |
| rnafold | ok | 885 | 0.2424 | 0.2179 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 643 | -0.1425 | -0.0379 |
| seed_p | 643 | -0.3180 | -0.2547 |
| seed_p_vs_seed_pars | 497 | -0.4072 | -0.3181 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
