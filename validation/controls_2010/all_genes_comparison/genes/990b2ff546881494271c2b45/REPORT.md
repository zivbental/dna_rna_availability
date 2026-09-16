# YBL098W
Status: ok. Length: 1529 nt. Measured usable bases: 660. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 660 | 0.2714 | 0.2730 |
| rnafold | ok | 660 | 0.2140 | 0.2005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | 0.0898 | 0.2495 |
| seed_p | 79 | 0.4353 | 0.4617 |
| seed_p_vs_seed_pars | 60 | 0.4076 | 0.1108 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
