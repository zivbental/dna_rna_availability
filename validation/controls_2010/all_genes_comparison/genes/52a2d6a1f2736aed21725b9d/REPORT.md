# YLR073C
Status: ok. Length: 713 nt. Measured usable bases: 399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 399 | 0.2316 | 0.2347 |
| rnafold | ok | 399 | 0.1822 | 0.1589 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 156 | -0.3214 | -0.3972 |
| seed_p | 156 | -0.0794 | -0.1162 |
| seed_p_vs_seed_pars | 108 | -0.3188 | -0.4192 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
