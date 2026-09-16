# YDR071C
Status: ok. Length: 714 nt. Measured usable bases: 532. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 532 | 0.3405 | 0.3170 |
| rnafold | ok | 532 | 0.3029 | 0.3055 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 383 | 0.0595 | -0.3293 |
| seed_p | 383 | -0.2001 | -0.2413 |
| seed_p_vs_seed_pars | 290 | -0.3860 | -0.3433 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
