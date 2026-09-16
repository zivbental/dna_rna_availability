# YOL056W
Status: ok. Length: 1192 nt. Measured usable bases: 469. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 469 | 0.3111 | 0.3016 |
| rnafold | ok | 469 | 0.1993 | 0.1730 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 47 | 0.0740 | 0.1010 |
| seed_p | 47 | 0.7937 | 0.6394 |
| seed_p_vs_seed_pars | 34 | 0.2415 | 0.3606 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
