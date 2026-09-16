# YBL003C
Status: ok. Length: 611 nt. Measured usable bases: 401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 401 | 0.3811 | 0.3839 |
| rnafold | ok | 401 | 0.2694 | 0.2966 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 280 | -0.2704 | -0.3463 |
| seed_p | 280 | -0.4816 | -0.4940 |
| seed_p_vs_seed_pars | 231 | -0.5378 | -0.5791 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
