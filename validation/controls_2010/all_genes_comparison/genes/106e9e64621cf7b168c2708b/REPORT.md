# YCR024C-B
Status: ok. Length: 439 nt. Measured usable bases: 295. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 295 | 0.1511 | 0.1501 |
| rnafold | ok | 295 | 0.1014 | 0.1133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 199 | 0.2858 | -0.0032 |
| seed_p | 199 | 0.2295 | 0.1336 |
| seed_p_vs_seed_pars | 144 | -0.0915 | -0.0886 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
