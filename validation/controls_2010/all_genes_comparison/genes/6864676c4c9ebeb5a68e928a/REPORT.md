# YEL056W
Status: ok. Length: 1500 nt. Measured usable bases: 666. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 666 | 0.2267 | 0.2295 |
| rnafold | ok | 666 | 0.2029 | 0.2092 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 85 | 0.1455 | 0.0532 |
| seed_p | 85 | 0.1688 | 0.0973 |
| seed_p_vs_seed_pars | 34 | -0.1515 | 0.2028 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
