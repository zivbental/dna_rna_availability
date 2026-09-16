# YAR002C-A
Status: ok. Length: 763 nt. Measured usable bases: 627.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 627 | 0.2541 | 0.2620 |
| rnafold | ok | 627 | 0.1935 | 0.2480 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 605 | 0.0159 | -0.0285 |
| seed_p | 605 | -0.0478 | -0.0828 |
| seed_p_vs_seed_pars | 531 | 0.0134 | -0.0221 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
