# YJR062C
Status: ok. Length: 1450 nt. Measured usable bases: 580. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 580 | 0.3927 | 0.3891 |
| rnafold | ok | 580 | 0.3695 | 0.3604 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 56 | -0.0353 | 0.0788 |
| seed_p | 56 | 0.0045 | 0.0154 |
| seed_p_vs_seed_pars | 44 | 0.1404 | 0.1894 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
