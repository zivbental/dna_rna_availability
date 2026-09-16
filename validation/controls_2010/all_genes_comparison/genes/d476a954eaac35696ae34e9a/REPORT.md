# YNL134C
Status: ok. Length: 1226 nt. Measured usable bases: 961. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 961 | 0.3498 | 0.3492 |
| rnafold | ok | 961 | 0.3052 | 0.3075 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 752 | -0.2640 | -0.2614 |
| seed_p | 752 | -0.3739 | -0.3671 |
| seed_p_vs_seed_pars | 614 | -0.4675 | -0.4276 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
