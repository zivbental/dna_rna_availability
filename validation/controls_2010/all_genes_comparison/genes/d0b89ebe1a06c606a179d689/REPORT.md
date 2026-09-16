# YFR052W
Status: ok. Length: 1066 nt. Measured usable bases: 579. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 579 | 0.2734 | 0.2622 |
| rnafold | ok | 579 | 0.2471 | 0.2508 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 284 | -0.0626 | -0.1577 |
| seed_p | 284 | -0.2164 | -0.2589 |
| seed_p_vs_seed_pars | 219 | -0.1082 | -0.1904 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
