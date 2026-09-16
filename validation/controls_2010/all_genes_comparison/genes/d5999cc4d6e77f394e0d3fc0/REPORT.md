# YDR178W
Status: ok. Length: 904 nt. Measured usable bases: 520. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 520 | 0.3073 | 0.2860 |
| rnafold | ok | 520 | 0.2701 | 0.2754 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 279 | -0.0138 | 0.1471 |
| seed_p | 279 | -0.2107 | -0.0328 |
| seed_p_vs_seed_pars | 210 | -0.3707 | -0.1547 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
