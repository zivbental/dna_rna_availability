# YOR288C
Status: ok. Length: 1053 nt. Measured usable bases: 556. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 556 | 0.3253 | 0.3163 |
| rnafold | ok | 556 | 0.3225 | 0.3276 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.3827 | -0.4201 |
| seed_p | 82 | -0.4436 | -0.4400 |
| seed_p_vs_seed_pars | 44 | -0.3452 | -0.0281 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
