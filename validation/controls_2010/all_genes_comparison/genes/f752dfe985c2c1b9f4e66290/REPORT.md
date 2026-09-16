# YJL134W
Status: ok. Length: 1305 nt. Measured usable bases: 781. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 781 | 0.2571 | 0.2296 |
| rnafold | ok | 781 | 0.2002 | 0.1908 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 362 | -0.1853 | -0.2385 |
| seed_p | 362 | -0.2293 | -0.1391 |
| seed_p_vs_seed_pars | 287 | -0.4128 | -0.3059 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
