# YDL178W
Status: ok. Length: 1675 nt. Measured usable bases: 718. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 718 | 0.3940 | 0.3886 |
| rnafold | ok | 718 | 0.2991 | 0.3098 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 100 | 0.2366 | 0.1125 |
| seed_p | 100 | 0.1490 | 0.0079 |
| seed_p_vs_seed_pars | 89 | 0.1812 | 0.0569 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
