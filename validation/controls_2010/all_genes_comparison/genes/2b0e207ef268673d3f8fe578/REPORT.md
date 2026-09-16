# YMR062C
Status: ok. Length: 1411 nt. Measured usable bases: 750. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 750 | 0.3605 | 0.3571 |
| rnafold | ok | 750 | 0.2669 | 0.2655 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 161 | -0.2788 | -0.3694 |
| seed_p | 161 | -0.3787 | -0.2762 |
| seed_p_vs_seed_pars | 130 | -0.2633 | -0.2562 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
