# YJL140W
Status: ok. Length: 802 nt. Measured usable bases: 547. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 547 | 0.3506 | 0.3463 |
| rnafold | ok | 547 | 0.2397 | 0.2556 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 284 | -0.1203 | -0.3898 |
| seed_p | 284 | -0.2841 | -0.2554 |
| seed_p_vs_seed_pars | 251 | -0.2344 | -0.2527 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
