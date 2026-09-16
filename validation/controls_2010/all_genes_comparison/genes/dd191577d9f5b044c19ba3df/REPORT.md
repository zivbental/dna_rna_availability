# YJL052W
Status: ok. Length: 1205 nt. Measured usable bases: 396. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 396 | 0.3902 | 0.3958 |
| rnafold | ok | 396 | 0.3645 | 0.3718 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 133 | -0.4263 | -0.3033 |
| seed_p | 133 | -0.2657 | -0.1002 |
| seed_p_vs_seed_pars | 84 | -0.2969 | -0.2768 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
