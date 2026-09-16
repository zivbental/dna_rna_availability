# YLL008W
Status: ok. Length: 2396 nt. Measured usable bases: 973. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 973 | 0.3089 | 0.2996 |
| rnafold | ok | 973 | 0.2853 | 0.2906 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | -0.1588 | -0.3200 |
| seed_p | 121 | -0.3907 | -0.2166 |
| seed_p_vs_seed_pars | 108 | -0.2669 | -0.0943 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
