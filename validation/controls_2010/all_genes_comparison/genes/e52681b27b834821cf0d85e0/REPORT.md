# YHR190W
Status: ok. Length: 1485 nt. Measured usable bases: 1022. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1022 | 0.1803 | 0.1590 |
| rnafold | ok | 1022 | 0.1844 | 0.1439 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 775 | 0.1306 | -0.0474 |
| seed_p | 775 | -0.0022 | -0.0139 |
| seed_p_vs_seed_pars | 605 | -0.0782 | -0.1615 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
