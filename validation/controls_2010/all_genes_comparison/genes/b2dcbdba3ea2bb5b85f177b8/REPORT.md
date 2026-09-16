# YOR317W
Status: ok. Length: 2497 nt. Measured usable bases: 1498. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1498 | 0.2821 | 0.2665 |
| rnafold | ok | 1498 | 0.2507 | 0.2446 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 654 | 0.0364 | -0.2385 |
| seed_p | 654 | 0.1333 | 0.1403 |
| seed_p_vs_seed_pars | 368 | -0.1978 | -0.1023 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
