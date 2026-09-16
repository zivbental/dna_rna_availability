# YPL260W
Status: ok. Length: 1833 nt. Measured usable bases: 643. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 643 | 0.3475 | 0.3295 |
| rnafold | ok | 643 | 0.2823 | 0.2581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | -0.2879 | 0.0322 |
| seed_p | 70 | 0.2805 | 0.2190 |
| seed_p_vs_seed_pars | 53 | 0.3105 | 0.4268 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
