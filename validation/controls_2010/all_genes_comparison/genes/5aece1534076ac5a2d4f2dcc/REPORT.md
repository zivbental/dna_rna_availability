# YDR366C
Status: ok. Length: 399 nt. Measured usable bases: 100. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 100 | 0.1377 | 0.1466 |
| rnafold | ok | 100 | 0.1917 | 0.1656 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 32 | -0.2532 | -0.2384 |
| seed_p | 32 | 0.0361 | 0.0803 |
| seed_p_vs_seed_pars | 29 | -0.4251 | -0.2441 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
