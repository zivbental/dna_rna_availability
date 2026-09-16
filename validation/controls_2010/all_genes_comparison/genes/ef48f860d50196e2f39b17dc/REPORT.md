# YNL158W
Status: ok. Length: 1044 nt. Measured usable bases: 393. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 393 | 0.2459 | 0.2309 |
| rnafold | ok | 393 | 0.1802 | 0.2302 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | -0.0355 | 0.0665 |
| seed_p | 98 | 0.0442 | -0.1132 |
| seed_p_vs_seed_pars | 75 | 0.1651 | -0.1036 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
