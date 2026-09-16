# YCR082W
Status: ok. Length: 516 nt. Measured usable bases: 376. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 376 | 0.3375 | 0.3311 |
| rnafold | ok | 376 | 0.2635 | 0.2842 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 260 | -0.1558 | -0.3088 |
| seed_p | 260 | -0.0042 | -0.0498 |
| seed_p_vs_seed_pars | 221 | -0.0584 | -0.0387 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
