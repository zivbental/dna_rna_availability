# YHR019C
Status: ok. Length: 1766 nt. Measured usable bases: 1602. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1602 | 0.3025 | 0.3052 |
| rnafold | ok | 1602 | 0.2257 | 0.2390 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1595 | -0.1092 | -0.0715 |
| seed_p | 1595 | -0.1175 | -0.1241 |
| seed_p_vs_seed_pars | 1447 | -0.2852 | -0.2400 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
