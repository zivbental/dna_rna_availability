# YOR091W
Status: ok. Length: 1166 nt. Measured usable bases: 634. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 634 | 0.3767 | 0.3829 |
| rnafold | ok | 634 | 0.3661 | 0.3638 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 196 | -0.0359 | -0.1953 |
| seed_p | 196 | -0.1039 | -0.0790 |
| seed_p_vs_seed_pars | 130 | -0.3663 | -0.2733 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
