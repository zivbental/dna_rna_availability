# YJL210W
Status: ok. Length: 881 nt. Measured usable bases: 558. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 558 | 0.3699 | 0.3410 |
| rnafold | ok | 558 | 0.2837 | 0.2958 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 263 | -0.0430 | -0.0376 |
| seed_p | 263 | -0.0063 | -0.1449 |
| seed_p_vs_seed_pars | 209 | -0.2464 | -0.3485 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
