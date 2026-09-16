# YJL054W
Status: ok. Length: 1648 nt. Measured usable bases: 754. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 754 | 0.3272 | 0.3148 |
| rnafold | ok | 754 | 0.2717 | 0.2691 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 89 | -0.7709 | -0.4869 |
| seed_p | 89 | 0.0327 | -0.2538 |
| seed_p_vs_seed_pars | 64 | -0.3388 | -0.5624 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
