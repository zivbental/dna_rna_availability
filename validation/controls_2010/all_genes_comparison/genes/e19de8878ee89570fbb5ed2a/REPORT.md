# YJL174W
Status: ok. Length: 1118 nt. Measured usable bases: 877. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 877 | 0.2437 | 0.2381 |
| rnafold | ok | 877 | 0.2008 | 0.2028 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 704 | -0.0112 | -0.2286 |
| seed_p | 704 | -0.0303 | -0.0941 |
| seed_p_vs_seed_pars | 617 | -0.0349 | -0.1174 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
