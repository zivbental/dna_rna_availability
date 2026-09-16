# YNL063W
Status: ok. Length: 1187 nt. Measured usable bases: 487. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 487 | 0.3293 | 0.3065 |
| rnafold | ok | 487 | 0.2888 | 0.2597 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.2623 | -0.2651 |
| seed_p | 37 | -0.0048 | 0.2121 |
| seed_p_vs_seed_pars | 23 | 0.1293 | 0.4348 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
