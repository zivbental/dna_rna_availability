# YAL040C
Status: ok. Length: 2073 nt. Measured usable bases: 870.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 870 | 0.1600 | 0.1424 |
| rnafold | ok | 870 | 0.1674 | 0.1476 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | -0.5357 | -0.1935 |
| seed_p | 77 | -0.4834 | -0.4599 |
| seed_p_vs_seed_pars | 44 | -0.5341 | -0.5994 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
