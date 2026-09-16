# YOR326W
Status: ok. Length: 5069 nt. Measured usable bases: 2635. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2635 | 0.3439 | 0.3268 |
| rnafold | ok | 2635 | 0.2794 | 0.2690 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 696 | -0.2094 | -0.1622 |
| seed_p | 696 | -0.3717 | -0.4031 |
| seed_p_vs_seed_pars | 558 | -0.3838 | -0.4440 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
