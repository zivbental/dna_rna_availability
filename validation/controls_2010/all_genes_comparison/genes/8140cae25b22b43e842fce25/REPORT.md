# YBR118W
Status: ok. Length: 1479 nt. Measured usable bases: 85. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 85 | 0.2251 | 0.2486 |
| rnafold | ok | 85 | 0.1323 | 0.1482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.5175 | -0.7863 |
| seed_p | 46 | -0.3437 | -0.3966 |
| seed_p_vs_seed_pars | 30 | -0.6002 | -0.6202 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
