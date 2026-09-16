# YKR026C
Status: ok. Length: 1147 nt. Measured usable bases: 557. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 557 | 0.3259 | 0.3109 |
| rnafold | ok | 557 | 0.2598 | 0.2405 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | 0.0398 | 0.0585 |
| seed_p | 203 | -0.1047 | -0.1132 |
| seed_p_vs_seed_pars | 149 | -0.1294 | -0.1296 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
