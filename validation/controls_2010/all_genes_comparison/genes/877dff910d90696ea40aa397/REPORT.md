# YDR214W
Status: ok. Length: 1250 nt. Measured usable bases: 897. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 897 | 0.2571 | 0.2522 |
| rnafold | ok | 897 | 0.1900 | 0.1953 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 574 | 0.1436 | 0.1059 |
| seed_p | 574 | -0.0080 | 0.0183 |
| seed_p_vs_seed_pars | 458 | 0.0403 | 0.0707 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
