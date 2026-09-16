# YMR010W
Status: ok. Length: 1637 nt. Measured usable bases: 921. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 921 | 0.2402 | 0.2411 |
| rnafold | ok | 921 | 0.1558 | 0.1696 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 392 | -0.0536 | -0.1500 |
| seed_p | 392 | -0.2236 | -0.2401 |
| seed_p_vs_seed_pars | 299 | -0.2675 | -0.2283 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
