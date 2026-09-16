# YML080W
Status: ok. Length: 1493 nt. Measured usable bases: 563. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 563 | 0.3541 | 0.3594 |
| rnafold | ok | 563 | 0.3348 | 0.3399 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | 0.1953 | -0.0567 |
| seed_p | 62 | -0.7508 | -0.7229 |
| seed_p_vs_seed_pars | 55 | -0.6299 | -0.6867 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
