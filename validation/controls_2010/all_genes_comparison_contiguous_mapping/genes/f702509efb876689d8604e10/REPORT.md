# YAL041W
Status: ok. Length: 2711 nt. Measured usable bases: 1094.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1094 | 0.2899 | 0.2898 |
| rnafold | ok | 1094 | 0.2419 | 0.2377 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | 0.0170 | 0.0999 |
| seed_p | 87 | -0.0024 | 0.0246 |
| seed_p_vs_seed_pars | 67 | -0.2921 | -0.2379 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
