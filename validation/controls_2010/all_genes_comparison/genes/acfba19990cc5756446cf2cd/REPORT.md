# YGL084C
Status: ok. Length: 1832 nt. Measured usable bases: 1079. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1079 | 0.2815 | 0.2661 |
| rnafold | ok | 1079 | 0.2468 | 0.2432 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 440 | -0.2797 | -0.0884 |
| seed_p | 440 | -0.2209 | -0.1606 |
| seed_p_vs_seed_pars | 355 | -0.1850 | -0.1607 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
