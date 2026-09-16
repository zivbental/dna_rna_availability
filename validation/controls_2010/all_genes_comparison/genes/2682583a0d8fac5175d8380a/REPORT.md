# YDR294C
Status: ok. Length: 1839 nt. Measured usable bases: 1204. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1204 | 0.2993 | 0.2982 |
| rnafold | ok | 1204 | 0.3219 | 0.3080 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 609 | -0.1985 | -0.0764 |
| seed_p | 609 | -0.0880 | -0.0880 |
| seed_p_vs_seed_pars | 469 | -0.1292 | -0.2519 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
