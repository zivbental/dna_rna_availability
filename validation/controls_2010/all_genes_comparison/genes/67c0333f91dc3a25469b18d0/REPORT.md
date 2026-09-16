# YJL080C
Status: ok. Length: 3934 nt. Measured usable bases: 2838. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2838 | 0.3449 | 0.3310 |
| rnafold | ok | 2838 | 0.3014 | 0.2866 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1752 | 0.0165 | 0.0655 |
| seed_p | 1752 | -0.1099 | -0.0414 |
| seed_p_vs_seed_pars | 1390 | -0.2841 | -0.2516 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
