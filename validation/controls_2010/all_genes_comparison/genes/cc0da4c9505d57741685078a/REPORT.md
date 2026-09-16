# YCR077C
Status: ok. Length: 2571 nt. Measured usable bases: 1497. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1497 | 0.2381 | 0.2273 |
| rnafold | ok | 1497 | 0.1803 | 0.1704 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 504 | 0.0102 | -0.0445 |
| seed_p | 504 | -0.0239 | -0.0347 |
| seed_p_vs_seed_pars | 390 | -0.1009 | -0.1220 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
