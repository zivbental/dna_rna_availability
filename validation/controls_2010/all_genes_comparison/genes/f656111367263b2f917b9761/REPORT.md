# YDR211W
Status: ok. Length: 2362 nt. Measured usable bases: 1109. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1109 | 0.3009 | 0.3039 |
| rnafold | ok | 1109 | 0.2904 | 0.2910 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 170 | -0.2370 | -0.2524 |
| seed_p | 170 | -0.2300 | -0.3080 |
| seed_p_vs_seed_pars | 153 | -0.2901 | -0.4462 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
