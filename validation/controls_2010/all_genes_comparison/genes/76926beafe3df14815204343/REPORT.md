# YDL123W
Status: ok. Length: 485 nt. Measured usable bases: 277. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 277 | 0.2560 | 0.2361 |
| rnafold | ok | 277 | 0.2000 | 0.2067 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 123 | 0.2514 | 0.1908 |
| seed_p | 123 | 0.3210 | 0.2969 |
| seed_p_vs_seed_pars | 102 | 0.1739 | 0.1663 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
