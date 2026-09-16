# YHR187W
Status: ok. Length: 1076 nt. Measured usable bases: 459. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 459 | 0.2322 | 0.2391 |
| rnafold | ok | 459 | 0.2569 | 0.2679 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 38 | 0.1387 | 0.1606 |
| seed_p | 38 | -0.3540 | -0.2393 |
| seed_p_vs_seed_pars | 27 | -0.3809 | -0.7237 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
