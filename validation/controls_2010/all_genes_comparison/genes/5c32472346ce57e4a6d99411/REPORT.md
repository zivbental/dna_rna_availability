# YPL172C
Status: ok. Length: 1539 nt. Measured usable bases: 686. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 686 | 0.3376 | 0.3254 |
| rnafold | ok | 686 | 0.2845 | 0.2752 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.2210 | -0.5556 |
| seed_p | 79 | -0.4734 | -0.4929 |
| seed_p_vs_seed_pars | 62 | -0.6259 | -0.6114 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
