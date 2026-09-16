# YGR135W
Status: ok. Length: 919 nt. Measured usable bases: 708. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 708 | 0.3097 | 0.2960 |
| rnafold | ok | 708 | 0.2178 | 0.2000 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 574 | -0.2472 | 0.0999 |
| seed_p | 574 | -0.1207 | -0.0944 |
| seed_p_vs_seed_pars | 511 | -0.3078 | -0.2508 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
