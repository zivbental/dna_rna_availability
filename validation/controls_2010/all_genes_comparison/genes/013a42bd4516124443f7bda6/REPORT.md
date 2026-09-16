# YJL065C
Status: ok. Length: 602 nt. Measured usable bases: 397. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 397 | 0.3671 | 0.3445 |
| rnafold | ok | 397 | 0.2925 | 0.2754 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 204 | -0.4087 | -0.3049 |
| seed_p | 204 | -0.3854 | -0.3046 |
| seed_p_vs_seed_pars | 178 | -0.0601 | -0.0200 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
