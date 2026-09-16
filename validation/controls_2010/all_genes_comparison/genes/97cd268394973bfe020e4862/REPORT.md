# YIL076W
Status: ok. Length: 1067 nt. Measured usable bases: 804. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 804 | 0.3420 | 0.3349 |
| rnafold | ok | 804 | 0.3186 | 0.3282 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 652 | -0.1256 | -0.2257 |
| seed_p | 652 | -0.1975 | -0.1949 |
| seed_p_vs_seed_pars | 489 | -0.3697 | -0.3154 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
