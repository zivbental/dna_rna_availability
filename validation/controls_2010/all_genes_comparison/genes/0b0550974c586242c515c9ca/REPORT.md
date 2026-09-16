# YJL198W
Status: ok. Length: 2889 nt. Measured usable bases: 1745. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1745 | 0.2168 | 0.2127 |
| rnafold | ok | 1745 | 0.1691 | 0.1704 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 635 | 0.0858 | 0.0022 |
| seed_p | 635 | -0.0332 | -0.0272 |
| seed_p_vs_seed_pars | 476 | -0.2064 | -0.2264 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
