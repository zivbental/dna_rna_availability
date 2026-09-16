# YBR073W
Status: ok. Length: 2914 nt. Measured usable bases: 1236.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1236 | 0.3622 | 0.3543 |
| rnafold | ok | 1236 | 0.2892 | 0.3035 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.1011 | 0.0009 |
| seed_p | 153 | 0.2790 | 0.0442 |
| seed_p_vs_seed_pars | 124 | 0.1951 | -0.0423 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
