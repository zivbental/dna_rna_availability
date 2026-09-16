# YAL007C
Status: ok. Length: 842 nt. Measured usable bases: 613.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 613 | 0.2507 | 0.2394 |
| rnafold | ok | 613 | 0.2797 | 0.2504 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 380 | -0.1832 | -0.3569 |
| seed_p | 380 | -0.2499 | -0.3138 |
| seed_p_vs_seed_pars | 293 | -0.1038 | -0.1622 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
