# YPL184C
Status: ok. Length: 2122 nt. Measured usable bases: 1113. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1113 | 0.3085 | 0.2751 |
| rnafold | ok | 1113 | 0.2611 | 0.2491 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 424 | -0.0494 | -0.3702 |
| seed_p | 424 | -0.0428 | -0.1054 |
| seed_p_vs_seed_pars | 303 | -0.1032 | -0.1085 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
