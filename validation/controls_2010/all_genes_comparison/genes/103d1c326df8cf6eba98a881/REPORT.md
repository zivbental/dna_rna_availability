# YKL067W
Status: ok. Length: 714 nt. Measured usable bases: 531. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 531 | 0.4366 | 0.4262 |
| rnafold | ok | 531 | 0.2975 | 0.2715 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 351 | -0.3277 | -0.4464 |
| seed_p | 351 | -0.4781 | -0.5132 |
| seed_p_vs_seed_pars | 304 | -0.4294 | -0.4060 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
