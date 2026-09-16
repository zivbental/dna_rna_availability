# YDR354W
Status: ok. Length: 1304 nt. Measured usable bases: 873. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 873 | 0.3233 | 0.3273 |
| rnafold | ok | 873 | 0.2164 | 0.2368 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 444 | -0.4378 | -0.1287 |
| seed_p | 444 | -0.3595 | -0.3455 |
| seed_p_vs_seed_pars | 354 | -0.3809 | -0.3540 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
