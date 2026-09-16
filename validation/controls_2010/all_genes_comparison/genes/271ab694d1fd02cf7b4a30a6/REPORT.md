# YKL003C
Status: ok. Length: 485 nt. Measured usable bases: 252. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 252 | 0.3815 | 0.3903 |
| rnafold | ok | 252 | 0.3679 | 0.3707 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | -0.4934 | -0.5734 |
| seed_p | 62 | -0.1339 | -0.2145 |
| seed_p_vs_seed_pars | 24 | -0.6146 | -0.7285 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
