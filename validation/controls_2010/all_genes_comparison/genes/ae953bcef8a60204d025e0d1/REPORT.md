# YNR038W
Status: ok. Length: 2052 nt. Measured usable bases: 920. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 920 | 0.3065 | 0.2982 |
| rnafold | ok | 920 | 0.2374 | 0.2348 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | 0.0605 | -0.0393 |
| seed_p | 45 | -0.5587 | -0.3462 |
| seed_p_vs_seed_pars | 24 | -0.9872 | -0.7069 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
