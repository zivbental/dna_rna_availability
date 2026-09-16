# YAL036C
Status: ok. Length: 1297 nt. Measured usable bases: 869.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 869 | 0.3339 | 0.3090 |
| rnafold | ok | 869 | 0.2795 | 0.2751 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 528 | 0.0125 | 0.0524 |
| seed_p | 528 | -0.1754 | -0.1413 |
| seed_p_vs_seed_pars | 436 | -0.2580 | -0.2675 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
