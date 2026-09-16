# YMR024W
Status: ok. Length: 1173 nt. Measured usable bases: 571. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 571 | 0.3540 | 0.3417 |
| rnafold | ok | 571 | 0.2447 | 0.2537 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | -0.3996 | -0.5698 |
| seed_p | 66 | -0.5877 | -0.6070 |
| seed_p_vs_seed_pars | 41 | -0.6451 | -0.6940 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
