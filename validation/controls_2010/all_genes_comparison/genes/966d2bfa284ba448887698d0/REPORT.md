# YNL220W
Status: ok. Length: 1483 nt. Measured usable bases: 371. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 371 | 0.2765 | 0.2509 |
| rnafold | ok | 371 | 0.2080 | 0.1841 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 271 | -0.2042 | -0.1141 |
| seed_p | 271 | -0.0785 | -0.1357 |
| seed_p_vs_seed_pars | 226 | -0.2925 | -0.1439 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
