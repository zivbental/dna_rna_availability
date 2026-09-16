# YOR043W
Status: ok. Length: 1673 nt. Measured usable bases: 857. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 857 | 0.2894 | 0.2861 |
| rnafold | ok | 857 | 0.2654 | 0.2882 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 241 | 0.0572 | -0.2318 |
| seed_p | 241 | -0.2514 | -0.2582 |
| seed_p_vs_seed_pars | 183 | -0.3379 | -0.2941 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
