# YLR389C
Status: ok. Length: 3274 nt. Measured usable bases: 1568. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1568 | 0.3371 | 0.3259 |
| rnafold | ok | 1568 | 0.2658 | 0.2624 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 286 | 0.0602 | -0.0034 |
| seed_p | 286 | -0.2130 | -0.1228 |
| seed_p_vs_seed_pars | 222 | -0.3692 | -0.3340 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
