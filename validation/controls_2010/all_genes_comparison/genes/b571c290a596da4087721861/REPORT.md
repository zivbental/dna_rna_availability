# YOR066W
Status: ok. Length: 2134 nt. Measured usable bases: 877. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 877 | 0.3016 | 0.2863 |
| rnafold | ok | 877 | 0.2723 | 0.2463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | 0.0945 | 0.0329 |
| seed_p | 91 | -0.2297 | -0.2528 |
| seed_p_vs_seed_pars | 74 | -0.5792 | -0.5327 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
