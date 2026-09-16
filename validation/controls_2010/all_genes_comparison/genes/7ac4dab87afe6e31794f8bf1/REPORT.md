# YFL007W
Status: ok. Length: 6623 nt. Measured usable bases: 2744. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2744 | 0.2804 | 0.2608 |
| rnafold | ok | 2744 | 0.2568 | 0.2419 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 303 | -0.3880 | -0.3561 |
| seed_p | 303 | -0.3802 | -0.3558 |
| seed_p_vs_seed_pars | 173 | -0.2022 | -0.1567 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
