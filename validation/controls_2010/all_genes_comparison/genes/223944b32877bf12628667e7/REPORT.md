# YMR054W
Status: ok. Length: 2806 nt. Measured usable bases: 1432. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1432 | 0.2569 | 0.2441 |
| rnafold | ok | 1432 | 0.1661 | 0.1554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 329 | 0.1489 | 0.3016 |
| seed_p | 329 | 0.2764 | 0.2951 |
| seed_p_vs_seed_pars | 255 | 0.3604 | 0.3934 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
