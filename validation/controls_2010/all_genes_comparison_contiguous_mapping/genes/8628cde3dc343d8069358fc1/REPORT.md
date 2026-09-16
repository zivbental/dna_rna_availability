# YAL012W
Status: ok. Length: 1352 nt. Measured usable bases: 1230.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1230 | 0.3218 | 0.3076 |
| rnafold | ok | 1230 | 0.1876 | 0.1810 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1216 | -0.0966 | -0.1140 |
| seed_p | 1216 | -0.2087 | -0.1215 |
| seed_p_vs_seed_pars | 1098 | -0.2655 | -0.1639 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
