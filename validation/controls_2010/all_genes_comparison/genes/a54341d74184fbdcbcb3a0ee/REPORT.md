# YNL160W
Status: ok. Length: 1327 nt. Measured usable bases: 1004. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1004 | 0.2704 | 0.2468 |
| rnafold | ok | 1004 | 0.2220 | 0.2042 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 723 | -0.2435 | -0.2864 |
| seed_p | 723 | -0.1914 | -0.2316 |
| seed_p_vs_seed_pars | 633 | -0.2707 | -0.3013 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
