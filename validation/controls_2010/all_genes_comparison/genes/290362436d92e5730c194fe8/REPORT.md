# YPL270W
Status: ok. Length: 2412 nt. Measured usable bases: 1158. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1158 | 0.3028 | 0.2933 |
| rnafold | ok | 1158 | 0.2571 | 0.2535 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | 0.2463 | 0.3004 |
| seed_p | 203 | 0.1336 | 0.0969 |
| seed_p_vs_seed_pars | 135 | 0.1046 | 0.1651 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
