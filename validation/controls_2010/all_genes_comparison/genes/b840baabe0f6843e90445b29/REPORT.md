# YNL052W
Status: ok. Length: 754 nt. Measured usable bases: 554. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 554 | 0.2721 | 0.2878 |
| rnafold | ok | 554 | 0.2838 | 0.2998 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 415 | -0.0979 | -0.3421 |
| seed_p | 415 | -0.2238 | -0.2521 |
| seed_p_vs_seed_pars | 340 | -0.3543 | -0.3499 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
