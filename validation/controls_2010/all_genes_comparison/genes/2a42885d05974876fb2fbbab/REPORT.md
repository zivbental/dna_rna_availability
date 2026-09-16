# YOR150W
Status: ok. Length: 605 nt. Measured usable bases: 293. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 293 | 0.3630 | 0.3851 |
| rnafold | ok | 293 | 0.2493 | 0.2893 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | -0.4542 | -0.5655 |
| seed_p | 70 | -0.1546 | -0.4086 |
| seed_p_vs_seed_pars | 51 | -0.2631 | -0.3463 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
