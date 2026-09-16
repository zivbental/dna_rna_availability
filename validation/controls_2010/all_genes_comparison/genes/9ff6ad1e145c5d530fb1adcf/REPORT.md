# YHR174W
Status: ok. Length: 1555 nt. Measured usable bases: 503. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 503 | 0.1958 | 0.1950 |
| rnafold | ok | 503 | 0.1341 | 0.1435 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 334 | -0.0355 | -0.3445 |
| seed_p | 334 | -0.1166 | -0.2952 |
| seed_p_vs_seed_pars | 312 | -0.1732 | -0.3925 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
