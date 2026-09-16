# YOL136C
Status: ok. Length: 1707 nt. Measured usable bases: 738. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 738 | 0.2511 | 0.2520 |
| rnafold | ok | 738 | 0.1671 | 0.1786 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | -0.1630 | -0.0839 |
| seed_p | 71 | 0.3373 | 0.2986 |
| seed_p_vs_seed_pars | 49 | 0.0658 | 0.1426 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
