# YBR162C
Status: ok. Length: 1759 nt. Measured usable bases: 1485. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1485 | 0.3330 | 0.3218 |
| rnafold | ok | 1485 | 0.2424 | 0.2576 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1388 | -0.2245 | -0.1878 |
| seed_p | 1388 | -0.3199 | -0.2779 |
| seed_p_vs_seed_pars | 1235 | -0.3461 | -0.3272 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
