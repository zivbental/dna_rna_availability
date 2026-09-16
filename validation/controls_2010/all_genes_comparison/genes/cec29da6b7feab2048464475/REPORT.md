# YDR530C
Status: ok. Length: 1080 nt. Measured usable bases: 584. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 584 | 0.2363 | 0.2281 |
| rnafold | ok | 584 | 0.1800 | 0.1959 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 141 | -0.1162 | 0.1391 |
| seed_p | 141 | -0.0471 | -0.0518 |
| seed_p_vs_seed_pars | 104 | -0.2299 | -0.3089 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
