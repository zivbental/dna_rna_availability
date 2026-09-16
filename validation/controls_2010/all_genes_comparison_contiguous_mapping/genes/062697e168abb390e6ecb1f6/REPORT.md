# YAL005C
Status: ok. Length: 2120 nt. Measured usable bases: 585.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 585 | 0.3345 | 0.3184 |
| rnafold | ok | 585 | 0.2133 | 0.2098 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 387 | -0.1471 | -0.2738 |
| seed_p | 387 | -0.0377 | -0.1391 |
| seed_p_vs_seed_pars | 309 | -0.2570 | -0.3287 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
