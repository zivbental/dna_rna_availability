# YKL178C
Status: ok. Length: 1413 nt. Measured usable bases: 1198. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1198 | 0.2581 | 0.2302 |
| rnafold | ok | 1198 | 0.1883 | 0.1830 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1066 | -0.0469 | 0.0330 |
| seed_p | 1066 | -0.1405 | 0.0006 |
| seed_p_vs_seed_pars | 930 | -0.1500 | -0.1022 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
