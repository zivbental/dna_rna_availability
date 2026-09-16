# YEL007W
Status: ok. Length: 2380 nt. Measured usable bases: 1064. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1064 | 0.2154 | 0.1900 |
| rnafold | ok | 1064 | 0.1739 | 0.1445 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 191 | 0.0963 | 0.2179 |
| seed_p | 191 | 0.0052 | 0.1293 |
| seed_p_vs_seed_pars | 120 | -0.1532 | 0.0769 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
