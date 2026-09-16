# YNL125C
Status: ok. Length: 2133 nt. Measured usable bases: 927. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 927 | 0.2971 | 0.3038 |
| rnafold | ok | 927 | 0.2216 | 0.2407 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.1715 | -0.2829 |
| seed_p | 72 | -0.4318 | -0.3756 |
| seed_p_vs_seed_pars | 46 | -0.6526 | -0.6828 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
