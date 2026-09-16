# YNL085W
Status: ok. Length: 3018 nt. Measured usable bases: 1705. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1705 | 0.2718 | 0.2598 |
| rnafold | ok | 1705 | 0.2494 | 0.2499 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 587 | -0.2940 | -0.1652 |
| seed_p | 587 | -0.2458 | -0.2000 |
| seed_p_vs_seed_pars | 477 | -0.2281 | -0.2069 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
