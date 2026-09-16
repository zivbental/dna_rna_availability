# YJL096W
Status: ok. Length: 584 nt. Measured usable bases: 290. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 290 | 0.3035 | 0.2800 |
| rnafold | ok | 290 | 0.3181 | 0.3031 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | 0.6614 | 0.5650 |
| seed_p | 71 | 0.2699 | 0.3709 |
| seed_p_vs_seed_pars | 60 | 0.2623 | 0.2769 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
