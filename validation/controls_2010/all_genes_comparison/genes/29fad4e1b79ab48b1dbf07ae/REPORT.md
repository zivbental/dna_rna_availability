# YOR251C
Status: ok. Length: 1035 nt. Measured usable bases: 669. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 669 | 0.3356 | 0.3012 |
| rnafold | ok | 669 | 0.3383 | 0.3116 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 305 | -0.2604 | -0.1462 |
| seed_p | 305 | -0.2807 | -0.2466 |
| seed_p_vs_seed_pars | 268 | 0.0537 | -0.0352 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
