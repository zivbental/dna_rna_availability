# YBR202W
Status: ok. Length: 2778 nt. Measured usable bases: 1279. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1279 | 0.2958 | 0.2797 |
| rnafold | ok | 1279 | 0.2559 | 0.2531 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 170 | 0.0700 | -0.1508 |
| seed_p | 170 | -0.0990 | -0.1338 |
| seed_p_vs_seed_pars | 126 | -0.0370 | 0.0022 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
