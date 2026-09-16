# YKL013C
Status: ok. Length: 697 nt. Measured usable bases: 508. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 508 | 0.3428 | 0.3243 |
| rnafold | ok | 508 | 0.2836 | 0.2769 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 378 | -0.0526 | -0.1431 |
| seed_p | 378 | -0.0719 | -0.1946 |
| seed_p_vs_seed_pars | 276 | 0.0950 | 0.0035 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
