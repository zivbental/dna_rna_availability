# YLL041C
Status: ok. Length: 1113 nt. Measured usable bases: 713. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 713 | 0.2954 | 0.2728 |
| rnafold | ok | 713 | 0.2530 | 0.2220 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 337 | -0.1848 | -0.0600 |
| seed_p | 337 | -0.3820 | -0.3021 |
| seed_p_vs_seed_pars | 229 | -0.3225 | -0.4168 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
