# YNL026W
Status: ok. Length: 1595 nt. Measured usable bases: 727. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 727 | 0.2269 | 0.2224 |
| rnafold | ok | 727 | 0.1575 | 0.1796 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 103 | 0.4967 | 0.3383 |
| seed_p | 103 | 0.5375 | 0.3844 |
| seed_p_vs_seed_pars | 85 | 0.7107 | 0.7242 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
