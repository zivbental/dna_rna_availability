# YER120W
Status: ok. Length: 861 nt. Measured usable bases: 680. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 680 | 0.3202 | 0.3124 |
| rnafold | ok | 680 | 0.2902 | 0.2780 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 643 | -0.1002 | -0.0387 |
| seed_p | 643 | -0.1572 | -0.1097 |
| seed_p_vs_seed_pars | 520 | -0.0770 | -0.0291 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
