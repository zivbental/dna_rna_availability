# YML052W
Status: ok. Length: 1029 nt. Measured usable bases: 810. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 810 | 0.2882 | 0.2717 |
| rnafold | ok | 810 | 0.2374 | 0.2548 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 633 | 0.0170 | -0.0540 |
| seed_p | 633 | -0.1105 | -0.0593 |
| seed_p_vs_seed_pars | 521 | -0.4650 | -0.3404 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
