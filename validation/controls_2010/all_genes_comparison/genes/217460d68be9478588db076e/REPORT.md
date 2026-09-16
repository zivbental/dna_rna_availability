# YDR090C
Status: ok. Length: 1380 nt. Measured usable bases: 676. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 676 | 0.2948 | 0.2832 |
| rnafold | ok | 676 | 0.2716 | 0.2711 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.1441 | -0.0531 |
| seed_p | 137 | 0.1483 | 0.1057 |
| seed_p_vs_seed_pars | 99 | 0.1004 | -0.0545 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
