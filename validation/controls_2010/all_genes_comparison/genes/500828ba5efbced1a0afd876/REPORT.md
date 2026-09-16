# YJR070C
Status: ok. Length: 1086 nt. Measured usable bases: 926. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 926 | 0.3223 | 0.3156 |
| rnafold | ok | 926 | 0.2588 | 0.2535 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 818 | -0.0841 | -0.0482 |
| seed_p | 818 | -0.0830 | -0.1109 |
| seed_p_vs_seed_pars | 712 | -0.1009 | -0.1287 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
