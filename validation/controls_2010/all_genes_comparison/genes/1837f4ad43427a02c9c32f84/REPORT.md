# YLR008C
Status: ok. Length: 770 nt. Measured usable bases: 485. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 485 | 0.2569 | 0.2603 |
| rnafold | ok | 485 | 0.2582 | 0.2522 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 292 | 0.4463 | 0.3204 |
| seed_p | 292 | 0.1810 | 0.2715 |
| seed_p_vs_seed_pars | 238 | -0.0824 | -0.1162 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
