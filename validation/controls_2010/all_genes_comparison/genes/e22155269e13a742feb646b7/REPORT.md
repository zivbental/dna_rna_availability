# YMR261C
Status: ok. Length: 3457 nt. Measured usable bases: 1791. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1791 | 0.2723 | 0.2492 |
| rnafold | ok | 1791 | 0.1881 | 0.1747 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 303 | -0.3212 | -0.1349 |
| seed_p | 303 | -0.3916 | -0.2308 |
| seed_p_vs_seed_pars | 224 | -0.2982 | -0.1729 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
