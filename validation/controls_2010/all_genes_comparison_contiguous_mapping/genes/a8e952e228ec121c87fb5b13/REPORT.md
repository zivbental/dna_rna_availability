# YBL035C
Status: ok. Length: 2364 nt. Measured usable bases: 884.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 884 | 0.3456 | 0.3384 |
| rnafold | ok | 884 | 0.2837 | 0.2852 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | 0.3954 | -0.0355 |
| seed_p | 64 | 0.1532 | 0.0105 |
| seed_p_vs_seed_pars | 52 | 0.1762 | 0.0873 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
