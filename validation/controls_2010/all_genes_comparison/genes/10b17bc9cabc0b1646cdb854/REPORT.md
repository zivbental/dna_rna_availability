# YOR042W
Status: ok. Length: 1287 nt. Measured usable bases: 613. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 613 | 0.3997 | 0.4001 |
| rnafold | ok | 613 | 0.3398 | 0.3557 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 107 | -0.4586 | 0.0001 |
| seed_p | 107 | -0.3145 | -0.2486 |
| seed_p_vs_seed_pars | 88 | -0.4042 | -0.3777 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
