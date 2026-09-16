# YNL232W
Status: ok. Length: 971 nt. Measured usable bases: 522. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 522 | 0.3926 | 0.4002 |
| rnafold | ok | 522 | 0.2883 | 0.3161 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.3838 | -0.1930 |
| seed_p | 153 | -0.2988 | -0.3984 |
| seed_p_vs_seed_pars | 106 | -0.2405 | -0.4650 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
