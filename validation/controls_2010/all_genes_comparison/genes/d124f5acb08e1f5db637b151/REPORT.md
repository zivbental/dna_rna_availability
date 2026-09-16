# YLR163C
Status: ok. Length: 1569 nt. Measured usable bases: 765. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 765 | 0.3265 | 0.3198 |
| rnafold | ok | 765 | 0.2572 | 0.2704 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | -0.0983 | -0.5685 |
| seed_p | 149 | -0.3813 | -0.5144 |
| seed_p_vs_seed_pars | 94 | -0.4477 | -0.6622 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
