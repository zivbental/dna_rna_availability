# YHR050W
Status: ok. Length: 1696 nt. Measured usable bases: 1074. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1074 | 0.3135 | 0.3017 |
| rnafold | ok | 1074 | 0.2922 | 0.2755 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 516 | -0.1054 | -0.2123 |
| seed_p | 516 | -0.1077 | -0.0759 |
| seed_p_vs_seed_pars | 346 | -0.4475 | -0.4301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
