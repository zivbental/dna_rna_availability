# YPL061W
Status: ok. Length: 1659 nt. Measured usable bases: 1505. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1505 | 0.2628 | 0.2581 |
| rnafold | ok | 1505 | 0.2505 | 0.2411 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1517 | 0.0305 | -0.0292 |
| seed_p | 1517 | 0.0106 | -0.0169 |
| seed_p_vs_seed_pars | 1407 | -0.0068 | -0.0272 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
