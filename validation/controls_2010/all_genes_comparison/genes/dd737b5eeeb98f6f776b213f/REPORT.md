# YGR143W
Status: ok. Length: 2870 nt. Measured usable bases: 1184. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1184 | 0.3309 | 0.3185 |
| rnafold | ok | 1184 | 0.2810 | 0.2664 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 93 | -0.1502 | -0.1069 |
| seed_p | 93 | -0.2777 | -0.2518 |
| seed_p_vs_seed_pars | 61 | -0.3344 | -0.2941 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
