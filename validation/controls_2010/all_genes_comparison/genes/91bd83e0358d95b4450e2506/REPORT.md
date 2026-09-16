# YKL164C
Status: ok. Length: 1336 nt. Measured usable bases: 738. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 738 | 0.2484 | 0.2281 |
| rnafold | ok | 738 | 0.1529 | 0.1459 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 582 | -0.1216 | -0.1958 |
| seed_p | 582 | -0.3902 | -0.2992 |
| seed_p_vs_seed_pars | 529 | -0.4084 | -0.3188 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
