# YLR372W
Status: ok. Length: 1285 nt. Measured usable bases: 1084. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1084 | 0.1920 | 0.1774 |
| rnafold | ok | 1084 | 0.1503 | 0.1399 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 984 | -0.1709 | -0.1145 |
| seed_p | 984 | -0.1153 | -0.1447 |
| seed_p_vs_seed_pars | 847 | -0.2463 | -0.2911 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
