# YJL124C
Status: ok. Length: 881 nt. Measured usable bases: 484. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 484 | 0.3759 | 0.3746 |
| rnafold | ok | 484 | 0.3329 | 0.3309 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 185 | -0.2649 | -0.2593 |
| seed_p | 185 | -0.3163 | -0.1691 |
| seed_p_vs_seed_pars | 136 | -0.3012 | -0.1748 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
