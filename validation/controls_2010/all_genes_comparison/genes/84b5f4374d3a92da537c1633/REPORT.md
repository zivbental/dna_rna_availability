# YNL066W
Status: ok. Length: 1819 nt. Measured usable bases: 1302. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1302 | 0.3114 | 0.3029 |
| rnafold | ok | 1302 | 0.2686 | 0.2674 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1187 | -0.1006 | -0.0997 |
| seed_p | 1187 | -0.0998 | -0.1502 |
| seed_p_vs_seed_pars | 1081 | -0.1377 | -0.2283 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
