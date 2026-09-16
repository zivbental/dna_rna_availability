# YGL193C
Status: ok. Length: 357 nt. Measured usable bases: 164. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 164 | 0.2345 | 0.1975 |
| rnafold | ok | 164 | 0.2953 | 0.2750 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.2561 | 0.1379 |
| seed_p | 58 | -0.3980 | -0.3208 |
| seed_p_vs_seed_pars | 49 | -0.2428 | -0.3468 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
