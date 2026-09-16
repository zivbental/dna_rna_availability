# YNL081C
Status: ok. Length: 639 nt. Measured usable bases: 358. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 358 | 0.3604 | 0.3571 |
| rnafold | ok | 358 | 0.3727 | 0.3853 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | -0.4059 | -0.4390 |
| seed_p | 135 | -0.5274 | -0.5706 |
| seed_p_vs_seed_pars | 86 | -0.6822 | -0.5771 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
