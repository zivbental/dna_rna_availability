# YEL063C
Status: ok. Length: 1965 nt. Measured usable bases: 1135. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1135 | 0.3125 | 0.2971 |
| rnafold | ok | 1135 | 0.2656 | 0.2635 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 341 | 0.0318 | 0.0762 |
| seed_p | 341 | -0.0684 | -0.0230 |
| seed_p_vs_seed_pars | 271 | -0.2275 | -0.1648 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
