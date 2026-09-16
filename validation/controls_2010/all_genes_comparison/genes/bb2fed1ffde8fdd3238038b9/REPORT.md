# YLR167W
Status: ok. Length: 568 nt. Measured usable bases: 399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 399 | 0.3847 | 0.3727 |
| rnafold | ok | 399 | 0.1983 | 0.2262 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 360 | -0.2372 | -0.3576 |
| seed_p | 360 | -0.3138 | -0.2463 |
| seed_p_vs_seed_pars | 359 | -0.4587 | -0.3015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
