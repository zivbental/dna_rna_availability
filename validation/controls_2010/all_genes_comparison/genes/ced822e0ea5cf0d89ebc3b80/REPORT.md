# YBR205W
Status: ok. Length: 1215 nt. Measured usable bases: 957. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 957 | 0.3527 | 0.3337 |
| rnafold | ok | 957 | 0.3320 | 0.3248 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 734 | -0.2887 | -0.2996 |
| seed_p | 734 | -0.4241 | -0.3934 |
| seed_p_vs_seed_pars | 635 | -0.3722 | -0.3266 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
